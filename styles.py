def load_css():

    css = """
    <style>

    .stApp {
        background: linear-gradient(
            to bottom right,
            #020617,
            #0f172a
        );
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    h1, h2, h3, h4, h5 {
        color: #ffffff;
        font-weight: bold;
    }

    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 10px;
        border: 1px solid #334155;
    }

    .stTextArea textarea {
        background-color: #1e293b;
        color: white;
        border-radius: 10px;
    }

    .stButton > button {
        background: linear-gradient(
            90deg,
            #2563eb,
            #1d4ed8
        );

        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: bold;
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #1d4ed8,
            #2563eb
        );
    }

    </style>
    """

    return css