import streamlit as st

st.header("Niña Grace Nazareno")


import streamlit as st
from PIL import Image

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Niña Grace | Personal Dashboard",
    page_icon="♟️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PROFILE INFORMATION
# ==========================================
NAME = "Niña Grace Nazareno"
AGE = 19
ADDRESS = "P3 Tabon"
COURSE = "Bachelor of Science in Mechanical Engineering"
HOBBY = "Playing Chess"

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
<style>
.stApp {
    background-color: #f4f6fb;
}

[data-testid="stSidebar"] {
    background-color: #172554;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.main-title {
    color: #172554;
    font-size: 36px;
    font-weight: 800;
}

.subtitle {
    color: #64748b;
    font-size: 16px;
}

.profile-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06);
    margin-bottom: 15px;
}

.info-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #2563eb;
    box-shadow: 0 3px 12px rgba(0,0,0,0.05);
}

.big-number {
    color: #1e3a8a;
    font-size: 28px;
    font-weight: bold;
}

.profile-name {
    color: #172554;
    font-size: 26px;
    font-weight: bold;
}

div.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}

div.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}

hr {
    border-color: #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================
if "profile_image" not in st.session_state:
    st.session_state.profile_image = None

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:

    st.markdown("# ♟️ MY DASHBOARD")
    st.markdown("---")

    st.markdown("### Welcome!")
    st.write("Niña Grace Nazareno")

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Home",
            "👤 My Profile",
            "🎓 Education",
            "♟️ My Interests",
            "ℹ️ About Me"
        ]
    )

    st.markdown("---")
    st.caption("PERSONAL PORTFOLIO")
    st.caption("© 2026 Niña Grace Nazareno")

# ==========================================
# HOME DASHBOARD
# ==========================================
if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">Welcome to My Dashboard!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Your personal space to know more about me.</div>',
        unsafe_allow_html=True
    )

    st.write("")
    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.markdown('<div class="profile-card">', unsafe_allow_html=True)

        if st.session_state.profile_image:
            st.image(
                st.session_state.profile_image,
                width=180
            )
        else:
            st.image(
                "https://placehold.co/300x300/e2e8f0/172554?text=My+Photo",
                width=180
            )

        st.markdown(
            f'<div class="profile-name">{NAME}</div>',
            unsafe_allow_html=True
        )

        st.write("Mechanical Engineering Student")
        st.caption("♟️ Chess Enthusiast")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:

        st.markdown("### 👋 Hello, welcome!")

        st.write(
            f"""
            Hi! I am **{NAME}**, a {AGE}-year-old
            student from **{ADDRESS}**.

            I am currently pursuing a **{COURSE}**.

            Aside from my academic journey, I enjoy
            playing chess, which helps me develop
            my strategic thinking, patience, and
            problem-solving skills.

            Welcome to my personal dashboard!
            """
        )

    st.write("")
    st.markdown("### 📊 Personal Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            '<div class="info-card">'
            '<h4>👤 Age</h4>'
            '<div class="big-number">19 Years Old</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            '<div class="info-card">'
            '<h4>🎓 Education</h4>'
            '<div class="big-number">BSME</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            '<div class="info-card">'
            '<h4>♟️ Favorite Hobby</h4>'
            '<div class="big-number">Chess</div>'
            '</div>',
            unsafe_allow_html=True
        )

# ==========================================
# MY PROFILE
# ==========================================
elif page == "👤 My Profile":

    st.markdown(
        '<div class="main-title">👤 My Profile</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Get to know me and my personal information.</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    left, right = st.columns([1, 2])

    with left:

        st.markdown("### Profile Picture")

        uploaded_image = st.file_uploader(
            "Upload your picture",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_image:
            st.session_state.profile_image = Image.open(
                uploaded_image
            ).copy()

        if st.session_state.profile_image:
            st.image(
                st.session_state.profile_image,
                width=250
            )
        else:
            st.image(
                "https://placehold.co/400x400/e2e8f0/172554?text=Upload+Your+Photo",
                width=250
            )

        st.caption("Upload your own photo to use as your profile picture.")

    with right:

        st.markdown("### Personal Information")

        st.markdown(
            f'<div class="profile-name">{NAME}</div>',
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.write("**🎂 Age:** 19 years old")
        st.write("**📍 Address:** P3 Tabon")
        st.write("**🎓 Course:** Bachelor of Science in Mechanical Engineering")
        st.write("**♟️ Favorite Hobby:** Playing Chess")

        st.markdown("---")

        st.markdown("### About My Personality")

        st.write(
            """
            I am a student who enjoys learning new things
            and developing my skills. I value education,
            patience, creativity, and continuous improvement.

            I also love playing chess because it challenges
            me to think critically and make strategic decisions.
            """
        )

# ==========================================
# EDUCATION
# ==========================================
elif page == "🎓 Education":

    st.markdown(
        '<div class="main-title">🎓 Educational Background</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### My Academic Journey")

    st.markdown(
        '<div class="profile-card">',
        unsafe_allow_html=True
    )

    st.subheader("🏛️ College")

    st.markdown("**Bachelor of Science in Mechanical Engineering**")

    st.write("Currently pursuing my college education.")

    st.info(
        "My goal is to gain knowledge, improve my engineering "
        "skills, and prepare for my future career."
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### My Academic Goals")

    st.write("- Develop technical and engineering skills.")
    st.write("- Improve my problem-solving abilities.")
    st.write("- Learn new technologies.")
    st.write("- Become a successful mechanical engineer.")

# ==========================================
# MY INTERESTS
# ==========================================
elif page == "♟️ My Interests":

    st.markdown(
        '<div class="main-title">♟️ My Hobbies and Interests</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Things I enjoy doing in my free time.</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            "https://images.unsplash.com/photo-1586165368502-1bad197a6461?w=800",
            use_container_width=True
        )

    with col2:

        st.markdown("### ♟️ Playing Chess")

        st.write(
            """
            One of my favorite hobbies is playing chess.

            Chess is more than just a game for me.
            It teaches me to think ahead, analyze situations,
            develop strategies, and make smart decisions.

            It also helps me practice patience,
            concentration, and critical thinking.
            """
        )

        st.success("Favorite Hobby: Chess")

    st.markdown("---")

    st.markdown("### Skills I Develop Through Chess")

    a, b, c = st.columns(3)

    with a:
        st.markdown("### 🧠")
        st.write("Critical Thinking")

    with b:
        st.markdown("### 🎯")
        st.write("Strategic Planning")

    with c:
        st.markdown("### ⏳")
        st.write("Patience")

# ==========================================
# ABOUT ME
# ==========================================
elif page == "ℹ️ About Me":

    st.markdown(
        '<div class="main-title">ℹ️ About Me</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        f"""
        ### Hello! I am {NAME}.

        I am {AGE} years old and currently living in
        {ADDRESS}.

        I am taking up **{COURSE}**.

        I consider myself a person who enjoys learning,
        exploring new ideas, and improving my abilities.

        Outside academics, I love playing chess because
        it allows me to challenge myself and strengthen
        my strategic thinking.

        ### My Personal Goal

        To become a knowledgeable, skilled, and successful
        mechanical engineer while continuously growing
        as an individual.

        ### My Motto

        *"Every move is a decision, and every decision
        is an opportunity to learn and grow."*
        """
    )

    st.markdown("---")

    st.markdown("### Thank you for visiting my dashboard! 💙")

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")

st.markdown(
    "<center style='color:gray;'>"
    "Designed with 💙 using Python and Streamlit"
    "<br>Niña Grace Nazareno © 2026"
    "</center>",
    unsafe_allow_html=True
)
