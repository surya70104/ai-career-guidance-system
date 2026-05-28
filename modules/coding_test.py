import streamlit as st
from ai_engine import ask_ai
import plotly.graph_objects as go

def coding_test():

    st.title("AI Coding Test")

    language = st.text_input("Programming Language")

    if "coding_question" not in st.session_state:
        st.session_state.coding_question = ""

    if "coding_score" not in st.session_state:
        st.session_state.coding_score = 0

    if st.button("Generate Coding Question"):

        prompt = f"""
        Generate one coding interview question for {language}.

        Rules:
        - Give only ONE question
        - Beginner to Intermediate level
        - Real coding interview problem
        - Include problem statement clearly
        """

        question = ask_ai(prompt)

        st.session_state.coding_question = question

    if st.session_state.coding_question != "":

        st.subheader("Coding Question")

        st.write(st.session_state.coding_question)

        code = st.text_area(
            "Write Your Code",
            height=250,
            key=st.session_state.coding_question
        )

        if st.button("Analyze Code"):

            prompt = f"""
            Analyze this code.

            Programming Language:
            {language}

            Coding Question:
            {st.session_state.coding_question}

            User Code:
            {code}

            Evaluate:
            - Logic correctness
            - Errors
            - Time complexity
            - Improvements
            - Correct code
            - Score out of 100
            - Skill level
            """

            result = ask_ai(prompt)

            st.write(result)

            score = 50

            if "90" in result:
                score = 90

            elif "80" in result:
                score = 80

            elif "70" in result:
                score = 70

            elif "60" in result:
                score = 60

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                title={'text': "Coding Skill"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "green"},
                }
            ))

            st.plotly_chart(fig)

            if score < 40:
                st.error("Beginner Programmer")

            elif score < 70:
                st.warning("Intermediate Programmer")

            else:
                st.success("Expert Programmer")