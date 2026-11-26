import streamlit as st

# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------
st.set_page_config(
    page_title="Niña Grace Nazareno | Personal Profile",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------
# CUSTOM DESIGN - BLACK AND PINK
# -----------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #101010;
        color: #ffffff;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #f2a1c2 !important;
    }

    .welcome {
        color: #f2a1c2;
        font-size: 14px;
        font-weight: 600;
        letter-spacing: 4px;
        text-transform: uppercase;
    }

    .main-name {
        color: #ffffff;
        font-size: 43px;
        font-weight: 700;
        line-height: 1.2;
    }

    .course {
        color: #f2a1c2;
        font-size: 17px;
        margin-top: 12px;
        margin-bottom: 25px;
    }

    .description {
        color: #cccccc;
        font-size: 16px;
        line-height: 1.9;
    }

    .section-title {
        color: #f2a1c2;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 20px;
    }

    .info-card {
        background-color: #1b1b1b;
        border: 1px solid #61364d;
        border-radius: 12px;
        padding: 23px;
        min-height: 130px;
        margin-bottom: 15px;
    }

    .info-label {
        color: #f2a1c2;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .info-value {
        color: #ffffff;
        font-size: 17px;
        font-weight: 500;
        margin-top: 10px;
    }

    .divider {
        border-top: 1px solid #61364d;
        margin-top: 35px;
        margin-bottom: 35px;
    }

    .footer {
        text-align: center;
        color: #888888;
        font-size: 13px;
        padding-top: 25px;
    }

    [data-testid="stFileUploader"] {
        background-color: #1b1b1b;
        border: 1px solid #61364d;
        border-radius: 12px;
        padding: 15px;
    }

    [data-testid="stFileUploader"] label {
        color: #f2a1c2 !important;
    }

    [data-testid="stImage"] img {
        border: 3px solid #f2a1c2;
        border-radius: 15px;
    }

    .stButton > button {
        background-color: #f2a1c2;
        color: #101010;
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #ffffff;
        color: #101010;
        border: none;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# HEADER
# -----------------------------------------
st.markdown(
    '<p class="welcome">WELCOME TO MY PERSONAL PROFILE</p>',
    unsafe_allow_html=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


# -----------------------------------------
# PROFILE PICTURE UPLOADER
# -----------------------------------------
st.markdown("## My Profile Picture")

uploaded_image = st.file_uploader(
    "Upload or change your profile picture",
    type=["jpg", "jpeg", "png"],
    help="Choose a JPG or PNG image from your device."
)

# -----------------------------------------
# PROFILE DISPLAY
# -----------------------------------------
profile_col, details_col = st.columns(
    [1, 2],
    gap="large"
)

with profile_col:

    if uploaded_image is not None:
        st.image(
            uploaded_image,
            caption="My Profile Picture",
            width="stretch"
        )
    else:
        st.markdown("""
        <div style="
            height: 300px;
            background-color: #1b1b1b;
            border: 2px dashed #f2a1c2;
            border-radius: 15px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: #f2a1c2;
            font-size: 16px;
            padding: 20px;">
            YOUR PROFILE PICTURE<br>
            <span style="font-size:13px;color:#aaaaaa;">
            Upload your photo above
            </span>
        </div>
        """, unsafe_allow_html=True)


with details_col:

    st.markdown(
        '<div class="main-name">Niña Grace Nazareno</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="course">2nd Year Bachelor of Science in Mechanical Engineering</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <p class="description">
        Hello! Welcome to my personal profile.

        My name is Niña Grace Nazareno, a 19-year-old
        college student currently pursuing a Bachelor of
        Science in Mechanical Engineering.

        I am passionate about learning, gaining new
        experiences, and continuously improving myself.
        Outside my academic life, I enjoy playing chess,
        which helps me develop strategic thinking,
        patience, and problem-solving skills.
    </p>
    """, unsafe_allow_html=True)


# -----------------------------------------
# PERSONAL INFORMATION
# -----------------------------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">PERSONAL INFORMATION</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

with col1:

    st.markdown("""
    <div class="info-card">
        <div class="info-label">Full Name</div>
        <div class="info-value">Niña Grace Nazareno</div>
    </div>

    <div class="info-card">
        <div class="info-label">Age</div>
        <div class="info-value">19 Years Old</div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="info-card">
        <div class="info-label">Address</div>
        <div class="info-value">P3 Tabon, Bislig City</div>
    </div>

    <div class="info-card">
        <div class="info-label">Hobby</div>
        <div class="info-value">Playing Chess</div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------
# EDUCATIONAL BACKGROUND
# -----------------------------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">EDUCATIONAL BACKGROUND</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">
    <div class="info-label">Current Education</div>
    <div class="info-value">
        Bachelor of Science in Mechanical Engineering
    </div>
    <div style="color:#aaaaaa; margin-top:8px;">
        Second Year College Student
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------------------
# ABOUT ME
# -----------------------------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">ABOUT ME</div>',
    unsafe_allow_html=True
)

st.markdown("""
<p class="description">
    I am a dedicated Mechanical Engineering student who
    values education, personal growth, and continuous
    learning. I enjoy exploring new ideas and challenging
    myself to improve my knowledge and abilities.

    <br><br>

    Playing chess is one of my favorite hobbies because
    it encourages me to think critically, plan ahead,
    and make thoughtful decisions. I aim to continue
    developing my skills and preparing for future
    opportunities in the engineering field.
</p>
""", unsafe_allow_html=True)


# -----------------------------------------
# FOOTER
# -----------------------------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    NIÑA GRACE NAZARENO
    <br><br>
    Personal Profile | 2026
    <br>
    Designed with Streamlit
</div>
""", unsafe_allow_html=True)
