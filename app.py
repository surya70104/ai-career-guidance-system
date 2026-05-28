import streamlit as st

from auth import (
    register_user,
    login_user
)

from profile_manager import (
    update_profile,
    get_profile
)

from modules.career_guidance import career_guidance
from modules.interview_module import interview_module
from modules.resume_module import resume_module
from modules.dashboard import dashboard


# ---------------- AVATARS ----------------

AVATARS = {

    "Professional Male":
    "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",

    "Professional Female":
    "https://cdn-icons-png.flaticon.com/512/6997/6997662.png",

    "Developer":
    "https://cdn-icons-png.flaticon.com/512/921/921347.png",

    "AI Engineer":
    "https://cdn-icons-png.flaticon.com/512/4140/4140048.png",

    "Student":
    "https://cdn-icons-png.flaticon.com/512/2784/2784445.png",

    "Cyber Security":
    "https://cdn-icons-png.flaticon.com/512/3064/3064197.png"
}


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Career Guidance System",
    layout="wide"
)


# ---------------- SESSION ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None


# ---------------- SIDEBAR ----------------

st.sidebar.title("Menu")

menu = st.sidebar.selectbox(
    "Choose",
    ["Login", "Register"]
)


# ---------------- LOGIN / REGISTER ----------------

if not st.session_state.logged_in:

    # ---------------- LOGIN ----------------

    if menu == "Login":

        st.title("Login Form")

        email = st.text_input(
            "Email",
            autocomplete="email"
        )

        password = st.text_input(
            "Password",
            type="password",
            autocomplete="current-password"
        )

        if st.button("Login"):

            user = login_user(
                email,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.user = user

                st.success("Login Successful")

                st.rerun()

            else:

                st.error("Invalid Email or Password")

    # ---------------- REGISTER ----------------

    else:

        st.title("Register Form")

        name = st.text_input("Name")

        email = st.text_input(
            "Email",
            autocomplete="email"
        )

        password = st.text_input(
            "Password",
            type="password",
            autocomplete="new-password"
        )

        if st.button("Register"):

            result = register_user(
                name,
                email,
                password
            )

            if result:

                st.success("Registration Successful")

            else:

                st.error("Email Already Exists")


# ---------------- AFTER LOGIN ----------------

else:

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "Go To",
        [
            "Dashboard",
            "Career Guidance",
            "Interview Preparation",
            "Resume Checker",
            "Profile"
        ]
    )

    # ---------------- LOGOUT ----------------

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user = None

        st.rerun()

    # ---------------- DASHBOARD ----------------

    if page == "Dashboard":

        dashboard()

    # ---------------- CAREER GUIDANCE ----------------

    elif page == "Career Guidance":

        career_guidance()

    # ---------------- INTERVIEW ----------------

    elif page == "Interview Preparation":

        interview_module()

    # ---------------- RESUME ----------------

    elif page == "Resume Checker":

        resume_module()

    # ---------------- PROFILE ----------------

    elif page == "Profile":

        st.title("👤 Professional Profile")

        user = st.session_state.user

        profile = get_profile(user[2])

        if profile:

            phone = profile[0] or ""
            linkedin = profile[1] or ""
            github = profile[2] or ""
            location = profile[3] or ""
            college = profile[4] or ""
            degree = profile[5] or ""
            skills = profile[6] or ""
            objective = profile[7] or ""
            projects = profile[8] or ""
            certifications = profile[9] or ""
            avatar = profile[10] or list(AVATARS.values())[0]

        else:

            phone = ""
            linkedin = ""
            github = ""
            location = ""
            college = ""
            degree = ""
            skills = ""
            objective = ""
            projects = ""
            certifications = ""
            avatar = list(AVATARS.values())[0]

        st.markdown("---")

        col1, col2 = st.columns([1, 2])

        # ---------------- LEFT SIDE ----------------

        with col1:

            st.image(
                avatar,
                width=220
            )

            avatar_name = st.selectbox(
                "Choose Avatar",
                list(AVATARS.keys())
            )

            avatar = AVATARS[avatar_name]

            st.markdown("## Career Status")

            st.success("Active User")

            st.markdown("## Account Type")

            st.info("AI Career User")

        # ---------------- RIGHT SIDE ----------------

        with col2:

            st.subheader("Personal Information")

            st.text_input(
                "Full Name",
                value=user[1],
                disabled=True
            )

            st.text_input(
                "Email Address",
                value=user[2],
                disabled=True
            )

            phone = st.text_input(
                "Phone Number",
                value=phone
            )

            linkedin = st.text_input(
                "LinkedIn URL",
                value=linkedin
            )

            github = st.text_input(
                "GitHub URL",
                value=github
            )

            location = st.text_input(
                "Location",
                value=location
            )

            college = st.text_input(
                "College / University",
                value=college
            )

            degree = st.text_input(
                "Degree",
                value=degree
            )

            st.subheader("Professional Skills")

            skills = st.text_area(
                "Skills",
                value=skills,
                height=120
            )

            st.subheader("Career Objective")

            objective = st.text_area(
                "Career Objective",
                value=objective,
                height=100
            )

            st.subheader("Projects")

            projects = st.text_area(
                "Projects",
                value=projects,
                height=120
            )

            st.subheader("Certifications")

            certifications = st.text_area(
                "Certifications",
                value=certifications,
                height=100
            )

            if st.button(
                "Update Professional Profile"
            ):

                update_profile(
                    user[2],
                    phone,
                    linkedin,
                    github,
                    location,
                    college,
                    degree,
                    skills,
                    objective,
                    projects,
                    certifications,
                    avatar
                )

                st.success(
                    "Profile Updated Successfully"
                )