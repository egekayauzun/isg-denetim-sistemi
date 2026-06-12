import io
import streamlit as st
import cv2
import numpy as np
import tempfile

from ui.styles import inject_css
from ui.components import (
    SEKTORLER,
    render_navbar,
    handle_back_navigation,
    render_landing,
    render_sector_button,
    render_upload_hint,
    render_panel_title,
    render_kural_paneli,
    render_report_block,
    render_step_indicator,
)

# ==========================================
# 🧠 SİSTEM AYARLARI VE HAFIZA
# ==========================================
st.set_page_config(page_title="ISG-P | Akıllı İSG Denetimi", layout="wide")
inject_css()

if "secilen_kurallar" not in st.session_state:
    st.session_state.secilen_kurallar = {
        "🏥 Hastane": {},
        "👨‍🍳 Gastronomi": {},
        "🏗️ İnşaat": {},
        "🏢 Ofis": {},
    }
if "sayfa" not in st.session_state:
    st.session_state.sayfa = "secim"
if "kategori" not in st.session_state:
    st.session_state.kategori = None
if "analiz_gorsel" not in st.session_state:
    st.session_state.analiz_gorsel = None
if "rapor_satirlari" not in st.session_state:
    st.session_state.rapor_satirlari = []
if "medya_bytes" not in st.session_state:
    st.session_state.medya_bytes = None
if "medya_adi" not in st.session_state:
    st.session_state.medya_adi = None
if "medya_turu" not in st.session_state:
    st.session_state.medya_turu = "foto"
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0

GUVEN_ESIGI = 0.40
UST_USTE_BINME_ESIGI = 0.45
def _medya_turu_belirle(dosya_adi: str) -> str:
    ext = dosya_adi.lower().rsplit(".", 1)[-1]
    return "video" if ext in ("mp4", "avi", "mov") else "foto"


def _medyayi_sifirla():
    st.session_state.medya_bytes = None
    st.session_state.medya_adi = None
    st.session_state.analiz_gorsel = None
    st.session_state.rapor_satirlari = []
    st.session_state.uploader_key += 1


def _sektor_sec(sektor_id):
    st.session_state.kategori = sektor_id
    st.session_state.sayfa = "calisma"
    _medyayi_sifirla()


# ==========================================
# 🚀 MODEL YÜKLEME MANTIĞI
# ==========================================
def modelleri_yukle(secilen_kategori):
    from ultralytics import YOLO

    if secilen_kategori == "🏥 Hastane":
        mod = YOLO("hastanebest.pt")
        isimler = {
            0: "Person", 1: "Shoe Covers", 2: "Surgical Cap", 3: "Surgical Gloves",
            4: "Surgical Gown", 5: "Surgical Mask", 6: "Surgical Scrubs", 7: "face-shields",
            8: "no-facial-gear", 9: "no-medical-attire", 10: "no-surgical-cap", 11: "no-surgical-gloves",
        }
        return [(mod, isimler)]

    if secilen_kategori == "👨‍🍳 Gastronomi":
        mutfak_mod = YOLO("mutfakbest.pt")
        mutfak_isimler = {0: "apron", 1: "chef-hat", 2: "gloves", 3: "no-chef-hat"}
        eldiven_mod = YOLO("eldivenbest.pt")
        eldiven_isimler = {0: "gloves", 1: "no-gloves"}
        apron_mod = YOLO("apronbest.pt")
        apron_isimler = {0: "apron", 1: "no-apron"}
        return [(mutfak_mod, mutfak_isimler), (eldiven_mod, eldiven_isimler), (apron_mod, apron_isimler)]

    if secilen_kategori == "🏢 Ofis":
        ofis_eski_mod = YOLO("ofisbest.pt")
        ofis_eski_isimler = {0: "id-card", 1: "suit", 2: "tie"}
        ofis_yeni_mod = YOLO("yofficebest.pt")
        ofis_yeni_isimler = {0: "id card", 1: "not wear", 2: "person", 3: "tie"}
        return [(ofis_eski_mod, ofis_eski_isimler), (ofis_yeni_mod, ofis_yeni_isimler)]

    if secilen_kategori == "🏗️ İnşaat":
        mod = YOLO("insaatbest.pt")
        isimler = {0: "Gloves", 1: "Helmet", 2: "Non-Helmet", 3: "Person", 4: "Shoes", 5: "Vest", 6: "bare-arms"}
        return [(mod, isimler)]

    return []


def _ihlal_rengi(label: str):
    low = label.lower()
    if "no-" in low or "non-" in low or "bare-" in low or "not wear" in low:
        return (0, 0, 255)
    return (0, 255, 0)


def _gastronomi_filtre(kategori, sirasi, label):
    if kategori != "👨‍🍳 Gastronomi":
        return False
    if sirasi == 0 and label not in ["chef-hat", "no-chef-hat"]:
        return True
    if sirasi == 1 and label not in ["gloves", "no-gloves"]:
        return True
    if sirasi == 2 and label not in ["apron", "no-apron"]:
        return True
    return False


def _ofis_filtre(kategori, sirasi, label):
    if kategori != "🏢 Ofis":
        return False
    if sirasi == 0 and label not in ["suit", "tie"]:
        return True
    if sirasi == 1 and label != "id card":
        return True
    return False


POZITIF_ESIK = 0.40  # Bu eşik üstü = kesin uyumlu


def _kisiye_ata(box, kisi_kutulari):
    """Bir tespiti en yakın / içinde bulunduğu kişiye atar."""
    if not kisi_kutulari:
        return None
    if box is None:
        return 0
    ax1, ay1, ax2, ay2 = box
    a_cx, a_cy = (ax1 + ax2) / 2, (ay1 + ay2) / 2
    for i, (px1, py1, px2, py2) in enumerate(kisi_kutulari):
        if px1 <= a_cx <= px2 and py1 <= a_cy <= py2:
            return i
    nearest, min_d = 0, float("inf")
    for i, (px1, py1, px2, py2) in enumerate(kisi_kutulari):
        d = ((a_cx - (px1 + px2) / 2) ** 2 + (a_cy - (py1 + py2) / 2) ** 2) ** 0.5
        if d < min_d:
            min_d, nearest = d, i
    return nearest


def _foto_rapor_olustur(kategori, kurallar, bulunan_etiketler):
    """
    bulunan_etiketler: [{"isim": str, "conf": float, "box": tuple|None}]
    %50+ pozitif tespit → başarı (bare-arms/non- etiketleri görmezden gelinir).
    """
    rapor = []
    kontrol = bulunan_etiketler.copy()
    for aksesuar_adi, istenen_etiket in kurallar.items():
        positif = next((o for o in kontrol if o["isim"] == istenen_etiket), None)
        p_conf = positif.get("conf", 0.0) if positif else 0.0

        if positif and p_conf >= POZITIF_ESIK:
            rapor.append({"tip": "success",
                          "mesaj": f"Başarılı: {aksesuar_adi} tespit edildi (%{p_conf * 100:.0f})."})
            kontrol.remove(positif)
            continue

        # Pozitif < %50 veya hiç yok → negatif etiketlere bak
        if kategori == "🏢 Ofis" and any(o["isim"] == "not wear" for o in kontrol):
            nw = next(o for o in kontrol if o["isim"] == "not wear")
            rapor.append({"tip": "error",
                          "mesaj": f"Kesin ihlal: {aksesuar_adi} — kurallara uyulmadığı tespit edildi (%{nw.get('conf', 0) * 100:.0f})."})
        elif istenen_etiket == "Helmet" and any(o["isim"] == "Non-Helmet" for o in kontrol):
            nh = next(o for o in kontrol if o["isim"] == "Non-Helmet")
            rapor.append({"tip": "error",
                          "mesaj": f"Kesin ihlal: {aksesuar_adi} — baret takılmıyor (%{nh.get('conf', 0) * 100:.0f})."})
        elif istenen_etiket == "Gloves" and any(o["isim"] == "bare-arms" for o in kontrol):
            ba = next(o for o in kontrol if o["isim"] == "bare-arms")
            rapor.append({"tip": "error",
                          "mesaj": f"Kesin ihlal: {aksesuar_adi} — çıplak el/kol tespit edildi (%{ba.get('conf', 0) * 100:.0f})."})
        elif any(f"no-{istenen_etiket.lower().replace(' ', '-')}" == o["isim"].lower() for o in kontrol):
            no_lbl = next(o for o in kontrol
                          if f"no-{istenen_etiket.lower().replace(' ', '-')}" == o["isim"].lower())
            rapor.append({"tip": "error",
                          "mesaj": f"Kesin ihlal: {aksesuar_adi} — kural ihlali tespit edildi (%{no_lbl.get('conf', 0) * 100:.0f})."})
        elif positif:
            rapor.append({"tip": "error",
                          "mesaj": f"İhlal: {aksesuar_adi} düşük güvenle tespit edildi (%{p_conf * 100:.0f})."})
        else:
            rapor.append({"tip": "error", "mesaj": f"İhlal: {aksesuar_adi} eksik veya bulunamadı."})
    return rapor


def _kisi_bazli_rapor(kategori, kurallar, kisi_kutulari, tespitler):
    """Kişi başına rapor; kişi yoksa genel rapor döndürür."""
    if not kisi_kutulari:
        return _foto_rapor_olustur(kategori, kurallar, tespitler)
    rapor = []
    kisi_tespitleri = {i: [] for i in range(len(kisi_kutulari))}
    for t in tespitler:
        idx = _kisiye_ata(t.get("box"), kisi_kutulari)
        if idx is not None:
            kisi_tespitleri[idx].append(t)
    for i in range(len(kisi_kutulari)):
        rapor.append({"tip": "bolge", "mesaj": f"👤 Person-{i + 1}"})
        rapor.extend(_foto_rapor_olustur(kategori, kurallar, kisi_tespitleri[i]))
    return rapor


def _video_rapor_olustur(kategori, kurallar, video_rapor):
    """video_rapor: {label: max_conf_float}. %50+ → başarı."""
    rapor = []
    for aksesuar_adi, istenen_etiket in kurallar.items():
        conf = video_rapor.get(istenen_etiket, 0.0)
        if conf >= POZITIF_ESIK:
            rapor.append({"tip": "success",
                          "mesaj": f"Başarılı: {aksesuar_adi} tespit edildi (%{conf * 100:.0f})."})
        elif conf >= GUVEN_ESIGI:
            rapor.append({"tip": "error",
                          "mesaj": f"İhlal: {aksesuar_adi} düşük güvenle tespit edildi (%{conf * 100:.0f})."})
        elif kategori == "🏢 Ofis" and "not wear" in video_rapor:
            nw_c = video_rapor["not wear"]
            rapor.append({"tip": "error",
                          "mesaj": f"Kesin ihlal: {aksesuar_adi} — kurallara uyulmadığı tespit edildi (%{nw_c * 100:.0f})."})
        elif istenen_etiket == "Helmet" and "Non-Helmet" in video_rapor:
            nh_c = video_rapor["Non-Helmet"]
            rapor.append({"tip": "error",
                          "mesaj": f"Kesin ihlal: {aksesuar_adi} — baret takılmıyor (%{nh_c * 100:.0f})."})
        elif istenen_etiket == "Gloves" and "bare-arms" in video_rapor:
            ba_c = video_rapor["bare-arms"]
            rapor.append({"tip": "error",
                          "mesaj": f"Kesin ihlal: {aksesuar_adi} — çıplak el/kol tespit edildi (%{ba_c * 100:.0f})."})
        else:
            ihlal_key = f"no-{istenen_etiket.lower().replace(' ', '-')}"
            eslesme = next((k for k in video_rapor if k.lower() == ihlal_key), None)
            if eslesme:
                rapor.append({"tip": "error",
                              "mesaj": f"Kesin ihlal: {aksesuar_adi} — kural ihlali tespit edildi (%{video_rapor[eslesme] * 100:.0f})."})
            else:
                rapor.append({"tip": "error", "mesaj": f"İhlal: {aksesuar_adi} hiç bulunamadı."})
    return rapor


def analiz_foto(kategori, img):
    model_listesi = modelleri_yukle(kategori)
    islem_img = img.copy()
    tum_tespitler = []  # {"isim", "conf", "box"}

    for sirasi, (model, sinif_isimleri) in enumerate(model_listesi):
        results = model.predict(source=islem_img, conf=GUVEN_ESIGI, iou=UST_USTE_BINME_ESIGI)
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = sinif_isimleri.get(cls, f"ID:{cls}")
            if _gastronomi_filtre(kategori, sirasi, label) or _ofis_filtre(kategori, sirasi, label):
                continue
            tum_tespitler.append({"isim": label, "conf": conf, "box": (x1, y1, x2, y2)})

    # Kişileri ayır (büyük/küçük harf fark etmez)
    kisiler = [t for t in tum_tespitler if t["isim"].lower() == "person"]
    kisi_kutulari = [t["box"] for t in kisiler]
    diger = [t for t in tum_tespitler if t["isim"].lower() != "person"]

    # Kişi bounding box'larını çiz (gri, Person-N etiketi)
    for i, (x1, y1, x2, y2) in enumerate(kisi_kutulari):
        lbl = f"Person-{i + 1}"
        cv2.rectangle(islem_img, (x1, y1), (x2, y2), (180, 180, 180), 1)
        cv2.putText(islem_img, lbl, (x1, y1 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(islem_img, lbl, (x1, y1 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (230, 230, 230), 1, cv2.LINE_AA)

    # Aksesuar / ihlal kutularını çiz (renk + %conf)
    for t in diger:
        x1, y1, x2, y2 = t["box"]
        color = _ihlal_rengi(t["isim"])
        gosterim = f"{t['isim']} %{t['conf'] * 100:.0f}"
        cv2.rectangle(islem_img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(islem_img, gosterim, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.putText(islem_img, gosterim, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1, cv2.LINE_AA)

    kurallar = st.session_state.secilen_kurallar[kategori]
    rapor = _kisi_bazli_rapor(kategori, kurallar, kisi_kutulari, diger)
    return islem_img, rapor


def analiz_video(kategori, video_bytes):
    model_listesi = modelleri_yukle(kategori)
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_bytes)
    cap = cv2.VideoCapture(tfile.name)
    video_ekrani = st.empty()
    video_rapor = {}   # {label: max_conf}
    son_kare = None
    son_kare_tespitler = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        kare_tespitler = []
        for sirasi, (model, sinif_isimleri) in enumerate(model_listesi):
            results = model.predict(source=frame, conf=GUVEN_ESIGI, iou=UST_USTE_BINME_ESIGI, verbose=False)
            for box in results[0].boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label_isim = sinif_isimleri.get(cls, f"ID:{cls}")
                if _gastronomi_filtre(kategori, sirasi, label_isim) or _ofis_filtre(kategori, sirasi, label_isim):
                    continue
                kare_tespitler.append({"isim": label_isim, "conf": conf, "box": (x1, y1, x2, y2)})
                if label_isim not in video_rapor or conf > video_rapor[label_isim]:
                    video_rapor[label_isim] = conf
                color = _ihlal_rengi(label_isim)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        son_kare = frame.copy()
        son_kare_tespitler = kare_tespitler
        video_ekrani.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB", use_container_width=True)
    cap.release()

    # Son karedeki kişileri bul → Person-N etiketlerini son kareye çiz
    kisiler_son = [t for t in son_kare_tespitler if t["isim"].lower() == "person"]
    kisi_kutulari = [t["box"] for t in kisiler_son]
    diger_son = [t for t in son_kare_tespitler if t["isim"].lower() != "person"]

    # Video genelinde görülüp son karede olmayan tespitleri ekle (box=None)
    son_kare_labellar = {t["isim"] for t in son_kare_tespitler}
    for lbl, conf in video_rapor.items():
        if lbl not in son_kare_labellar and lbl.lower() != "person":
            diger_son.append({"isim": lbl, "conf": conf, "box": None})

    if son_kare is not None:
        for i, (x1, y1, x2, y2) in enumerate(kisi_kutulari):
            lbl = f"Person-{i + 1}"
            cv2.rectangle(son_kare, (x1, y1), (x2, y2), (180, 180, 180), 1)
            cv2.putText(son_kare, lbl, (x1, y1 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(son_kare, lbl, (x1, y1 - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (230, 230, 230), 1, cv2.LINE_AA)

    kurallar = st.session_state.secilen_kurallar[kategori]
    rapor = _kisi_bazli_rapor(kategori, kurallar, kisi_kutulari, diger_son)
    return son_kare, rapor


# ==========================================
# 📂 SAYFA 1: SEKTÖR SEÇİMİ
# ==========================================
if st.session_state.sayfa == "secim":
    render_navbar()
    render_landing()
    row1 = st.columns(2, gap="large")
    row2 = st.columns(2, gap="large")
    cols = [row1[0], row1[1], row2[0], row2[1]]
    for idx, (col, sektor) in enumerate(zip(cols, SEKTORLER)):
        with col:
            render_sector_button(sektor, idx, _sektor_sec)

# ==========================================
# 📂 SAYFA 2: ÇALIŞMA ALANI
# ==========================================
elif st.session_state.sayfa == "calisma":
    kategori = st.session_state.kategori
    render_navbar(kategori)
    handle_back_navigation(_medyayi_sifirla)
    render_step_indicator()

    col_onizleme, col_panel = st.columns([1.2, 0.8], gap="medium")

    # --- SOL: ÖNİZLEME + RAPOR ---
    with col_onizleme:
        with st.container(border=True):
            render_panel_title("Önizleme")

            if st.session_state.analiz_gorsel is not None:
                st.image(
                    cv2.cvtColor(st.session_state.analiz_gorsel, cv2.COLOR_BGR2RGB),
                    caption="Yapay Zeka Analizi — Son Kare",
                    use_container_width=True,
                )
                if st.session_state.medya_turu == "video" and st.session_state.medya_bytes:
                    with st.expander("🎬 Orijinal Videoyu İzle"):
                        st.video(st.session_state.medya_bytes)
            elif st.session_state.medya_bytes is not None:
                if st.session_state.medya_turu == "foto":
                    file_bytes = np.asarray(bytearray(st.session_state.medya_bytes), dtype=np.uint8)
                    img = cv2.imdecode(file_bytes, 1)
                    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Yüklenen Medya", use_container_width=True)
                else:
                    st.video(st.session_state.medya_bytes)
            else:
                render_upload_hint()
                yuklenen = st.file_uploader(
                    "Medya yükle",
                    type=["jpg", "jpeg", "png", "mp4", "avi", "mov"],
                    key=f"medya_uploader_{st.session_state.uploader_key}",
                    label_visibility="collapsed",
                )
                if yuklenen is not None:
                    st.session_state.medya_bytes = yuklenen.getvalue()
                    st.session_state.medya_adi = yuklenen.name
                    st.session_state.medya_turu = _medya_turu_belirle(yuklenen.name)
                    st.session_state.analiz_gorsel = None
                    st.session_state.rapor_satirlari = []
                    st.rerun()

            if st.session_state.medya_bytes is not None and st.session_state.analiz_gorsel is None:
                if not st.session_state.secilen_kurallar[kategori]:
                    st.info("Analiz için önce sağ panelden taranacak aksesuarları işaretleyin.")
                col_analiz, col_degistir = st.columns([5, 1])
                with col_analiz:
                    st.markdown('<span class="isg-analiz-marker"></span>', unsafe_allow_html=True)
                    if st.button(
                        "Analiz Et",
                        disabled=not bool(st.session_state.secilen_kurallar[kategori]),
                        use_container_width=True,
                        type="primary",
                        key="analiz_et",
                    ):
                        try:
                            with st.spinner("Yapay zeka analiz ediyor..."):
                                if st.session_state.medya_turu == "foto":
                                    file_bytes = np.asarray(bytearray(st.session_state.medya_bytes), dtype=np.uint8)
                                    img = cv2.imdecode(file_bytes, 1)
                                    sonuc_img, rapor = analiz_foto(kategori, img)
                                    st.session_state.analiz_gorsel = sonuc_img
                                else:
                                    son_kare, rapor = analiz_video(kategori, st.session_state.medya_bytes)
                                    st.session_state.analiz_gorsel = son_kare
                                st.session_state.rapor_satirlari = rapor
                                st.toast("Analiz tamamlandı.")
                                st.rerun()
                        except Exception as e:
                            st.error(f"HATA: {e}")
                with col_degistir:
                    st.markdown('<span class="isg-degistir-marker"></span>', unsafe_allow_html=True)
                    st.button("Değiştir", key="degistir", use_container_width=True, type="secondary", on_click=_medyayi_sifirla)

        render_report_block(on_yeni_analiz=_medyayi_sifirla)

    # --- SAĞ: KURALLAR ---
    with col_panel:
        with st.container(border=True):
            render_panel_title("Taranacak Aksesuarlar")
            render_kural_paneli(kategori)
