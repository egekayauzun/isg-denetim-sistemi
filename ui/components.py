import streamlit as st

SEKTOR_AKSESUARLARI = {
    "🏥 Hastane": [
        ("Cerrahi Bone", "Surgical Cap"),
        ("Yüz Siperliği", "face-shields"),
        ("Cerrahi Maske", "Surgical Mask"),
        ("Cerrahi Önlük", "Surgical Gown"),
        ("Hasta Kıyafeti", "Surgical Scrubs"),
        ("Cerrahi Eldiven", "Surgical Gloves"),
        ("Ayakkabı Kılıfı", "Shoe Covers"),
    ],
    "👨‍🍳 Gastronomi": [
        ("Aşçı Şapkası", "chef-hat"),
        ("Mutfak Önlüğü", "apron"),
        ("Mutfak Eldiveni", "gloves"),
    ],
    "🏗️ İnşaat": [
        ("Baret / Kask", "Helmet"),
        ("Güvenlik Yeleği", "Vest"),
        ("İş Eldiveni", "Gloves"),
        ("İş Ayakkabısı", "Shoes"),
    ],
    "🏢 Ofis": [
        ("Takım Elbise", "suit"),
        ("Kravat", "tie"),
        ("Yaka Kartı", "id card"),
    ],
}

SEKTORLER = [
    {
        "id": "🏥 Hastane",
        "emoji": "🏥",
        "baslik": "Hastane",
        "aciklama": "Cerrahi önlük, maske, eldiven ve baş koruması denetimi",
        "renk": "hastane",
        "kkd_sayisi": 7,
        "alt_baslik": "Cerrahi & Tıbbi KKD",
    },
    {
        "id": "👨‍🍳 Gastronomi",
        "emoji": "👨‍🍳",
        "baslik": "Gastronomi",
        "aciklama": "Aşçı şapkası, önlük ve mutfak eldiveni kontrolü",
        "renk": "gastronomi",
        "kkd_sayisi": 3,
        "alt_baslik": "Mutfak Güvenliği",
    },
    {
        "id": "🏗️ İnşaat",
        "emoji": "🏗️",
        "baslik": "İnşaat",
        "aciklama": "Baret, yelek, iş ayakkabısı ve eldiven denetimi",
        "renk": "insaat",
        "kkd_sayisi": 4,
        "alt_baslik": "Şantiye Koruma",
    },
    {
        "id": "🏢 Ofis",
        "emoji": "🏢",
        "baslik": "Ofis",
        "aciklama": "Takım elbise, kravat ve yaka kartı uygunluğu",
        "renk": "ofis",
        "kkd_sayisi": 3,
        "alt_baslik": "Kıyafet Denetimi",
    },
]

_SEKTOR_RENK = {
    "🏥 Hastane": "hastane",
    "👨‍🍳 Gastronomi": "gastronomi",
    "🏗️ İnşaat": "insaat",
    "🏢 Ofis": "ofis",
}


def kategori_baslik(kategori: str) -> str:
    if not kategori:
        return ""
    return kategori.split(" ", 1)[-1]


# ──────────────────────────────────────────────
# NAVBAR
# ──────────────────────────────────────────────
def render_navbar(kategori=None):
    sektor = kategori_baslik(kategori) if kategori else ""
    sektor_html = f' <span class="isg-nav-sektor">/ {sektor}</span>' if sektor else ""
    st.markdown(
        '<div class="isg-navbar-outer">'
        '<div class="isg-navbar-inner">'
        '<div class="isg-nav-left">'
        '<div class="isg-nav-logo">ISG</div>'
        '<div>'
        f'<div class="isg-nav-title">Akıllı İSG Denetim Sistemi{sektor_html}</div>'
        '<div class="isg-nav-sub">Yapay Zeka Destekli KKD Kontrolü</div>'
        '</div></div>'
        '<div class="isg-nav-right">'
        '<div class="isg-nav-status"><span class="isg-nav-status-dot"></span>SİSTEM AKTİF</div>'
        '<div class="isg-nav-brand">ISG-P</div>'
        '</div>'
        '</div></div>',
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# LANDING HERO
# ──────────────────────────────────────────────
def render_landing():
    intro_card = (
        '<div class="isg-intro-outer">'
        '<div class="isg-intro-card">'
        '<div class="isg-intro-title">Nasıl Çalışır?</div>'
        '<div class="isg-intro-steps">'
        '<div class="isg-intro-step">'
        '<div class="isg-intro-num">01</div>'
        '<div class="isg-intro-text">'
        '<strong>Sektör Seçin</strong>'
        '<span>Hastane, mutfak, inşaat veya ofis</span>'
        '</div></div>'
        '<div class="isg-intro-step">'
        '<div class="isg-intro-num">02</div>'
        '<div class="isg-intro-text">'
        '<strong>KKD Belirleyin</strong>'
        '<span>Denetlenecek ekipmanları işaretleyin</span>'
        '</div></div>'
        '<div class="isg-intro-step">'
        '<div class="isg-intro-num">03</div>'
        '<div class="isg-intro-text">'
        '<strong>Görsel Yükleyin</strong>'
        '<span>Fotoğraf veya video yükleme</span>'
        '</div></div>'
        '<div class="isg-intro-step">'
        '<div class="isg-intro-num">04</div>'
        '<div class="isg-intro-text">'
        '<strong>Rapor Alın</strong>'
        '<span>Anlık YZ destekli denetim sonucu</span>'
        '</div></div>'
        '</div></div></div>'
    )
    st.markdown(
        f'<div class="isg-hero">'
        f'<div class="isg-hero-inner">'
        f'<div class="isg-hero-content">'
        f'<div class="isg-hero-eyebrow"><span>🛡️</span> YZ Destekli İSG Denetimi</div>'
        f'<h1>İSG Denetim Platformu</h1>'
        f'<p class="isg-hero-sub">Yapay zeka ile güvenliği izleyin, anında raporlayın.</p>'
        f'<div class="isg-hero-badge-row">'
        f'<div class="isg-hero-badge">🏥 Hastane</div>'
        f'<div class="isg-hero-badge">👨‍🍳 Gastronomi</div>'
        f'<div class="isg-hero-badge">🏗️ İnşaat</div>'
        f'<div class="isg-hero-badge">🏢 Ofis</div>'
        f'</div>'
        f'<div class="isg-hero-stats">'
        f'<div class="isg-stat"><div class="isg-stat-value">4</div><div class="isg-stat-label">Sektör</div></div>'
        f'<div class="isg-stat"><div class="isg-stat-value">17</div><div class="isg-stat-label">KKD Kuralı</div></div>'
        f'<div class="isg-stat"><div class="isg-stat-value">YZ</div><div class="isg-stat-label">Destekli</div></div>'
        f'</div>'
        f'</div>'
        f'{intro_card}'
        f'</div></div>'
        f'<div class="isg-section-header" style="padding-top:1.75rem">'
        f'<div class="isg-section-title">Denetim Sektörünüzü Seçin</div>'
        f'<div class="isg-section-sub">Her sektör için özelleştirilmiş yapay zeka modelleri</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# STEP INDICATOR
# ──────────────────────────────────────────────
def render_step_indicator():
    kategori = st.session_state.get("kategori")
    kurallar = st.session_state.secilen_kurallar.get(kategori, {}) if kategori else {}
    medya = st.session_state.get("medya_bytes")
    rapor = st.session_state.get("rapor_satirlari", [])

    if rapor:
        step = 4
    elif medya and kurallar:
        step = 3
    else:
        step = 2

    def cls(n):
        if n < step:
            return "done"
        if n == step:
            return "active"
        return ""

    def connector_cls(n):
        return "done" if n < step else ""

    def dot_label(n):
        return "✓" if n < step else str(n)

    st.markdown(
        f'<div class="isg-steps">'
        f'<div class="isg-step done">'
        f'<div class="isg-step-dot">✓</div><span>Sektör</span>'
        f'</div>'
        f'<div class="isg-step-connector done"></div>'
        f'<div class="isg-step {cls(2)}">'
        f'<div class="isg-step-dot">{dot_label(2)}</div><span>Kurallar</span>'
        f'</div>'
        f'<div class="isg-step-connector {connector_cls(2)}"></div>'
        f'<div class="isg-step {cls(3)}">'
        f'<div class="isg-step-dot">{dot_label(3)}</div><span>Analiz</span>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# BACK NAVIGATION
# ──────────────────────────────────────────────
def handle_back_navigation(on_reset):
    st.markdown('<span class="isg-nav-spacer"></span>', unsafe_allow_html=True)
    if st.button("← Sektör Seçimine Dön", key="nav_back", type="secondary"):
        st.session_state.sayfa = "secim"
        st.session_state.kategori = None
        on_reset()
        st.rerun()


# ──────────────────────────────────────────────
# SECTOR BUTTON
# ──────────────────────────────────────────────
def render_sector_button(sektor: dict, idx: int, on_click):
    renk = sektor.get("renk", "hastane")
    kkd = sektor.get("kkd_sayisi", "")
    alt = sektor.get("alt_baslik", "")
    st.markdown(
        f'<span class="isg-sector-btn-marker isg-sector-{renk}"></span>',
        unsafe_allow_html=True,
    )
    label = f"{sektor['emoji']}\n{sektor['baslik']} — {alt}\n{sektor['aciklama']}\n✦ {kkd} KKD Kuralı"
    st.button(
        label,
        key=f"sektor_{idx}",
        use_container_width=True,
        type="secondary",
        on_click=on_click,
        args=(sektor["id"],),
    )


# ──────────────────────────────────────────────
# UPLOAD HINT
# ──────────────────────────────────────────────
def render_upload_hint():
    st.markdown(
        '<div class="isg-preview-box isg-upload-zone">'
        '<div class="isg-preview-empty-icon">📸</div>'
        '<div class="isg-preview-empty-title">Medya Yükleyin</div>'
        '<div class="isg-preview-empty-desc">Fotoğraf veya videoyu sürükleyin ya da seçin</div>'
        '<div class="isg-upload-formats">'
        '<span class="isg-upload-fmt-badge">JPG</span>'
        '<span class="isg-upload-fmt-badge">PNG</span>'
        '<span class="isg-upload-fmt-badge">MP4</span>'
        '<span class="isg-upload-fmt-badge">AVI</span>'
        '<span class="isg-upload-fmt-badge">MOV</span>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# PANEL TITLE
# ──────────────────────────────────────────────
def render_panel_title(title: str):
    st.markdown(
        f'<div class="isg-panel-title">{title}</div>',
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# SECTOR BADGE
# ──────────────────────────────────────────────
def render_sector_badge(kategori: str):
    renk = _SEKTOR_RENK.get(kategori, "default")
    baslik = kategori_baslik(kategori)
    emoji = kategori.split(" ")[0] if kategori else ""
    if "İnşaat" in (kategori or ""):
        emoji = "🏗️"
    st.markdown(
        f'<div class="isg-sector-badge isg-badge-{renk}">'
        f'<span style="font-size:1.1rem">{emoji}</span>'
        f'<span>{baslik}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────
# RULE SUMMARY
# ──────────────────────────────────────────────
def render_rule_summary_compact(kurallar: dict):
    if not kurallar:
        st.caption("Henüz aksesuar seçilmedi.")
        return
    for ad in kurallar:
        st.markdown(
            '<div class="isg-rule-item">'
            f'<div class="isg-rule-region">{ad}</div>'
            '</div>',
            unsafe_allow_html=True,
        )


# ──────────────────────────────────────────────
# ACCESSORIES PANEL
# ──────────────────────────────────────────────

def _tumunu_uygula(kategori: str, aksesuarlar: list, sec: bool):
    """on_click callback — widget instantiate edilmeden önce tetiklenir."""
    if sec:
        for _ad, etiket in aksesuarlar:
            st.session_state[f"aks_{kategori}_{etiket}"] = True
        st.session_state.secilen_kurallar[kategori] = {ad: et for ad, et in aksesuarlar}
    else:
        for _ad, etiket in aksesuarlar:
            key = f"aks_{kategori}_{etiket}"
            if key in st.session_state:
                st.session_state[key] = False
        st.session_state.secilen_kurallar[kategori] = {}


def render_kural_paneli(kategori: str):
    render_sector_badge(kategori)
    st.caption("Denetlenmesini istediğiniz KKD ekipmanlarını işaretleyin.")

    aksesuarlar = SEKTOR_AKSESUARLARI.get(kategori, [])
    mevcut = st.session_state.secilen_kurallar.get(kategori, {})
    if mevcut and any(isinstance(v, dict) for v in mevcut.values()):
        mevcut = {}
        st.session_state.secilen_kurallar[kategori] = {}

    if not aksesuarlar:
        st.info("Bu sektör için aksesuar listesi tanımlı değil.")
        return

    yeni_secimler = {}
    col1, col2 = st.columns(2, gap="small")
    for i, (ad, etiket) in enumerate(aksesuarlar):
        hedef = col1 if i % 2 == 0 else col2
        with hedef:
            if st.checkbox(ad, value=ad in mevcut, key=f"aks_{kategori}_{etiket}"):
                yeni_secimler[ad] = etiket

    st.session_state.secilen_kurallar[kategori] = yeni_secimler

    if yeni_secimler:
        st.markdown("**Seçili Aksesuarlar**")
        render_rule_summary_compact(yeni_secimler)

    # "Tümünü Seç / Kaldır" — en altta
    # on_click kullanılır: callback bir sonraki run başlamadan önce çalışır,
    # bu sayede widget state'i henüz instantiate edilmemiş olur → hata olmaz
    tumu_secili = len(yeni_secimler) == len(aksesuarlar)
    btn_label = "☑ Tümünü Kaldır" if tumu_secili else "☐ Tümünü Seç"
    st.markdown('<span class="isg-tumunu-marker"></span>', unsafe_allow_html=True)
    st.button(
        btn_label,
        key=f"tumu_{kategori}",
        use_container_width=True,
        on_click=_tumunu_uygula,
        args=(kategori, aksesuarlar, not tumu_secili),
    )


# ──────────────────────────────────────────────
# REPORT BLOCK
# ──────────────────────────────────────────────
def render_report_block(on_yeni_analiz=None):
    rapor = st.session_state.get("rapor_satirlari", [])
    if not rapor:
        return

    ok_count = sum(1 for r in rapor if r["tip"] == "success")
    err_count = sum(1 for r in rapor if r["tip"] == "error")

    with st.container(border=True):
        st.markdown(
            f'<div class="isg-report-header">'
            f'<div class="isg-report-title">📋 İSG Denetim Raporu</div>'
            f'<div class="isg-report-counts">'
            f'<span class="isg-count-badge isg-count-ok">✓ {ok_count} Uygun</span>'
            f'<span class="isg-count-badge isg-count-err">✗ {err_count} İhlal</span>'
            f'</div></div>',
            unsafe_allow_html=True,
        )
        for satir in rapor:
            tip = satir["tip"]
            mesaj = satir["mesaj"]
            if tip == "success":
                st.markdown(
                    f'<div class="isg-report-item isg-report-ok">'
                    f'<span class="isg-report-icon">✅</span>'
                    f'<span class="isg-report-msg">{mesaj}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            elif tip == "error":
                st.markdown(
                    f'<div class="isg-report-item isg-report-err">'
                    f'<span class="isg-report-icon">🚨</span>'
                    f'<span class="isg-report-msg">{mesaj}</span>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
            elif tip == "bolge":
                st.markdown(f"**{mesaj}**")

        if on_yeni_analiz:
            st.markdown('<span class="isg-yeni-analiz-marker"></span>', unsafe_allow_html=True)
            st.button(
                "Yeni Analiz",
                key="yeni_analiz",
                use_container_width=True,
                type="secondary",
                on_click=on_yeni_analiz,
            )
