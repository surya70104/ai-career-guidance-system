import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        .stApp {
            background: linear-gradient(135deg, #020617 0%, #0f172a 100%);
            color: white;
        }

        section[data-testid="stSidebar"] {
            background: #020617;
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        h1, h2, h3 {
            color: white !important;
            font-weight: 700;
        }

        .hero-card {
            background: rgba(255,255,255,0.04);
            padding: 30px;
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.08);
            backdrop-filter: blur(10px);
            margin-bottom: 25px;
        }

        .feature-card {
            background: rgba(255,255,255,0.03);
            padding: 20px;
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,0.06);
            transition: 0.3s ease;
            height: 180px;
        }

        .feature-card:hover {
            transform: translateY(-5px);
            border: 1px solid #6366f1;
        }

        .ai-response {
            background: rgba(99,102,241,0.12);
            padding: 20px;
            border-radius: 18px;
            border-left: 4px solid #6366f1;
            margin-top: 20px;
        }

        .stButton button {
            background: linear-gradient(90deg,#6366f1,#8b5cf6);
            color: white;
            border-radius: 12px;
            border: none;
            padding: 12px 24px;
            font-weight: 600;
            width: 100%;
        }

        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] {
            background-color: rgba(255,255,255,0.05) !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            color: white !important;
        }

        .footer {
            text-align: center;
            color: #94a3b8;
            padding-top: 40px;
            padding-bottom: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )