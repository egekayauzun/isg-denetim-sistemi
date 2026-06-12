import streamlit as st


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        :root {
            --isg-primary: #0F766E;
            --isg-primary-dark: #0B534F;
            --isg-primary-light: #F0FDFA;
            --isg-accent: #14B8A6;
            --isg-bg: #F1F5F9;
            --isg-card: #FFFFFF;
            --isg-text: #0F172A;
            --isg-muted: #64748B;
            --isg-border: #E2E8F0;
            --isg-shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --isg-shadow: 0 4px 16px rgba(0,0,0,0.08);
            --isg-shadow-lg: 0 8px 32px rgba(0,0,0,0.14);
            --isg-radius: 14px;
            --isg-radius-sm: 8px;
            --isg-max: 1680px;
            --color-hastane: #0284C7;
            --color-gastronomi: #EA580C;
            --color-insaat: #D97706;
            --color-ofis: #7C3AED;
            --isg-success: #16A34A;
            --isg-success-bg: #F0FDF4;
            --isg-success-border: #86EFAC;
            --isg-danger: #DC2626;
            --isg-danger-bg: #FEF2F2;
            --isg-danger-border: #FCA5A5;
        }

        /* ─── RESET ─── */
        html, body { margin: 0 !important; padding: 0 !important; }
        html, body, .stApp {
            background: var(--isg-bg) !important;
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
        }

        /* Tüm olası üst boşluk kaynaklarını sıfırla */
        .stApp,
        .stApp > div,
        .stApp > div > div {
            margin-top: 0 !important;
            padding-top: 0 !important;
        }
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > .main,
        [data-testid="stAppViewContainer"] > section {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        [data-testid="stMain"],
        section[data-testid="stMain"],
        [data-testid="stMain"] > div,
        section[data-testid="stMain"] > div {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        [data-testid="stMainBlockContainer"],
        [data-testid="stMainBlockContainer"] > div {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        .main, .main > div, .block-container {
            padding-top: 0 !important;
            margin-top: 0 !important;
        }
        [data-testid="stAppViewContainer"] .main .block-container {
            max-width: var(--isg-max);
            width: 100%;
            padding: 0 1.5rem 2.5rem !important;
            margin: 0 auto;
        }

        /* Header / toolbar / dekorasyon gizle */
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        header[data-testid="stHeader"] {
            display: none !important;
            height: 0 !important;
            min-height: 0 !important;
            max-height: 0 !important;
            padding: 0 !important;
            margin: 0 !important;
            overflow: hidden !important;
        }
        #MainMenu, footer { visibility: hidden; }

        /* ─── NAVBAR ─── */
        .isg-navbar-outer {
            width: 100vw;
            position: relative;
            left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
            margin-top: 0 !important; margin-bottom: 0;
            background: linear-gradient(135deg, #083D39 0%, #0B534F 40%, #0F766E 100%);
            box-shadow: 0 2px 24px rgba(8,61,57,0.45);
        }
        .isg-navbar-inner {
            max-width: var(--isg-max);
            margin: 0 auto;
            padding: 0.9rem 1.5rem;
            display: flex; align-items: center; justify-content: space-between;
        }
        .isg-nav-left { display: flex; align-items: center; gap: 1rem; }
        .isg-nav-logo {
            width: 46px; height: 46px;
            background: rgba(255,255,255,0.12);
            border: 1.5px solid rgba(255,255,255,0.22);
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            font-size: 0.68rem; font-weight: 800; color: white; letter-spacing: 0.06em;
        }
        .isg-nav-title { color: white; font-weight: 700; font-size: 1rem; line-height: 1.3; }
        .isg-nav-sektor { color: rgba(255,255,255,0.65); font-weight: 500; }
        .isg-nav-sub { color: rgba(255,255,255,0.45); font-size: 0.73rem; margin-top: 0.15rem; }
        .isg-nav-right { display: flex; align-items: center; gap: 0.85rem; }
        .isg-nav-status {
            display: flex; align-items: center; gap: 0.45rem;
            background: rgba(22,163,74,0.18);
            border: 1px solid rgba(22,163,74,0.35);
            color: #86EFAC;
            font-size: 0.68rem; font-weight: 700; letter-spacing: 0.07em;
            padding: 0.28rem 0.75rem; border-radius: 20px;
        }
        .isg-nav-status-dot {
            width: 6px; height: 6px;
            background: #4ADE80; border-radius: 50%;
            animation: blink 2s ease infinite;
        }
        @keyframes blink {
            0%, 100% { opacity: 1; } 50% { opacity: 0.3; }
        }
        .isg-nav-brand {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            color: white; font-weight: 800; font-size: 0.95rem;
            letter-spacing: 0.22em;
            padding: 0.4rem 1.1rem; border-radius: 8px;
        }

        /* ─── HERO ─── */
        .isg-hero {
            position: relative;
            background: linear-gradient(135deg, #083D39 0%, #0F766E 45%, #134E4A 100%);
            overflow: hidden;
            padding: 3.5rem 2rem 3.25rem;
            margin-bottom: 2rem;
            width: 100vw; left: 50%; right: 50%;
            margin-left: -50vw; margin-right: -50vw;
        }
        .isg-hero::before {
            content: '';
            position: absolute; inset: 0;
            background:
                radial-gradient(ellipse 55% 70% at 15% 50%, rgba(20,184,166,0.18) 0%, transparent 65%),
                radial-gradient(ellipse 40% 60% at 85% 20%, rgba(255,255,255,0.06) 0%, transparent 55%);
        }
        .isg-hero::after {
            content: '';
            position: absolute; inset: 0;
            background-image: radial-gradient(circle, rgba(255,255,255,0.035) 1px, transparent 1px);
            background-size: 28px 28px;
        }
        .isg-hero-inner {
            position: relative; z-index: 2;
            max-width: var(--isg-max); margin: 0 auto;
            display: flex; align-items: center; justify-content: space-between; gap: 2rem;
        }
        .isg-hero-content { flex: 1; }
        .isg-hero-eyebrow {
            display: inline-flex; align-items: center; gap: 0.5rem;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.18);
            color: #A7F3D0; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em;
            padding: 0.3rem 0.85rem; border-radius: 20px; text-transform: uppercase;
            margin-bottom: 1.1rem;
        }
        .isg-hero h1 {
            font-size: 2.4rem !important; font-weight: 800 !important;
            color: white !important; margin: 0 0 0.85rem !important;
            letter-spacing: -0.035em; line-height: 1.15;
            white-space: nowrap !important;
        }
        .isg-hero-sub {
            color: rgba(255,255,255,0.62); font-size: 0.98rem; line-height: 1.65;
            max-width: 510px; margin-bottom: 1.75rem;
        }
        .isg-hero-badge-row {
            display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.75rem;
        }
        .isg-hero-badge {
            display: flex; align-items: center; gap: 0.35rem;
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.14);
            color: rgba(255,255,255,0.78); font-size: 0.76rem; font-weight: 500;
            padding: 0.28rem 0.7rem; border-radius: 6px;
        }
        .isg-hero-stats { display: flex; gap: 2.25rem; flex-wrap: wrap; }
        .isg-stat { display: flex; flex-direction: column; }
        .isg-stat-value { font-size: 1.8rem; font-weight: 800; color: white; line-height: 1; }
        .isg-stat-label {
            font-size: 0.68rem; color: rgba(255,255,255,0.5);
            text-transform: uppercase; letter-spacing: 0.09em; margin-top: 0.22rem;
        }
        .isg-hero-illustration { flex-shrink: 0; opacity: 0.88; }
        .isg-hero-illustration svg { animation: shield-glow 3.5s ease-in-out infinite; }
        @keyframes shield-glow {
            0%, 100% { filter: drop-shadow(0 0 14px rgba(20,184,166,0.45)); }
            50% { filter: drop-shadow(0 0 28px rgba(20,184,166,0.75)); }
        }

        /* ─── SECTION HEADER ─── */
        .isg-section-header { text-align: center; margin-bottom: 1.5rem; }
        .isg-section-title {
            font-size: 1.3rem; font-weight: 700; color: var(--isg-text);
            letter-spacing: -0.02em; margin-bottom: 0.3rem;
        }
        .isg-section-sub { font-size: 0.88rem; color: var(--isg-muted); }

        /* ─── SECTOR CARDS ─── */
        span.isg-sector-btn-marker + div[data-testid="stButton"] { margin-bottom: 0 !important; }
        span.isg-sector-btn-marker + div[data-testid="stButton"] > button {
            width: 100% !important;
            min-height: 200px !important; height: auto !important;
            background: var(--isg-card) !important;
            color: var(--isg-text) !important;
            border: 1.5px solid var(--isg-border) !important;
            border-top: 4px solid var(--isg-primary) !important;
            border-radius: var(--isg-radius) !important;
            box-shadow: var(--isg-shadow) !important;
            padding: 1.75rem 1.5rem !important;
            font-weight: 500 !important; cursor: pointer !important;
            transition: all 0.22s cubic-bezier(0.4,0,0.2,1) !important;
        }
        span.isg-sector-btn-marker + div[data-testid="stButton"] > button p {
            white-space: pre-line !important; text-align: center !important;
            margin: 0 !important; font-size: 0.88rem !important;
            font-weight: 500 !important; color: var(--isg-text) !important;
            line-height: 1.55 !important;
        }
        span.isg-sector-btn-marker + div[data-testid="stButton"] > button p::first-line {
            font-size: 3rem; font-weight: 400; line-height: 1.35;
        }
        span.isg-sector-btn-marker + div[data-testid="stButton"] > button:hover {
            border-color: var(--isg-primary) !important;
            border-top-color: var(--isg-primary) !important;
            background: #F8FFFE !important;
            box-shadow: 0 12px 40px rgba(15,118,110,0.18) !important;
            transform: translateY(-4px) !important;
        }
        /* Per-sector top border colors */
        span.isg-sector-hastane + div[data-testid="stButton"] > button {
            border-top-color: var(--color-hastane) !important;
        }
        span.isg-sector-hastane + div[data-testid="stButton"] > button:hover {
            border-color: var(--color-hastane) !important;
            border-top-color: var(--color-hastane) !important;
            box-shadow: 0 12px 40px rgba(2,132,199,0.18) !important;
        }
        span.isg-sector-gastronomi + div[data-testid="stButton"] > button {
            border-top-color: var(--color-gastronomi) !important;
        }
        span.isg-sector-gastronomi + div[data-testid="stButton"] > button:hover {
            border-color: var(--color-gastronomi) !important;
            border-top-color: var(--color-gastronomi) !important;
            box-shadow: 0 12px 40px rgba(234,88,12,0.18) !important;
        }
        span.isg-sector-insaat + div[data-testid="stButton"] > button {
            border-top-color: var(--color-insaat) !important;
        }
        span.isg-sector-insaat + div[data-testid="stButton"] > button:hover {
            border-color: var(--color-insaat) !important;
            border-top-color: var(--color-insaat) !important;
            box-shadow: 0 12px 40px rgba(217,119,6,0.18) !important;
        }
        span.isg-sector-ofis + div[data-testid="stButton"] > button {
            border-top-color: var(--color-ofis) !important;
        }
        span.isg-sector-ofis + div[data-testid="stButton"] > button:hover {
            border-color: var(--color-ofis) !important;
            border-top-color: var(--color-ofis) !important;
            box-shadow: 0 12px 40px rgba(124,58,237,0.18) !important;
        }

        /* ─── STEP INDICATOR ─── */
        .isg-steps {
            display: flex; align-items: center; width: fit-content;
            background: white; border: 1px solid var(--isg-border);
            border-radius: 50px; padding: 0.45rem 1.25rem;
            margin-bottom: 1.25rem;
            box-shadow: var(--isg-shadow-sm);
        }
        .isg-step {
            display: flex; align-items: center; gap: 0.45rem;
            padding: 0.25rem 0.6rem;
            font-size: 0.78rem; font-weight: 500; color: var(--isg-muted);
        }
        .isg-step-dot {
            width: 22px; height: 22px; border-radius: 50%;
            border: 2px solid var(--isg-border);
            display: flex; align-items: center; justify-content: center;
            font-size: 0.62rem; font-weight: 700;
            background: white; color: var(--isg-muted); flex-shrink: 0;
        }
        .isg-step.done .isg-step-dot {
            background: var(--isg-primary); border-color: var(--isg-primary); color: white;
        }
        .isg-step.done { color: var(--isg-primary-dark); font-weight: 600; }
        .isg-step.active .isg-step-dot {
            background: white; border-color: var(--isg-primary); color: var(--isg-primary);
            box-shadow: 0 0 0 3px rgba(15,118,110,0.15);
        }
        .isg-step.active { color: var(--isg-primary-dark); font-weight: 700; }
        .isg-step-connector { width: 28px; height: 2px; background: var(--isg-border); flex-shrink: 0; }
        .isg-step-connector.done { background: var(--isg-primary); }

        /* ─── PANELS ─── */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: var(--isg-card) !important;
            border-color: var(--isg-border) !important;
            border-radius: var(--isg-radius) !important;
            padding: 0.75rem 1rem !important;
            box-shadow: var(--isg-shadow) !important;
            margin-bottom: 0.75rem;
        }
        .isg-panel-title {
            font-size: 0.78rem; font-weight: 700; color: var(--isg-text);
            text-transform: uppercase; letter-spacing: 0.08em;
            margin: 0 0 0.75rem; padding-bottom: 0.6rem;
            border-bottom: 2px solid var(--isg-border);
            display: flex; align-items: center; gap: 0.5rem;
        }
        .isg-panel-title::before {
            content: ''; display: inline-block;
            width: 3px; height: 13px;
            background: var(--isg-primary); border-radius: 2px;
        }

        /* ─── UPLOAD ZONE ─── */
        .isg-preview-box {
            background: linear-gradient(145deg, #FAFCFF 0%, #F1F5F9 100%);
            border: 2px dashed #CBD5E1;
            border-radius: var(--isg-radius);
            min-height: 230px;
            display: flex; align-items: center; justify-content: center;
            flex-direction: column; color: var(--isg-muted);
            text-align: center; padding: 2rem;
        }
        .isg-preview-empty-icon { font-size: 3rem; opacity: 0.38; margin-bottom: 0.9rem; }
        .isg-preview-empty-title { font-weight: 600; color: var(--isg-text); font-size: 0.95rem; }
        .isg-preview-empty-desc { font-size: 0.82rem; margin-top: 0.3rem; color: var(--isg-muted); }
        .isg-upload-formats {
            display: flex; gap: 0.4rem; margin-top: 0.85rem;
            flex-wrap: wrap; justify-content: center;
        }
        .isg-upload-fmt-badge {
            background: white; border: 1px solid var(--isg-border);
            color: var(--isg-muted); font-size: 0.65rem; font-weight: 700;
            padding: 0.18rem 0.45rem; border-radius: 4px; letter-spacing: 0.05em;
        }
        div[data-testid="stFileUploader"] section {
            border: 1.5px dashed #94A3B8 !important;
            border-radius: var(--isg-radius-sm) !important;
            background: #FAFBFC !important;
            padding: 1rem !important; min-height: 80px;
            transition: all 0.2s ease !important;
        }
        div[data-testid="stFileUploader"] section:hover {
            border-color: var(--isg-primary) !important;
            background: var(--isg-primary-light) !important;
        }

        /* ─── BUTTONS ─── */
        .stButton > button {
            background: linear-gradient(135deg, var(--isg-primary) 0%, #0D6860 100%) !important;
            color: white !important; border: none !important;
            border-radius: var(--isg-radius-sm) !important;
            font-weight: 600 !important; font-size: 0.88rem !important;
            padding: 0.55rem 1.25rem !important;
            box-shadow: 0 2px 8px rgba(15,118,110,0.28) !important;
            transition: all 0.15s ease !important;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, var(--isg-primary-dark) 0%, #094641 100%) !important;
            box-shadow: 0 4px 18px rgba(15,118,110,0.38) !important;
            transform: translateY(-1px) !important;
        }
        .stButton > button:disabled {
            background: #E2E8F0 !important; color: #94A3B8 !important;
            box-shadow: none !important; transform: none !important;
        }
        .stButton > button[kind="secondary"] {
            background: white !important;
            border: 1.5px solid var(--isg-border) !important;
            color: var(--isg-primary-dark) !important;
            box-shadow: none !important;
        }
        .stButton > button[kind="secondary"]:hover {
            background: var(--isg-primary-light) !important;
            border-color: var(--isg-primary) !important;
            transform: none !important; box-shadow: none !important;
        }
        span.isg-analiz-marker + div[data-testid="stButton"] > button {
            min-height: 50px !important;
            font-size: 0.95rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.02em !important;
        }
        span.isg-degistir-marker + div[data-testid="stButton"] > button,
        span.isg-yeni-analiz-marker + div[data-testid="stButton"] > button {
            min-height: 50px !important;
            font-size: 0.78rem !important;
            padding: 0.4rem 0.5rem !important;
            white-space: nowrap !important;
        }

        /* ─── SECTOR BADGE (working page) ─── */
        .isg-sector-badge {
            display: inline-flex; align-items: center; gap: 0.5rem;
            font-weight: 700; font-size: 0.88rem;
            padding: 0.5rem 1rem; border-radius: 8px;
            margin-bottom: 1rem; border: 1.5px solid;
        }
        .isg-badge-hastane   { background: #EFF6FF; color: #1D4ED8; border-color: #BFDBFE; }
        .isg-badge-gastronomi { background: #FFF7ED; color: #C2410C; border-color: #FED7AA; }
        .isg-badge-insaat    { background: #FFFBEB; color: #B45309; border-color: #FDE68A; }
        .isg-badge-ofis      { background: #F5F3FF; color: #6D28D9; border-color: #DDD6FE; }
        .isg-badge-default   { background: var(--isg-primary-light); color: var(--isg-primary-dark); border-color: #A7F3D0; }

        /* ─── CHECKBOXES (card-style, strictly equal height) ─── */

        /* 1. Dış container → sabit yükseklik + clip */
        [data-testid="stCheckbox"],
        .stCheckbox {
            height: 44px !important;
            min-height: 44px !important;
            max-height: 44px !important;
            overflow: hidden !important;
            margin-bottom: 0.35rem !important;
            display: flex !important;
            align-items: stretch !important;
        }
        /* Streamlit bazen ekstra bir div sarmalayıcı koyar */
        [data-testid="stCheckbox"] > div,
        .stCheckbox > div {
            height: 44px !important;
            min-height: 44px !important;
            max-height: 44px !important;
            overflow: hidden !important;
            display: flex !important;
            align-items: center !important;
            flex: 0 0 44px !important;
        }

        /* 2. Label → kart görünümü + sabit yükseklik */
        [data-testid="stCheckbox"] label,
        .stCheckbox label,
        label[data-baseweb="checkbox"] {
            display: flex !important;
            align-items: center !important;
            height: 44px !important;
            min-height: 44px !important;
            max-height: 44px !important;
            overflow: hidden !important;
            background: white !important;
            border: 1.5px solid var(--isg-border) !important;
            border-radius: var(--isg-radius-sm) !important;
            padding: 0 0.85rem !important;
            cursor: pointer !important;
            transition: border-color 0.15s ease, background 0.15s ease !important;
            width: 100% !important;
            gap: 0.6rem !important;
            box-sizing: border-box !important;
            flex: 1 !important;
        }

        /* 3. Metin span → tek satır, taşarsa kırp */
        [data-testid="stCheckbox"] label span,
        .stCheckbox label span {
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            white-space: nowrap !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
        }

        /* 4. Hover & checked durumları */
        [data-testid="stCheckbox"] label:hover,
        .stCheckbox label:hover {
            border-color: var(--isg-primary) !important;
            background: var(--isg-primary-light) !important;
        }
        [data-testid="stCheckbox"] label:has(input:checked),
        .stCheckbox label:has(input:checked) {
            border-color: var(--isg-primary) !important;
            background: linear-gradient(135deg, #F0FDFA 0%, #CCFBF1 100%) !important;
        }

        /* 5. BaseWeb padding sıfırla */
        [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
        .stCheckbox label[data-baseweb="checkbox"] {
            padding: 0 0.85rem !important;
        }

        /* ─── NAV SPACER ─── */
        span.isg-nav-spacer {
            display: block;
            height: 1rem;
        }

        /* ─── TUMUNU SEÇ BUTTON (bottom of panel, same height as checkboxes) ─── */
        span.isg-tumunu-marker + div[data-testid="stButton"] > button {
            min-height: 44px !important;
            height: 44px !important;
            background: white !important;
            border: 1.5px dashed var(--isg-border) !important;
            border-radius: var(--isg-radius-sm) !important;
            color: var(--isg-primary-dark) !important;
            font-weight: 600 !important; font-size: 0.85rem !important;
            box-shadow: none !important;
            width: 100% !important;
            margin-top: 0.35rem !important;
            background: linear-gradient(135deg, #F8FFFE 0%, #F0FDFA 100%) !important;
        }
        span.isg-tumunu-marker + div[data-testid="stButton"] > button:hover {
            background: var(--isg-primary-light) !important;
            border-color: var(--isg-primary) !important;
            transform: none !important; box-shadow: none !important;
        }

        /* ─── HERO INTRO CARD (slide-in from right) ─── */
        @keyframes slide-in-right {
            from { opacity: 0; transform: translateX(55px); }
            to   { opacity: 1; transform: translateX(0); }
        }
        .isg-intro-outer {
            flex-shrink: 0;
            animation: slide-in-right 0.9s cubic-bezier(0.25,0.46,0.45,0.94) 0.25s both;
        }
        .isg-intro-card {
            background: rgba(255,255,255,0.09);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 16px;
            padding: 1.5rem 1.75rem;
            min-width: 250px; max-width: 300px;
        }
        .isg-intro-title {
            color: rgba(255,255,255,0.88);
            font-weight: 700; font-size: 0.72rem;
            text-transform: uppercase; letter-spacing: 0.12em;
            margin-bottom: 1.1rem; padding-bottom: 0.7rem;
            border-bottom: 1px solid rgba(255,255,255,0.12);
        }
        .isg-intro-steps { display: flex; flex-direction: column; gap: 0.85rem; }
        .isg-intro-step { display: flex; align-items: flex-start; gap: 0.85rem; }
        .isg-intro-num {
            background: rgba(20,184,166,0.18);
            border: 1px solid rgba(20,184,166,0.32);
            color: #5EEAD4;
            font-weight: 800; font-size: 0.66rem; letter-spacing: 0.04em;
            width: 28px; height: 28px; border-radius: 8px;
            display: flex; align-items: center; justify-content: center;
            flex-shrink: 0;
        }
        .isg-intro-text { display: flex; flex-direction: column; gap: 0.1rem; padding-top: 0.15rem; }
        .isg-intro-text strong { color: rgba(255,255,255,0.88); font-size: 0.82rem; font-weight: 600; }
        .isg-intro-text span   { color: rgba(255,255,255,0.48); font-size: 0.73rem; }

        /* ─── REPORT ITEMS ─── */
        .isg-report-header {
            display: flex; align-items: center; justify-content: space-between;
            margin-bottom: 0.85rem; padding-bottom: 0.7rem;
            border-bottom: 1.5px solid var(--isg-border);
        }
        .isg-report-title {
            font-weight: 700; font-size: 0.8rem; color: var(--isg-text);
            text-transform: uppercase; letter-spacing: 0.06em;
        }
        .isg-report-counts { display: flex; gap: 0.45rem; }
        .isg-count-badge {
            font-size: 0.7rem; font-weight: 700; padding: 0.18rem 0.6rem;
            border-radius: 20px; letter-spacing: 0.03em;
        }
        .isg-count-ok   { background: var(--isg-success-bg); color: var(--isg-success); border: 1px solid var(--isg-success-border); }
        .isg-count-err  { background: var(--isg-danger-bg);  color: var(--isg-danger);  border: 1px solid var(--isg-danger-border); }
        .isg-report-item {
            display: flex; align-items: flex-start; gap: 0.7rem;
            padding: 0.7rem 0.9rem;
            border-radius: var(--isg-radius-sm);
            border-left: 4px solid;
            margin-bottom: 0.45rem;
            font-size: 0.84rem; line-height: 1.5;
        }
        .isg-report-ok {
            background: var(--isg-success-bg);
            border-left-color: var(--isg-success);
            color: #166534;
        }
        .isg-report-err {
            background: var(--isg-danger-bg);
            border-left-color: var(--isg-danger);
            color: #991B1B;
        }
        .isg-report-icon { font-size: 1.05rem; flex-shrink: 0; margin-top: 0.05rem; }
        .isg-report-msg { font-weight: 500; }

        /* ─── RULE SUMMARY ITEMS ─── */
        .isg-rule-item {
            display: flex; align-items: center; gap: 0.55rem;
            background: linear-gradient(135deg, #F0FDFA 0%, #FAFFFE 100%);
            border: 1px solid #A7F3D0;
            border-radius: var(--isg-radius-sm);
            padding: 0.48rem 0.85rem;
            margin-bottom: 0.35rem; font-size: 0.82rem;
        }
        .isg-rule-item::before {
            content: '✓'; color: var(--isg-primary);
            font-weight: 800; font-size: 0.78rem; flex-shrink: 0;
        }
        .isg-rule-region { font-weight: 600; color: var(--isg-primary-dark); }

        /* ─── VIDEO PLAYER ─── */
        [data-testid="stVideo"] {
            width: 100% !important;
            display: block !important;
        }
        [data-testid="stVideo"] > div {
            width: 100% !important;
        }
        [data-testid="stVideo"] video {
            width: 100% !important;
            height: auto !important;
            max-height: 520px;
            display: block !important;
            border-radius: var(--isg-radius-sm);
            background: #000;
        }
        /* Expander (orijinal videoyu izle) */
        [data-testid="stExpander"] {
            border: 1px solid var(--isg-border) !important;
            border-radius: var(--isg-radius-sm) !important;
            background: white !important;
            margin-top: 0.6rem !important;
        }
        [data-testid="stExpander"] summary {
            font-size: 0.85rem !important;
            font-weight: 600 !important;
            color: var(--isg-primary-dark) !important;
            padding: 0.55rem 0.85rem !important;
        }

        /* ─── ALERTS ─── */
        [data-testid="stAlert"] { border-radius: var(--isg-radius-sm) !important; font-size: 0.85rem !important; }
        [data-testid="stImage"] img { border-radius: var(--isg-radius-sm); }
        h3, h4, h5 { color: var(--isg-text) !important; }

        /* ─── EQUAL HEIGHT COLUMNS (only sector card buttons, NOT checkboxes) ─── */
        [data-testid="stColumn"] { display: flex !important; flex-direction: column !important; }

        /* flex:1 yalnızca stButton wrapper'larına uygulanır — checkbox wrapper'ları dahil değil */
        [data-testid="stColumn"] [data-testid="stButton"] {
            flex: 1 !important; display: flex !important; flex-direction: column !important;
        }
        [data-testid="stColumn"] [data-testid="stButton"] button {
            width: 100% !important; min-height: 100px !important; height: 100% !important;
            white-space: normal !important; word-break: break-word !important;
            display: flex !important; align-items: center !important;
            justify-content: flex-start !important; text-align: left !important;
            padding: 1.5rem 1.75rem !important; font-size: 0.92rem !important;
            line-height: 1.5 !important; box-sizing: border-box !important; flex: 1 !important;
        }

        /* Checkbox wrapper'ları kolondaki flex büyümesine katılmaz */
        [data-testid="stColumn"] [data-testid="stCheckbox"],
        [data-testid="stColumn"] .stCheckbox {
            flex: 0 0 44px !important;
            align-self: flex-start !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
