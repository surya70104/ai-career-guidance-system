import streamlit as st
from ai_engine import ask_ai

def career_guidance():

    st.title("AI Career Guidance")

    role = st.text_input("Enter Career Role")

    if st.button("Generate Roadmap"):

        prompt = f"""
        Give roadmap and required skills
        for becoming a {role}.

        Include:
        - Required Skills
        - Technologies
        - Projects
        - Certifications
        - Interview Preparation
        """

        result = ask_ai(prompt)

        st.write(result)