import streamlit as st
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Niña Grace Nazareno | My Profile",
    page_icon=None,
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>
    .stApp {
        background-color: #101010;
        color: #ffffff;
    }

    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    h1, h2, h3 {
        color: #f5a6c8 !important;
    }

    .welcome {
        font-size: 17px;
        color: #f5a6c8;
        letter-spacing: 3px;
        font-weight: 600;
        text-transform: uppercase;
    }

    .name {
        font-size: 46px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .course {
        font-size: 18px;
        color: #f5a6c8;
        margin-bottom: 25px;
    }

    .description {
        font-size: 16px;
        line-height: 1.8;
        color: #d0d0d0;
    }

    .profile-card {
        background-color: #1b1b1b;
        border: 1px solid #4a2940;
        border-radius: 15px;
        padding: 25px;
        margin-top: 15px;
    }

    .info-label {
        color: #f5a6c8;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .info-value {
        color: #ffffff;
        font-size: 17px;
        margin-bottom: 18px;
    }

    .divider {
        border-top: 1px solid #4a2940;
        margin: 30px 0;
    }

    .footer {
        text-align: center;
        color: #888888;
        font-size: 13px;
        padding-top: 30px;
    }

    [data-testid="stImage"] img {
        border-radius: 18px;
        border: 3px solid #f5a6c8;
    }
</style>
""", unsafe_allow_html=True)


# HEADER
st.markdown(
    '<p class="welcome">WELCOME TO MY PERSONAL PROFILE</p>',
    unsafe_allow_html=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# PROFILE SECTION
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    image_path = Path("profile.jpg")

    if image_path.exists():
        st.image(str(image_path), width="stretch")
    else:
        st.markdown("""
        <div style="
            background-color:#292029;
            border:2px solid #f5a6c8;
            border-radius:18px;
            height:300px;
            display:flex;
            justify-content:center;
            align-items:center;
            color:#f5a6c8;
            font-size:65px;
            font-weight:bold;">
            NGN
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown(
        '<div class="name">Niña Grace Nazareno</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="course">2nd Year | Bachelor of Science in Mechanical Engineering</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <p class="description">
        Hello! Welcome to my personal profile.
        I am Niña Grace Nazareno, a 19-year-old
        Mechanical Engineering student with an interest
        in learning, personal growth, and developing
        new skills.
        <br><br>
        I believe that every experience is an opportunity
        to learn something new. Outside my academic life,
        I enjoy playing chess, which allows me to develop
        my strategic thinking and problem-solving skills.
    </p>
    """, unsafe_allow_html=True)

    st.markdown(
        '<p style="color:#f5a6c8; font-weight:600;">MECHANICAL ENGINEERING STUDENT</p>',
        unsafe_allow_html=True
    )


# PERSONAL INFORMATION
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("## Personal Information")

info1, info2 = st.columns(2, gap="large")

with info1:
    st.markdown("""
    <div class="profile-card">
        <p class="info-label">Full Name</p>
        <p class="info-value">Niña Grace Nazareno</p>

        <p class="info-label">Age</p>
        <p class="info-value">19 Years Old</p>

        <p class="info-label">Location</p>
        <p class="info-value">Bislig City, Philippines</p>
    </div>
    """, unsafe_allow_html=True)

with info2:
    st.markdown("""
    <div class="profile-card">
        <p class="info-label">Course</p>
        <p class="info-value">
            Bachelor of Science in Mechanical Engineering
        </p>

        <p class="info-label">Year Level</p>
        <p class="info-value">2nd Year College</p>

        <p class="info-label">Hobby</p>
        <p class="info-value">Playing Chess</p>
    </div>
    """, unsafe_allow_html=True)


# ABOUT ME
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("## About Me")

st.markdown("""
<p class="description">
    As a Mechanical Engineering student, I am continuously
    exploring new knowledge and experiences that will help
    me grow academically and personally. I value dedication,
    critical thinking, and continuous improvement.
    <br><br>
    My goal is to keep learning, enhance my abilities, and
    prepare myself for future opportunities in the field
    of engineering.
</p>
""", unsafe_allow_html=True)


# FOOTER
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    © 2026 Niña Grace Nazareno | Personal Profile
    <br>
    Designed with Streamlit
</div>
""", unsafe_allow_html=True)
