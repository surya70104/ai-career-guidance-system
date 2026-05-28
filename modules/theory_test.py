import streamlit as st
from ai_engine import ask_ai
import plotly.graph_objects as go
import random

def theory_test():

    st.title("AI Theory Interview Test")

    skill = st.text_input("Enter Skill")

    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "current_question" not in st.session_state:
        st.session_state.current_question = 0

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "feedback" not in st.session_state:
        st.session_state.feedback = ""

    if st.button("Start Test"):

        random_id = random.randint(1, 100000)

        prompt = f"""
        Generate EXACTLY 10 UNIQUE interview questions for {skill}.

        IMPORTANT:
        - Every question must contain COMPLETE sentence.
        - Do NOT give only headings.
        - Do NOT give labels only.
        - Questions must be real interview questions.
        - No repeated concepts.
        - Mix easy, intermediate and expert.

        Example Format:

        Q1: What is polymorphism in Python?

        Q2: Explain decorators with example.

        Q3: Difference between list and tuple?

        Generate in same format only.

        Random Seed:
        {random_id}
        """

        result = ask_ai(prompt)

        lines = result.split("\n")

        question_list = []

        for line in lines:

            line = line.strip()

            if line.startswith("Q"):
                question_list.append(line)

        st.session_state.questions = question_list
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.feedback = ""

    if len(st.session_state.questions) > 0:

        index = st.session_state.current_question

        if index < len(st.session_state.questions):

            question = st.session_state.questions[index]

            st.subheader(f"Question {index+1}")

            st.write(question)

            answer = st.text_area(
                "Your Answer",
                key=f"answer_{index}"
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button("Submit Answer"):

                    evaluation_prompt = f"""
                    Evaluate this answer.

                    Question:
                    {question}

                    User Answer:
                    {answer}

                    Give:
                    1. Score out of 10
                    2. Correct Answer
                    3. Explanation
                    """

                    feedback = ask_ai(evaluation_prompt)

                    st.session_state.feedback = feedback

                    if (
                        "8" in feedback or
                        "9" in feedback or
                        "10" in feedback
                    ):
                        st.session_state.score += 1

                    st.session_state.current_question += 1

                    st.rerun()

            with col2:

                if st.button("Skip Question"):

                    st.session_state.current_question += 1

                    st.rerun()

            if st.session_state.feedback != "":
                st.info(st.session_state.feedback)

        else:

            st.success("Interview Test Completed")

            total = len(st.session_state.questions)

            percentage = int(
                (st.session_state.score / total) * 100
            )

            st.subheader(f"Knowledge Score: {percentage}%")

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=percentage,
                title={'text': "Knowledge Meter"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "green"},
                }
            ))

            st.plotly_chart(fig)

            if percentage < 40:
                st.error("Beginner Level")

            elif percentage < 70:
                st.warning("Intermediate Level")

            else:
                st.success("Expert Level")