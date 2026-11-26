import streamlit as st
import textwrap

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Niña Grace Nazareno | Personal Profile",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #101010;
    color: #ffffff;
}

.block-container {
    max-width: 1050px;
    padding: 3rem 2rem;
}

h1, h2, h3 {
    color: #f2a1c2 !important;
}

p {
    color: #dddddd;
}

.welcome {
    color: #f2a1c2;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.main-name {
    font-size: 42px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.3;
    margin-bottom: 10px;
}

.course {
    color: #f2a1c2;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 25px;
}

.description {
    color: #cccccc;
    font-size: 16px;
    line-height: 1.9;
}

.section-title {
    color: #f2a1c2;
    font-size: 23px;
    font-weight: 700;
    margin-bottom: 20px;
    letter-spacing: 1px;
}

.info-card {
    background-color: #1b1b1b;
    border: 1px solid #61364d;
    border-radius: 12px;
    padding: 24px;
    min-height: 115px;
    margin-bottom: 18px;
}

.info-label {
    color: #f2a1c2;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.info-value {
    color: #ffffff;
    font-size: 17px;
    font-weight: 500;
    margin-top: 12px;
    line-height: 1.6;
}

.divider {
    border: none;
    border-top: 1px solid #61364d;
    margin: 35px 0;
}

.footer {
    text-align: center;
    color: #888888;
    font-size: 13px;
    line-height: 2;
    padding: 20px 0;
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
    object-fit: cover;
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
}

@media (max-width: 768px) {
    .main-name {
        font-size: 30px;
    }

    .block-container {
        padding: 2rem 1rem;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="welcome">WELCOME TO MY PERSONAL PROFILE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<hr class="divider">',
    unsafe_allow_html=True
)


# ==========================================
# PROFILE PICTURE UPLOADER
# ==========================================

st.markdown(
    '<div class="section-title">MY PROFILE PICTURE</div>',
    unsafe_allow_html=True
)

uploaded_image = st.file_uploader(
    "Upload or change your profile picture",
    type=["jpg", "jpeg", "png"],
    help="Select a JPG or PNG image from your device."
)


# ==========================================
# MAIN PROFILE SECTION
# ==========================================

profile_col, details_col = st.columns(
    [1, 2],
    gap="large"
)

with profile_col:

    if uploaded_image is not None:
        st.image(
            uploaded_image,
            caption="Niña Grace Nazareno",
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
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #f2a1c2;
    font-size: 15px;
">
    UPLOAD YOUR PROFILE PICTURE
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

    st.markdown("### Hello! Welcome to my personal profile.")

    st.markdown("""
My name is Niña Grace Nazareno, a 19-year-old college
student currently pursuing a Bachelor of Science in
Mechanical Engineering.

I am passionate about learning, gaining new experiences,
and continuously improving myself. Outside my academic
life, I enjoy playing chess, which helps me develop
strategic thinking, patience, and problem-solving skills.
""")


# ==========================================
# PERSONAL INFORMATION
# ==========================================

st.markdown(
    '<hr class="divider">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">PERSONAL INFORMATION</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

with col1:

    st.markdown("""
<div class="info-card">
    <div class="info-label">FULL NAME</div>
    <div class="info-value">Niña Grace Nazareno</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="info-card">
    <div class="info-label">AGE</div>
    <div class="info-value">19 Years Old</div>
</div>
""", unsafe_allow_html=True)


with col2:

    st.markdown("""
<div class="info-card">
    <div class="info-label">ADDRESS</div>
    <div class="info-value">P3 Tabon, Bislig City</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="info-card">
    <div class="info-label">HOBBY</div>
    <div class="info-value">Playing Chess</div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# EDUCATIONAL BACKGROUND
# ==========================================

st.markdown(
    '<hr class="divider">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">EDUCATIONAL BACKGROUND</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">
    <div class="info-label">COURSE</div>
    <div class="info-value">
        Bachelor of Science in Mechanical Engineering
    </div>
    <div style="color:#aaaaaa; margin-top:10px;">
        Second Year College Student
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# ABOUT ME
# ==========================================

st.markdown(
    '<hr class="divider">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">ABOUT ME</div>',
    unsafe_allow_html=True
)

st.markdown("""
I am a dedicated Mechanical Engineering student who
values education, personal growth, and continuous learning.

I enjoy exploring new ideas and challenging myself to
improve my knowledge and abilities. Playing chess is one
of my favorite hobbies because it encourages me to think
critically, plan ahead, and make thoughtful decisions.

My goal is to continue developing my skills, expanding
my knowledge, and preparing for future opportunities
in the field of engineering.
""")


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    '<hr class="divider">',
    unsafe_allow_html=True
)

st.markdown("""
<div class="footer">
    <strong style="color:#f2a1c2;">
        NIÑA GRACE NAZARENO
    </strong>
    <br>
    Personal Profile | 2026
    <br>
    Designed with Streamlit
</div>
""", unsafe_allow_html=True)
