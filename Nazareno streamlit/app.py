
import base64
import random
from pathlib import Path

import streamlit as st

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Niña Grace Nazareno",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PROFILE = {
    "name": "Niña Grace Nazareno",
    "age": 19,
    "address": "P3 Tabon",
    "program": "Bachelor of Science in Mechanical Engineering",
    "interest": "Chess",
    "tagline": "Mechanical Engineering Student",
    "about": (
        "I am a 19-year-old Mechanical Engineering student who enjoys "
        "understanding how things work and solving problems step by step. "
        "Outside of the classroom, I love playing chess."
    ),
    "chess": (
        "Chess teaches patience, planning, and thinking several moves ahead. "
        "These are habits that also shape how I approach engineering problems."
    ),
}

IMAGE_CANDIDATES = ["profile.jpg", "profile.jpeg", "profile.png"]


# ============================================================
# HELPERS
# ============================================================

def load_image_b64():
    base = Path(__file__).parent

    for name in IMAGE_CANDIDATES:
        path = base / name

        if path.exists():
            mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
            data = base64.b64encode(path.read_bytes()).decode()
            return f"data:{mime};base64,{data}"

    return None


def initials(name):
    parts = [p for p in name.split() if p]
    return (parts[0][0] + parts[-1][0]).upper()


# ============================================================
# DESIGN / CSS
# ============================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --bg: #060908;
    --card: #0D1411;
    --card2: #121C17;
    --ink: #E7F3EC;
    --soft: #B9CDC2;
    --muted: #8FA89B;
    --em: #10B981;
    --em-bright: #34D399;
    --em-soft: rgba(16, 185, 129, 0.12);
    --line: #1B2A23;
}

:root {
    color-scheme: dark;
}

html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
    color: var(--ink);
    font-size: 17px;
}

.stApp {
    background:
        radial-gradient(900px 380px at 88% -10%,
        rgba(16, 185, 129, 0.10), transparent 60%),
        var(--bg);
}

#MainMenu, footer, header[data-testid="stHeader"] {
    visibility: hidden;
    height: 0;
}

.block-container {
    padding-top: 1.2rem;
    padding-bottom: 1.5rem;
    max-width: 1000px;
}

div[data-testid="stVerticalBlock"] {
    gap: 0.8rem;
}

/* INPUTS */

label, [data-testid="stWidgetLabel"] p {
    color: var(--ink) !important;
    font-size: 1rem !important;
}

.stTextInput input {
    background: var(--card2) !important;
    color: var(--ink) !important;
    border: 1px solid var(--line) !important;
    font-size: 1rem !important;
}

div[data-baseweb="input"],
div[data-baseweb="base-input"] {
    background: var(--card2) !important;
}

.stButton > button {
    background: transparent;
    color: var(--em-bright);
    border: 1px solid var(--em);
    border-radius: 10px;
    padding: 0.4rem 1.1rem;
    font-weight: 500;
    font-size: 1rem;
    min-height: 0;
}

.stButton > button:hover {
    background: var(--em);
    color: #04120C;
    border-color: var(--em);
}

.stButton > button:focus:not(:active) {
    color: var(--em-bright);
    border-color: var(--em);
}

div[data-testid="stAlert"] {
    background: var(--em-soft);
    color: var(--ink);
    border: 1px solid var(--em);
}

/* TABS */

.stTabs [data-baseweb="tab-list"] {
    gap: 0.4rem;
    border-bottom: 1px solid var(--line);
}

.stTabs button[role="tab"] p {
    font-size: 1.02rem;
    font-weight: 500;
    color: var(--muted);
}

.stTabs button[role="tab"][aria-selected="true"] p {
    color: var(--em-bright);
}

.stTabs [data-baseweb="tab-highlight"] {
    background: var(--em);
}

.stTabs [data-baseweb="tab-border"] {
    background: transparent;
}

/* HERO */

.hero {
    display: flex;
    align-items: center;
    gap: 1.4rem;
    background: linear-gradient(135deg, #0F1A15 0%, #09100D 100%);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 1.2rem 1.6rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
}

.avatar {
    width: 104px;
    height: 104px;
    flex-shrink: 0;
    border-radius: 50%;
    border: 3px solid #09100D;
    box-shadow: 0 0 0 2px var(--em),
                0 0 22px rgba(16, 185, 129, 0.25);
    object-fit: cover;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--em-soft);
    color: var(--em-bright);
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.3rem;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero-eyebrow {
    font-size: 0.8rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--em);
    font-weight: 600;
    margin-bottom: 0.2rem;
}

.hero-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    font-weight: 700;
    line-height: 1.05;
    color: var(--ink);
    margin: 0;
}

.hero-sub {
    color: var(--muted);
    font-weight: 400;
    margin-top: 0.3rem;
    font-size: 1.05rem;
}

.pill-row {
    margin-top: 0.7rem;
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
}

.pill {
    padding: 0.28rem 0.85rem;
    border-radius: 999px;
    font-size: 0.9rem;
    font-weight: 500;
    background: var(--em-soft);
    color: var(--em-bright);
    border: 1px solid rgba(16, 185, 129, 0.3);
}

.pill.alt {
    background: rgba(255, 255, 255, 0.05);
    color: var(--soft);
    border-color: var(--line);
}

/* SECTION CARDS */

.section {
    background: var(--card);
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 1.1rem 1.3rem;
    height: 100%;
}

.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.65rem;
    font-weight: 700;
    margin: 0;
    color: var(--ink);
    line-height: 1.2;
}

.rule {
    width: 34px;
    height: 2px;
    background: var(--em);
    border: 0;
    margin: 0.3rem 0 0.7rem 0;
}

.section p {
    color: var(--soft);
    line-height: 1.65;
    font-weight: 400;
    font-size: 1.03rem;
    margin: 0;
}

.gap {
    height: 0.9rem;
}

.row {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.55rem 0;
    border-bottom: 1px dashed var(--line);
    font-size: 1rem;
}

.row:last-child {
    border-bottom: 0;
    padding-bottom: 0;
}

.row:first-of-type {
    padding-top: 0;
}

.row span:first-child {
    color: var(--muted);
}

.row span:last-child {
    font-weight: 500;
    text-align: right;
    color: var(--ink);
}

.stat-label {
    font-size: 0.75rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 500;
}

.footer-note {
    text-align: center;
    color: var(--muted);
    font-size: 0.8rem;
    letter-spacing: 1.5px;
    margin-top: 0.6rem;
    text-transform: uppercase;
}

/* CHESSBOARD */

.chessboard {
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    width: 100%;
    max-width: 320px;
    aspect-ratio: 1 / 1;
    border: 3px solid var(--em);
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(0,0,0,.5);
}

.square {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    line-height: 1;
}

@media (max-width: 700px) {
    .hero {
        flex-direction: column;
        text-align: center;
        padding: 1.2rem 1rem;
        gap: 0.9rem;
    }

    .hero-name {
        font-size: 2.2rem;
    }

    .pill-row {
        justify-content: center;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# PROFILE HEADER
# ============================================================

img = load_image_b64()

if img:
    avatar_html = f'<img class="avatar" src="{img}" alt="Profile picture">'
else:
    avatar_html = f'<div class="avatar">{initials(PROFILE["name"])}</div>'

st.markdown(
    f"""
<div class="hero">
    {avatar_html}
    <div>
        <div class="hero-eyebrow">My Profile</div>
        <div class="hero-name">{PROFILE["name"]}</div>
        <div class="hero-sub">{PROFILE["tagline"]}</div>

        <div class="pill-row">
            <span class="pill">{PROFILE["age"]} years old</span>
            <span class="pill alt">{PROFILE["address"]}</span>
            <span class="pill">{PROFILE["interest"]}</span>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# ABOUT ME AND PERSONAL DETAILS
# ============================================================

left, right = st.columns([1.15, 1], gap="medium")

with left:
    st.markdown(
        f"""
<div class="section">
    <div class="section-title">About Me</div>
    <hr class="rule">
    <p>{PROFILE["about"]}</p>

    <div class="gap"></div>

    <div class="section-title">Beyond the Classroom</div>
    <hr class="rule">
    <p>{PROFILE["chess"]}</p>
</div>
""",
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        f"""
<div class="section">
    <div class="section-title">Personal Details</div>
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
""",
        unsafe_allow_html=True,
    )


# ============================================================
# CHESS OPENINGS
# ============================================================

OPENINGS = [
    (
        "Italian Game",
        "A classic that develops pieces quickly and fights for the center.",
        "1. e4 e5  2. Nf3 Nc6  3. Bc4",
        [("e2", "e4"), ("e7", "e5"), ("g1", "f3"),
         ("b8", "c6"), ("f1", "c4")],
    ),
    (
        "Ruy Lopez",
        "One of the oldest openings, built on steady, patient pressure.",
        "1. e4 e5  2. Nf3 Nc6  3. Bb5",
        [("e2", "e4"), ("e7", "e5"), ("g1", "f3"),
         ("b8", "c6"), ("f1", "b5")],
    ),
    (
        "Sicilian Defense",
        "A popular reply to 1.e4 that leads to sharp, unbalanced play.",
        "1. e4 c5",
        [("e2", "e4"), ("c7", "c5")],
    ),
    (
        "Queen's Gambit",
        "White offers a pawn in order to gain control of the center.",
        "1. d4 d5  2. c4",
        [("d2", "d4"), ("d7", "d5"), ("c2", "c4")],
    ),
    (
        "London System",
        "A solid setup that is easy to learn and hard to break down.",
        "1. d4 d5  2. Nf3 Nf6  3. Bf4",
        [("d2", "d4"), ("d7", "d5"), ("g1", "f3"),
         ("g8", "f6"), ("c1", "f4")],
    ),
    (
        "Caro-Kann Defense",
        "A sturdy defense known for its reliable pawn structure.",
        "1. e4 c6  2. d4 d5",
        [("e2", "e4"), ("c7", "c6"), ("d2", "d4"),
         ("d7", "d5")],
    ),
]

if "opening_idx" not in st.session_state:
    st.session_state.opening_idx = 0

GLYPHS = {
    "K": "♚",
    "Q": "♛",
    "R": "♜",
    "B": "♝",
    "N": "♞",
    "P": "♟",
}


def start_position():
    pos = {}
    back = ["R", "N", "B", "Q", "K", "B", "N", "R"]

    for i, f in enumerate("abcdefgh"):
        pos[f + "1"] = ("w", back[i])
        pos[f + "2"] = ("w", "P")
        pos[f + "7"] = ("b", "P")
        pos[f + "8"] = ("b", back[i])

    return pos


def chessboard_html(pos):
    squares = ""

    for r in range(8):
        for c in range(8):
            sq = "abcdefgh"[c] + str(8 - r)
            bg = "#CFE9DC" if (r + c) % 2 == 0 else "#14825F"

            piece = ""
            color = ""
            shadow = ""

            if sq in pos:
                side, kind = pos[sq]
                piece = GLYPHS[kind] + "\uFE0E"

                if side == "w":
                    color = "#FFFFFF"
                    shadow = (
                        "text-shadow:0 0 2px #04120C,"
                        "0 0 2px #04120C;"
                    )
                else:
                    color = "#04120C"

            squares += (
                f'<div class="square" style="background:{bg};'
                f'color:{color};{shadow}">{piece}</div>'
            )

    return f'<div class="chessboard">{squares}</div>'


# ============================================================
# EXPLORE MORE - CHESS, GOALS, SAY HELLO
# ============================================================

tab_chess, tab_goals, tab_hello = st.tabs(
    ["Chess Corner", "Goals", "Say Hello"]
)


# ============================================================
# CHESS CORNER
# ============================================================

with tab_chess:

    name, desc, moves_text, moves = OPENINGS[
        st.session_state.opening_idx
    ]

    pos = start_position()

    for src, dst in moves:
        pos[dst] = pos.pop(src)

    c1, c2 = st.columns([1, 1.2], gap="large")

    with c1:
        st.markdown(
            chessboard_html(pos),
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
<div class="section">
    <div class="stat-label">Opening of the moment</div>

    <div class="section-title" style="margin-top:0.2rem">
        {name}
    </div>

    <hr class="rule">

    <p>{desc}</p>

    <div class="stat-label" style="margin-top:0.8rem">
        Moves
    </div>

    <p style="font-weight:500;color:#E7F3EC">
        {moves_text}
    </p>
</div>
""",
            unsafe_allow_html=True,
        )

        if st.button("Show another opening"):
            st.session_state.opening_idx = random.choice(
                [
                    i for i in range(len(OPENINGS))
                    if i != st.session_state.opening_idx
                ]
            )
            st.rerun()


# ============================================================
# GOALS
# ============================================================

with tab_goals:

    st.markdown(
        """
<div class="section">

    <div class="row">
        <span>Academic</span>
        <span>
            Complete my Bachelor of Science in Mechanical Engineering
        </span>
    </div>

    <div class="row">
        <span>Skills</span>
        <span>
            Keep learning and building practical engineering knowledge
        </span>
    </div>

    <div class="row">
        <span>Chess</span>
        <span>
            Keep improving, one game at a time
        </span>
    </div>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# SAY HELLO
# ============================================================

with tab_hello:

    visitor = st.text_input(
        "Leave your name",
        placeholder="Your name here",
    )

    if st.button("Say hello"):
        st.balloons()

        who = visitor.strip() if visitor.strip() else "visitor"

        st.success(
            f"Thank you for visiting, {who}. It is lovely to meet you."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer-note">
    Niña Grace Nazareno &nbsp;|&nbsp; Student Profile
</div>
""",
    unsafe_allow_html=True,
)
