
import base64
import random
import textwrap
from pathlib import Path

import streamlit as st


# ==========================================
# FIX HTML INDENTATION BEFORE STREAMLIT RENDERS IT
# ==========================================

_original_markdown = st.markdown

def markdown_html_fix(body, *args, **kwargs):
    """Remove common leading indentation from HTML passed to Streamlit."""
    if isinstance(body, str) and kwargs.get("unsafe_allow_html", False):
        body = textwrap.dedent("\n" + body).strip()
    return _original_markdown(body, *args, **kwargs)

st.markdown = markdown_html_fix

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Niña Grace Nazareno",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# PROFILE INFORMATION
# ==========================================

PROFILE = {
    "name": "Niña Grace Nazareno",
    "age": 19,
    "address": "P3 Tabon",
    "program": "Bachelor of Science in Mechanical Engineering",
    "interest": "Chess",
    "tagline": "Mechanical Engineering Student",

    "about": (
        "I am a 19-year-old Mechanical Engineering student "
        "who enjoys understanding how things work and solving "
        "problems step by step. Outside of the classroom, "
        "I love playing chess."
    ),

    "chess": (
        "Chess teaches patience, planning, and thinking "
        "several moves ahead. These are habits that also "
        "shape how I approach engineering problems."
    ),
}

# ==========================================
# PROFILE IMAGE
# ==========================================

def load_image():
    base = Path(__file__).parent

    for filename in [
        "profile.jpg",
        "profile.jpeg",
        "profile.png"
    ]:
        path = base / filename

        if path.exists():
            return path

    return None


# ==========================================
# BLACK AND WHITE THEME
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;500;600&display=swap');

:root {
    color-scheme: dark;
}

.stApp {
    background: #080808;
    color: #FFFFFF;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1050px;
    padding: 2rem 1.5rem;
}

#MainMenu,
footer,
header {
    visibility: hidden;
}

p, label {
    color: #DDDDDD;
    line-height: 1.8;
}

.hero {
    display: flex;
    align-items: center;
    gap: 25px;
    background: #151515;
    border: 1px solid #333333;
    border-radius: 18px;
    padding: 30px;
    margin-bottom: 25px;
}

.avatar {
    width: 115px;
    height: 115px;
    min-width: 115px;
    border-radius: 50%;
    border: 3px solid white;
    object-fit: cover;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #252525;
    color: white;
    font-size: 35px;
}

.hero-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 42px;
    font-weight: 700;
    line-height: 1.2;
    color: white;
}

.hero-sub {
    color: #AAAAAA;
    font-size: 16px;
    margin-top: 8px;
}

.hero-eyebrow {
    color: #AAAAAA;
    letter-spacing: 3px;
    font-size: 12px;
    margin-bottom: 8px;
}

.pill-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 15px;
}

.pill {
    background: #292929;
    border: 1px solid #555555;
    color: white;
    padding: 6px 14px;
    border-radius: 30px;
    font-size: 13px;
}

.section {
    background: #151515;
    border: 1px solid #333333;
    border-radius: 15px;
    padding: 25px;
    height: 100%;
}

.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 29px;
    font-weight: 700;
    color: white;
}

.rule {
    width: 40px;
    height: 2px;
    background: white;
    border: none;
    margin: 10px 0 18px 0;
}

.section p {
    font-size: 15px;
    line-height: 1.9;
    color: #CCCCCC;
}

.row {
    display: flex;
    justify-content: space-between;
    gap: 15px;
    padding: 12px 0;
    border-bottom: 1px solid #333333;
    line-height: 1.7;
}

.row:last-child {
    border-bottom: none;
}

.row span:first-child {
    color: #999999;
    flex-shrink: 0;
}

.row span:last-child {
    color: white;
    text-align: right;
    overflow-wrap: anywhere;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 15px;
    border-bottom: 1px solid #333333;
}

.stTabs button[role="tab"] p {
    color: #AAAAAA;
    font-size: 15px;
}

.stTabs button[role="tab"][aria-selected="true"] p {
    color: white;
}

.stTabs [data-baseweb="tab-highlight"] {
    background: white;
}

.stButton > button {
    background: #151515;
    color: white;
    border: 1px solid #777777;
    border-radius: 9px;
    padding: 10px 18px;
    min-height: 42px;
}

.stButton > button:hover {
    background: white;
    color: black;
    border-color: white;
}

.stTextInput input {
    background: #202020 !important;
    color: white !important;
    border: 1px solid #555555 !important;
}

div[data-testid="stTextInput"] label {
    color: white !important;
}

.chessboard {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    width: 100%;
    max-width: 360px;
    aspect-ratio: 1 / 1;
    border: 3px solid white;
    border-radius: 8px;
    overflow: hidden;
    margin: auto;
}

.square {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: clamp(18px, 4vw, 32px);
    line-height: 1;
    min-width: 0;
    min-height: 0;
}

.footer-note {
    text-align: center;
    color: #888888;
    font-size: 12px;
    letter-spacing: 2px;
    margin-top: 30px;
    padding: 15px;
}

@media (max-width: 700px) {

    .hero {
        flex-direction: column;
        text-align: center;
    }

    .hero-name {
        font-size: 32px;
    }

    .pill-row {
        justify-content: center;
    }

    .section {
        padding: 18px;
    }

    .row {
        flex-wrap: wrap;
    }

    .row span:last-child {
        text-align: left;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PROFILE HEADER
# ==========================================

img = load_image()

if img:
    mime_type = (
        "image/png"
        if img.suffix.lower() == ".png"
        else "image/jpeg"
    )

    encoded_image = base64.b64encode(
        img.read_bytes()
    ).decode("utf-8")

    image_html = f"""
    <img
        class="avatar"
        src="data:{mime_type};base64,{encoded_image}"
        alt="Profile Picture"
    >
    """
else:
    image_html = """
    <div class="avatar">NN</div>
    """

st.markdown(f"""
<div class="hero">

    {image_html}

    <div>
        <div class="hero-eyebrow">MY PROFILE</div>

        <div class="hero-name">
            {PROFILE["name"]}
        </div>

        <div class="hero-sub">
            {PROFILE["tagline"]}
        </div>

        <div class="pill-row">
            <span class="pill">
                {PROFILE["age"]} years old
            </span>

            <span class="pill">
                {PROFILE["address"]}
            </span>

            <span class="pill">
                {PROFILE["interest"]}
            </span>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)


# ==========================================
# ABOUT ME AND PERSONAL DETAILS
# ==========================================

left, right = st.columns([1.15, 1], gap="medium")

with left:

    st.markdown(f"""
    <div class="section">

        <div class="section-title">
            About Me
        </div>

        <hr class="rule">

        <p>{PROFILE["about"]}</p>

        <br>

        <div class="section-title">
            Beyond the Classroom
        </div>

        <hr class="rule">

        <p>{PROFILE["chess"]}</p>

    </div>
    """, unsafe_allow_html=True)


with right:

    st.markdown(f"""
    <div class="section">

        <div class="section-title">
            Personal Details
        </div>

        <hr class="rule">

        <div class="row">
            <span>Full Name</span>
            <span>{PROFILE["name"]}</span>
        </div>

        <div class="row">
            <span>Age</span>
            <span>{PROFILE["age"]}</span>
        </div>

        <div class="row">
            <span>Address</span>
            <span>{PROFILE["address"]}</span>
        </div>

        <div class="row">
            <span>Course</span>
            <span>{PROFILE["program"]}</span>
        </div>

        <div class="row">
            <span>Interest</span>
            <span>{PROFILE["interest"]}</span>
        </div>

    </div>
    """, unsafe_allow_html=True)


# ==========================================
# CHESS OPENINGS
# ==========================================

OPENINGS = [

    (
        "Italian Game",
        "A classic opening that develops pieces quickly "
        "and fights for control of the center.",
        "1. e4 e5   2. Nf3 Nc6   3. Bc4",
        [
            ("e2", "e4"),
            ("e7", "e5"),
            ("g1", "f3"),
            ("b8", "c6"),
            ("f1", "c4"),
        ],
    ),

    (
        "Ruy Lopez",
        "One of the oldest chess openings, built on "
        "steady and patient pressure.",
        "1. e4 e5   2. Nf3 Nc6   3. Bb5",
        [
            ("e2", "e4"),
            ("e7", "e5"),
            ("g1", "f3"),
            ("b8", "c6"),
            ("f1", "b5"),
        ],
    ),

    (
        "Sicilian Defense",
        "A popular response to 1.e4 that creates "
        "sharp and exciting positions.",
        "1. e4 c5",
        [
            ("e2", "e4"),
            ("c7", "c5"),
        ],
    ),

    (
        "Queen's Gambit",
        "White offers a pawn to gain better control "
        "of the center.",
        "1. d4 d5   2. c4",
        [
            ("d2", "d4"),
            ("d7", "d5"),
            ("c2", "c4"),
        ],
    ),

    (
        "London System",
        "A solid opening setup that is easy to learn "
        "and useful for building strong positions.",
        "1. d4 d5   2. Nf3 Nf6   3. Bf4",
        [
            ("d2", "d4"),
            ("d7", "d5"),
            ("g1", "f3"),
            ("g8", "f6"),
            ("c1", "f4"),
        ],
    ),

    (
        "Caro-Kann Defense",
        "A reliable defense known for its solid "
        "pawn structure.",
        "1. e4 c6   2. d4 d5",
        [
            ("e2", "e4"),
            ("c7", "c6"),
            ("d2", "d4"),
            ("d7", "d5"),
        ],
    ),

]


# ==========================================
# CHESS PIECES
# ==========================================

GLYPHS = {
    "K": "♚",
    "Q": "♛",
    "R": "♜",
    "B": "♝",
    "N": "♞",
    "P": "♟",
}


# ==========================================
# INITIAL CHESS POSITION
# ==========================================

def start_position():

    position = {}

    back_row = [
        "R", "N", "B", "Q",
        "K", "B", "N", "R"
    ]

    for i, file in enumerate("abcdefgh"):

        position[file + "1"] = ("w", back_row[i])
        position[file + "2"] = ("w", "P")

        position[file + "7"] = ("b", "P")
        position[file + "8"] = ("b", back_row[i])

    return position


# ==========================================
# CREATE CHESSBOARD
# ==========================================

def chessboard_html(position):

    squares = ""

    for row in range(8):

        for col in range(8):

            square = "abcdefgh"[col] + str(8 - row)

            if (row + col) % 2 == 0:
                background = "#FFFFFF"
            else:
                background = "#333333"

            piece_html = ""
            piece_color = ""

            if square in position:

                side, kind = position[square]

                piece_html = GLYPHS[kind] + "\uFE0E"

                if side == "w":
                    piece_color = "#111111"
                else:
                    piece_color = "#FFFFFF"

            squares += f"""
            <div class="square"
                 style="
                    background-color: {background};
                    color: {piece_color};
                 ">
                {piece_html}
            </div>
            """

    return f"""
    <div class="chessboard">
        {squares}
    </div>
    """


# ==========================================
# EXPLORE MORE
# ==========================================

st.markdown("""
<div style="margin-top: 35px;">

    <div class="section-title">
        Explore More
    </div>

    <hr class="rule">

</div>
""", unsafe_allow_html=True)


# ==========================================
# NAVIGATION TABS
# ==========================================

tab_chess, tab_goals, tab_hello = st.tabs([
    "Chess Corner",
    "Goals",
    "Say Hello"
])


# ==========================================
# CHESS CORNER
# ==========================================

if "opening_idx" not in st.session_state:
    st.session_state.opening_idx = 0


with tab_chess:

    opening_name, description, moves_text, moves = OPENINGS[
        st.session_state.opening_idx
    ]

    position = start_position()

    for source, destination in moves:
        position[destination] = position.pop(source)

    chess_left, chess_right = st.columns(
        [1, 1.2],
        gap="large"
    )

    with chess_left:

        st.markdown(
            chessboard_html(position),
            unsafe_allow_html=True
        )

    with chess_right:

        st.markdown(f"""
        <div class="section">

            <div class="stat-label">
                OPENING OF THE MOMENT
            </div>

            <div class="section-title">
                {opening_name}
            </div>

            <hr class="rule">

            <p>
                {description}
            </p>

            <br>

            <div class="stat-label">
                CHESS MOVES
            </div>

            <p style="color: white; font-weight: 500;">
                {moves_text}
            </p>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "Show Another Opening",
            key="another_opening",
            use_container_width=True
        ):

            current = st.session_state.opening_idx

            choices = [
                i for i in range(len(OPENINGS))
                if i != current
            ]

            st.session_state.opening_idx = random.choice(choices)

            st.rerun()


# ==========================================
# GOALS
# ==========================================

with tab_goals:

    st.markdown("""
    <div class="section">

        <div class="section-title">
            My Goals
        </div>

        <hr class="rule">

        <div class="row">
            <span>Academic</span>

            <span>
                Complete my Bachelor of Science in
                Mechanical Engineering.
            </span>
        </div>

        <div class="row">
            <span>Skills</span>

            <span>
                Keep learning and building practical
                engineering knowledge.
            </span>
        </div>

        <div class="row">
            <span>Chess</span>

            <span>
                Continue improving my chess skills,
                one game at a time.
            </span>
        </div>

    </div>
    """, unsafe_allow_html=True)


# ==========================================
# SAY HELLO
# ==========================================

with tab_hello:

    st.markdown("""
    <div class="section">

        <div class="section-title">
            Say Hello!
        </div>

        <hr class="rule">

        <p>
            Thank you for visiting my personal profile.
            Feel free to leave your name below!
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    visitor = st.text_input(
        "Leave your name",
        placeholder="Enter your name here",
        key="visitor_name"
    )

    if st.button(
        "Say Hello",
        key="hello_button",
        use_container_width=True
    ):

        name = visitor.strip() or "visitor"

        st.success(
            f"Thank you for visiting, {name}! "
            "It is lovely to meet you."
        )

        st.balloons()


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer-note">

    NIÑA GRACE NAZARENO
    &nbsp; | &nbsp;
    STUDENT PROFILE

</div>
""", unsafe_allow_html=True)
