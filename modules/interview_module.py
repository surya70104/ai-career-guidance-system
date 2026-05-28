import streamlit as st
from modules.theory_test import theory_test
from modules.coding_test import coding_test

def interview_module():

    st.title("Interview Preparation")

    option = st.radio(
        "Choose Test Type",
        ["Theory Test", "Coding Test"]
    )

    if option == "Theory Test":
        theory_test()

    else:
        coding_test()