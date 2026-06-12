import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
import time
import tempfile # Videoları geçici kaydetmek için gerekli

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Sağlık Denetim Sistemi", page_icon="🏥", layout="centered")

# --- MODELİ YÜKLE ---
@st.cache_resource
def load_model():
    return YOLO('best.pt')

model = load_model()

# --- SINIF SÖZLÜĞÜ ---
sinif_isimleri = {
    0: 'Person', 1: 'Shoe Covers', 2: 'Surgical Cap', 3: 'Surgical Gloves', 
    4: 'Surgical Gown', 5: 'Surgical Mask', 6: 'Surgical Scrubs', 
    7: 'face-shields', 8: 'no-facial-gear', 9: 'no-medical-attire', 
    10: 'no-surgical-cap', 11: 'no-surgical-gloves'
}

# --- WEB ARAYÜZÜ ---
st.title("🏥 Sağlık Personeli Denetim Sistemi")

# Kullanıcıya Fotoğraf mı Video mu yükleyeceğini soralım
medya_turu = st.radio("Ne analiz etmek istiyorsunuz?", ("📸 Fotoğraf", "🎥 Video"))

# ==========================================
# 📸 FOTOĞRAF ANALİZ BÖLÜMÜ (Eski Kodumuz)
# ==========================================
if medya_turu == "📸 Fotoğraf":
    uploaded_file = st.file_uploader("Bir fotoğraf seçin (JPG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Yüklenen Fotoğraf", use_column_width=True)

        if st.button("🔍 Fotoğrafı Analiz Et"):
            with st.spinner('Yapay zeka tarıyor...'):
                img_array = np.array(image)
                img_cv2 = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

                results = model.predict(source=img_cv2, conf=0.50)
                bulunan_nesneler = []

                for box in results[0].boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    
                    label = sinif_isimleri.get(cls, f"ID:{cls}")
                    bulunan_nesneler.append(f"- **{label}** (Güven: %{conf*100:.0f})")
                    
                    color = (0, 0, 255) if "no-" in label else (0, 255, 0)

                    cv2.rectangle(img_cv2, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(img_cv2, f"{label}", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2, cv2.LINE_AA)
                    cv2.putText(img_cv2, f"{label}", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1, cv2.LINE_AA)

                img_result = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)

            st.success("✅ Analiz Tamamlandı!")
            st.image(img_result, use_column_width=True)
            
            st.markdown("### 📋 Denetim Raporu")
            if len(bulunan_nesneler) > 0:
                # Aynı olanları silip (set kullanarak) listeliyoruz
                for oge in list(set(bulunan_nesneler)):
                    st.write(oge)
            else:
                st.warning("⚠️ Herhangi bir nesne tespit edilemedi.")

# ==========================================
# 🎥 VİDEO ANALİZ BÖLÜMÜ
# ==========================================
elif medya_turu == "🎥 Video":
    uploaded_video = st.file_uploader("Bir video seçin (MP4, AVI)", type=["mp4", "avi", "mov"])

    if uploaded_video is not None:
        st.video(uploaded_video) # Orijinal videoyu göster
        
        if st.button("🔴 Videoyu Analiz Et (Canlı)"):
            
            tfile = tempfile.NamedTemporaryFile(delete=False) 
            tfile.write(uploaded_video.read())
            
            cap = cv2.VideoCapture(tfile.name)
            
            st.markdown("### 📡 Canlı Analiz Ekranı")
            video_ekrani = st.empty() 
            
            # --- VİDEO RAPORU İÇİN HAFIZA (SÖZLÜK) ---
            # Modelin video boyunca gördüğü nesneleri ve ulaştığı en yüksek güven oranını tutacağız
            video_rapor = {}
            
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break 
                
                results = model.predict(source=frame, conf=0.50, verbose=False)
                
                for box in results[0].boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    
                    label_isim = sinif_isimleri.get(cls, f"ID:{cls}")
                    
                    # AKILLI RAPORLAMA: Eşyayı hafızaya kaydet. 
                    # Daha önce gördüyse ve şimdiki güven oranı daha yüksekse, onu güncelle!
                    if label_isim not in video_rapor or conf > video_rapor[label_isim]:
                        video_rapor[label_isim] = conf
                    
                    # Çizim Renkleri ve Etiketleri
                    tam_etiket = f"{label_isim} %{conf*100:.0f}"
                    color = (0, 0, 255) if "no-" in label_isim else (0, 255, 0)

                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, tam_etiket, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2, cv2.LINE_AA)
                    cv2.putText(frame, tam_etiket, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1, cv2.LINE_AA)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                video_ekrani.image(frame, channels="RGB")

            cap.release()
            st.success("✅ Video analizi başarıyla tamamlandı!")
            
            # --- VİDEO BİTİNCE RAPORU EKRANA BAS ---
            st.markdown("### 📋 Video Genel Denetim Raporu")
            st.info("Bu rapor, videonun tamamı taranarak ulaşılan en yüksek kesinlik (güven) oranlarına göre oluşturulmuştur.")
            
            if len(video_rapor) > 0:
                for nesne, max_guven in video_rapor.items():
                    st.write(f"- **{nesne}** (Maksimum Güven: %{max_guven*100:.0f})")
            else:
                st.warning("⚠️ Videoda herhangi bir nesne tespit edilemedi.")