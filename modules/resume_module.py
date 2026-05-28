import streamlit as st
from resume_checker import extract_resume_text
from ai_engine import ask_ai

def resume_module():

    st.title("AI Resume Checker")

    role = st.text_input("Target Role")

    file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if file:

        text = extract_resume_text(file)

        if st.button("Analyze Resume"):

            prompt = f"""
            Analyze this resume for {role} role.

            Resume:
            {text}

            Give:
            - Matching Skills
            - Missing Skills
            - Resume Score
            - Project Suggestions
            - Experience Suggestions
            - Improvement Tips
            """

            result = ask_ai(prompt)

            st.write(result)