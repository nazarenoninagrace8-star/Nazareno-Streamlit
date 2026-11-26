import base64
import random
from pathlib import Path
from threading import Lock

import streamlit as st

# ---------------------------------------------------------------- CONFIG
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

# Put your photo in the same folder as this file and name it profile.jpg
# (profile.jpeg / profile.png also work).
IMAGE_CANDIDATES = ["profile.jpg", "profile.jpeg", "profile.png"]


# ---------------------------------------------------------------- HELPERS
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


# ---------------------------------------------------------------- STYLE
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

:root { color-scheme: dark; }
html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
    color: var(--ink);
    font-size: 17px;
}
.stApp {
    background:
        radial-gradient(900px 380px at 88% -10%, rgba(16, 185, 129, 0.10), transparent 60%),
        var(--bg);
}

#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
.block-container { padding-top: 1.2rem; padding-bottom: 1.5rem; max-width: 1000px; }
div[data-testid="stVerticalBlock"] { gap: 0.8rem; }

/* Widgets */
label, [data-testid="stWidgetLabel"] p { color: var(--ink) !important; font-size: 1rem !important; }
.stTextInput input {
    background: var(--card2) !important; color: var(--ink) !important;
    border: 1px solid var(--line) !important; font-size: 1rem !important;
}
div[data-baseweb="input"], div[data-baseweb="base-input"] { background: var(--card2) !important; }
.stButton > button {
    background: transparent; color: var(--em-bright);
    border: 1px solid var(--em); border-radius: 10px;
    padding: 0.4rem 1.1rem; font-weight: 500; font-size: 1rem; min-height: 0;
}
.stButton > button:hover { background: var(--em); color: #04120C; border-color: var(--em); }
.stButton > button:focus:not(:active) { color: var(--em-bright); border-color: var(--em); }
.stButton > button p { font-size: 1rem; }
div[data-testid="stAlert"] { background: var(--em-soft); color: var(--ink); border: 1px solid var(--em); }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: 0.4rem; border-bottom: 1px solid var(--line); }
.stTabs button[role="tab"] p { font-size: 1.02rem; font-weight: 500; color: var(--muted); }
.stTabs button[role="tab"][aria-selected="true"] p { color: var(--em-bright); }
.stTabs [data-baseweb="tab-highlight"] { background: var(--em); }
.stTabs [data-baseweb="tab-border"] { background: transparent; }

/* Hero */
.hero {
    display: flex; align-items: center; gap: 1.4rem;
    background: linear-gradient(135deg, #0F1A15 0%, #09100D 100%);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 1.2rem 1.6rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
}
.avatar {
    width: 104px; height: 104px; flex-shrink: 0;
    border-radius: 50%;
    border: 3px solid #09100D;
    box-shadow: 0 0 0 2px var(--em), 0 0 22px rgba(16, 185, 129, 0.25);
    object-fit: cover;
    display: flex; align-items: center; justify-content: center;
    background: var(--em-soft);
    color: var(--em-bright);
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.3rem; font-weight: 700; letter-spacing: 2px;
}
.hero-eyebrow {
    font-size: 0.8rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--em); font-weight: 600; margin-bottom: 0.2rem;
}
.hero-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem; font-weight: 700; line-height: 1.05;
    color: var(--ink); margin: 0;
}
.hero-sub { color: var(--muted); font-weight: 400; margin-top: 0.3rem; font-size: 1.05rem; }
.pill-row { margin-top: 0.7rem; display: flex; gap: 0.5rem; flex-wrap: wrap; }
.pill {
    padding: 0.28rem 0.85rem; border-radius: 999px; font-size: 0.9rem; font-weight: 500;
    background: var(--em-soft); color: var(--em-bright); border: 1px solid rgba(16, 185, 129, 0.3);
}
.pill.alt { background: rgba(255, 255, 255, 0.05); color: var(--soft); border-color: var(--line); }

/* Section cards */
.section {
    background: var(--card); border: 1px solid var(--line); border-radius: 16px;
    padding: 1.1rem 1.3rem; height: 100%;
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.65rem; font-weight: 700; margin: 0; color: var(--ink); line-height: 1.2;
}
.rule { width: 34px; height: 2px; background: var(--em); border: 0; margin: 0.3rem 0 0.7rem 0; }
.section p { color: var(--soft); line-height: 1.65; font-weight: 400; font-size: 1.03rem; margin: 0; }
.gap { height: 0.9rem; }

.stat-label {
    font-size: 0.75rem; letter-spacing: 2px; text-transform: uppercase;
    color: var(--muted); font-weight: 500;
}

.row { display: flex; justify-content: space-between; gap: 1rem;
       padding: 0.55rem 0; border-bottom: 1px dashed var(--line); font-size: 1rem; }
.row:last-child { border-bottom: 0; padding-bottom: 0; }
.row:first-of-type { padding-top: 0; }
.row span:first-child { color: var(--muted); }
.row span:last-child { font-weight: 500; text-align: right; color: var(--ink); }

.footer-note { text-align: center; color: var(--muted); font-size: 0.8rem;
               letter-spacing: 1.5px; margin-top: 0.6rem; text-transform: uppercase; }

/* ---------- Block Blast ---------- */
.scores { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.6rem; }
.score-card {
    background: var(--card); border: 1px solid var(--line); border-top: 2px solid var(--em);
    border-radius: 12px; padding: 0.5rem 0.9rem;
}
.score-value {
    font-family: 'Cormorant Garamond', serif; font-size: 2rem; font-weight: 700;
    line-height: 1.1; color: var(--em-bright);
}
.msg { color: var(--soft); font-size: 1rem; line-height: 1.5; min-height: 3rem; }
.hint { color: var(--muted); font-size: 0.9rem; line-height: 1.5; }

/* board + tray: always keep columns side by side, even on phones */
.st-key-board, .st-key-tray { width: 100%; }
.st-key-board { max-width: 440px; margin: 0 auto; }
.st-key-board [data-testid="stVerticalBlock"], .st-key-board[data-testid="stVerticalBlock"] { gap: 4px !important; }
.st-key-board [data-testid="stHorizontalBlock"],
.st-key-tray [data-testid="stHorizontalBlock"] { flex-wrap: nowrap !important; }
.st-key-board [data-testid="stHorizontalBlock"] { gap: 4px !important; }
.st-key-tray [data-testid="stHorizontalBlock"] { gap: 0.5rem !important; }
.st-key-board [data-testid="stColumn"], .st-key-board [data-testid="column"],
.st-key-tray [data-testid="stColumn"], .st-key-tray [data-testid="column"] {
    min-width: 0 !important; flex: 1 1 0 !important; width: auto !important;
}
.st-key-board .stButton > button {
    width: 100%; aspect-ratio: 1 / 1; height: auto; min-height: 0; padding: 0;
    border-radius: 8px; border: 1px solid var(--line); background: #0E1713;
}
.st-key-board .stButton > button p { font-size: 0; line-height: 0; }
.st-key-board [class*="st-key-cell_"] .stButton > button:hover {
    background: rgba(16, 185, 129, 0.22); border-color: var(--em);
}
.st-key-board [class*="st-key-fill1_"] .stButton > button { background: linear-gradient(145deg, #6EE7B7, #34D399); border-color: #6EE7B7; }
.st-key-board [class*="st-key-fill2_"] .stButton > button { background: linear-gradient(145deg, #34D399, #10B981); border-color: #34D399; }
.st-key-board [class*="st-key-fill3_"] .stButton > button { background: linear-gradient(145deg, #10B981, #059669); border-color: #10B981; }
.st-key-board [class*="st-key-fill4_"] .stButton > button { background: linear-gradient(145deg, #059669, #047857); border-color: #059669; }
.st-key-board [class*="st-key-fill"] .stButton > button:hover { filter: brightness(1.1); }

.piece-box {
    display: flex; align-items: center; justify-content: center;
    min-height: 100px; background: var(--card); border: 1px solid var(--line);
    border-radius: 14px; margin-bottom: 0.4rem;
}
.piece-box.on { border-color: var(--em); box-shadow: 0 0 0 1px var(--em), 0 0 18px rgba(16, 185, 129, 0.18); }
.piece-box.used { opacity: 0.3; }
.pg { display: grid; gap: 3px; }
.pc { width: 16px; height: 16px; border-radius: 4px; display: block; }
.pc.t1 { background: #6EE7B7; }
.pc.t2 { background: #34D399; }
.pc.t3 { background: #10B981; }
.pc.t4 { background: #059669; }
.st-key-tray [class*="st-key-pickon_"] .stButton > button { background: var(--em); color: #04120C; }
.st-key-tray .stButton > button { width: 100%; }

@media (max-width: 700px) {
    .hero { flex-direction: column; text-align: center; padding: 1.2rem 1rem; gap: 0.9rem; }
    .hero-name { font-size: 2.2rem; }
    .pill-row { justify-content: center; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- HERO
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

# ---------------------------------------------------------------- DETAILS
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
<div class="row"><span>Full Name</span><span>{PROFILE["name"]}</span></div>
<div class="row"><span>Age</span><span>{PROFILE["age"]}</span></div>
<div class="row"><span>Address</span><span>{PROFILE["address"]}</span></div>
<div class="row"><span>Course</span><span>{PROFILE["program"]}</span></div>
<div class="row"><span>Interest</span><span>{PROFILE["interest"]}</span></div>
</div>
""",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------- EXPLORE MORE
st.markdown(
    '<div class="section-title">Explore More</div><hr class="rule" style="margin-bottom:0">',
    unsafe_allow_html=True,
)

# ================================================================ BLOCK BLAST
SIZE = 8

SHAPE_ROWS = [
    # lines
    ["#"], ["##"], ["#", "#"], ["###"], ["#", "#", "#"],
    ["####"], ["#", "#", "#", "#"], ["#####"], ["#", "#", "#", "#", "#"],
    # squares
    ["##", "##"], ["###", "###", "###"],
    # small corners
    ["#.", "##"], [".#", "##"], ["##", "#."], ["##", ".#"],
    # big corners
    ["#..", "#..", "###"], ["..#", "..#", "###"], ["###", "#..", "#.."], ["###", "..#", "..#"],
    # T shapes
    ["###", ".#."], [".#.", "###"], ["#.", "##", "#."], [".#", "##", ".#"],
    # S / Z
    ["##.", ".##"], [".##", "##."], ["#.", "##", ".#"], [".#", "##", "#."],
    # L (2x3)
    ["#.", "#.", "##"], [".#", ".#", "##"], ["##", "#.", "#."], ["##", ".#", ".#"],
]


def parse_shape(rows):
    cells = [(r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == "#"]
    min_r = min(r for r, _ in cells)
    min_c = min(c for _, c in cells)
    return tuple((r - min_r, c - min_c) for r, c in cells)


SHAPES = [parse_shape(rows) for rows in SHAPE_ROWS]


@st.cache_resource
def get_leaderboard():
    """Shared by all visitors while the app is running (resets when it restarts)."""
    return {"rows": [], "lock": Lock()}


def can_place(board, cells, r, c):
    for dr, dc in cells:
        rr, cc = r + dr, c + dc
        if not (0 <= rr < SIZE and 0 <= cc < SIZE) or board[rr][cc]:
            return False
    return True


def fits_anywhere(board, cells):
    return any(can_place(board, cells, r, c) for r in range(SIZE) for c in range(SIZE))


def random_piece():
    return (random.choice(SHAPES), random.randint(1, 4))


def new_tray(board):
    tray = []
    for _ in range(40):  # make sure a fresh set always has at least one playable piece
        tray = [random_piece() for _ in range(3)]
        if any(fits_anywhere(board, p[0]) for p in tray):
            break
    return tray


def new_game():
    s = st.session_state
    s.board = [[0] * SIZE for _ in range(SIZE)]
    s.tray = new_tray(s.board)
    s.sel = 0
    s.score = 0
    s.streak = 0
    s.over = False
    s.saved = False
    s.msg = "Pick a piece, then tap the board square where its top-left corner should go."
    s.setdefault("best", 0)


def select_piece(i):
    if st.session_state.tray[i] is not None:
        st.session_state.sel = i


def place(r, c):
    s = st.session_state
    if s.over or s.tray[s.sel] is None:
        return
    cells, tone = s.tray[s.sel]
    if not can_place(s.board, cells, r, c):
        s.msg = "That piece does not fit there. Try another square."
        return

    for dr, dc in cells:
        s.board[r + dr][c + dc] = tone
    gained = len(cells)

    full_rows = [i for i in range(SIZE) if all(s.board[i])]
    full_cols = [j for j in range(SIZE) if all(s.board[i][j] for i in range(SIZE))]
    lines = len(full_rows) + len(full_cols)
    for i in full_rows:
        for j in range(SIZE):
            s.board[i][j] = 0
    for j in full_cols:
        for i in range(SIZE):
            s.board[i][j] = 0

    if lines:
        s.streak += 1
        bonus = 10 * lines * lines * s.streak
        gained += bonus
        s.msg = f"{lines} line{'s' if lines > 1 else ''} cleared!  +{gained}"
        if s.streak > 1:
            s.msg += f"  (combo x{s.streak})"
        if not any(any(row) for row in s.board):
            gained += 100
            s.msg += "  Perfect clear, +100"
    else:
        s.streak = 0
        s.msg = f"+{gained}"
    s.score += gained
    s.best = max(s.best, s.score)

    s.tray[s.sel] = None
    if all(p is None for p in s.tray):
        s.tray = new_tray(s.board)
    left_pieces = [i for i, p in enumerate(s.tray) if p is not None]
    s.sel = left_pieces[0]

    if not any(fits_anywhere(s.board, s.tray[i][0]) for i in left_pieces):
        s.over = True
        s.msg = f"No more moves. Final score: {s.score}"


def save_score():
    s = st.session_state
    name = (s.get("lb_name") or "").strip() or "Guest"
    lb = get_leaderboard()
    with lb["lock"]:
        lb["rows"].append((name[:24], s.score))
        lb["rows"].sort(key=lambda x: -x[1])
        del lb["rows"][10:]
    s.saved = True


def piece_html(cells, tone, selected, used):
    if cells is None:
        return '<div class="piece-box used"><div class="pg"></div></div>'
    h = max(r for r, _ in cells) + 1
    w = max(c for _, c in cells) + 1
    filled = set(cells)
    sq = "".join(
        f'<i class="pc t{tone}"></i>' if (r, c) in filled else '<i class="pc"></i>'
        for r in range(h)
        for c in range(w)
    )
    cls = "piece-box on" if selected else "piece-box"
    return (
        f'<div class="{cls}"><div class="pg" '
        f'style="grid-template-columns:repeat({w},16px)">{sq}</div></div>'
    )


if "board" not in st.session_state:
    new_game()


def render_game():
    s = st.session_state
    st.markdown(
        f"""
<div class="scores">
<div class="score-card"><div class="stat-label">Score</div><div class="score-value">{s.score}</div></div>
<div class="score-card"><div class="stat-label">Best</div><div class="score-value">{s.best}</div></div>
<div class="score-card"><div class="stat-label">Combo</div><div class="score-value">x{s.streak}</div></div>
</div>
""",
        unsafe_allow_html=True,
    )

    g_left, g_right = st.columns([1.1, 1], gap="large")

    with g_left:
        with st.container(key="board"):
            for r in range(SIZE):
                cols = st.columns(SIZE, gap="small")
                for c, col in enumerate(cols):
                    v = s.board[r][c]
                    key = f"fill{v}_{r}_{c}" if v else f"cell_{r}_{c}"
                    col.button(
                        "\u00a0", key=key, on_click=place, args=(r, c),
                        use_container_width=True,
                    )

    with g_right:
        st.markdown(f'<div class="msg">{s.msg}</div>', unsafe_allow_html=True)

        with st.container(key="tray"):
            cols = st.columns(3, gap="small")
            for i, col in enumerate(cols):
                piece = s.tray[i]
                with col:
                    selected = (i == s.sel) and not s.over and piece is not None
                    if piece is None:
                        st.markdown(piece_html(None, 0, False, True), unsafe_allow_html=True)
                        st.button("Used", key=f"used_{i}", disabled=True, use_container_width=True)
                    else:
                        st.markdown(
                            piece_html(piece[0], piece[1], selected, False),
                            unsafe_allow_html=True,
                        )
                        st.button(
                            "Selected" if selected else "Select",
                            key=f"pickon_{i}" if selected else f"pick_{i}",
                            on_click=select_piece, args=(i,),
                            use_container_width=True,
                        )

        if s.over:
            if not s.saved:
                st.text_input("Name for the leaderboard", key="lb_name", placeholder="Your name")
                st.button("Save my score", on_click=save_score)
            else:
                st.success("Score saved to the leaderboard.")
        st.button("New game", key="new_game_btn", on_click=new_game)

        st.markdown(
            '<div class="hint">Fill a whole row or column to clear it. Clearing lines on '
            "back-to-back moves builds a combo. The game ends when no piece fits.</div>",
            unsafe_allow_html=True,
        )

        rows = get_leaderboard()["rows"]
        if rows:
            body = "".join(
                f"<div class='row'><span>{i + 1}. {n}</span><span>{sc}</span></div>"
                for i, (n, sc) in enumerate(rows[:5])
            )
            st.markdown(
                f'<div class="section"><div class="stat-label" style="margin-bottom:0.4rem">'
                f"Top scores</div>{body}</div>",
                unsafe_allow_html=True,
            )


# ================================================================ CHESS
OPENINGS = [
    ("Italian Game",
     "A classic that develops pieces quickly and fights for the center.",
     "1. e4 e5  2. Nf3 Nc6  3. Bc4",
     [("e2", "e4"), ("e7", "e5"), ("g1", "f3"), ("b8", "c6"), ("f1", "c4")]),
    ("Ruy Lopez",
     "One of the oldest openings, built on steady, patient pressure.",
     "1. e4 e5  2. Nf3 Nc6  3. Bb5",
     [("e2", "e4"), ("e7", "e5"), ("g1", "f3"), ("b8", "c6"), ("f1", "b5")]),
    ("Sicilian Defense",
     "A popular reply to 1.e4 that leads to sharp, unbalanced play.",
     "1. e4 c5",
     [("e2", "e4"), ("c7", "c5")]),
    ("Queen's Gambit",
     "White offers a pawn in order to gain control of the center.",
     "1. d4 d5  2. c4",
     [("d2", "d4"), ("d7", "d5"), ("c2", "c4")]),
    ("London System",
     "A solid setup that is easy to learn and hard to break down.",
     "1. d4 d5  2. Nf3 Nf6  3. Bf4",
     [("d2", "d4"), ("d7", "d5"), ("g1", "f3"), ("g8", "f6"), ("c1", "f4")]),
    ("Caro-Kann Defense",
     "A sturdy defense known for its reliable pawn structure.",
     "1. e4 c6  2. d4 d5",
     [("e2", "e4"), ("c7", "c6"), ("d2", "d4"), ("d7", "d5")]),
]
if "opening_idx" not in st.session_state:
    st.session_state.opening_idx = 0

GLYPHS = {"K": "♚", "Q": "♛", "R": "♜", "B": "♝", "N": "♞", "P": "♟"}


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
            piece, color, shadow = "", "", ""
            if sq in pos:
                side, kind = pos[sq]
                piece = GLYPHS[kind] + "\uFE0E"  # plain text glyph, not an emoji
                if side == "w":
                    color = "#FFFFFF"
                    shadow = "text-shadow:0 0 2px #04120C,0 0 2px #04120C;"
                else:
                    color = "#04120C"
            squares += (
                f'<div style="background:{bg};display:flex;align-items:center;'
                f'justify-content:center;font-size:30px;line-height:1;'
                f'color:{color};{shadow}">{piece}</div>'
            )
    return (
        '<div style="display:grid;grid-template-columns:repeat(8,1fr);'
        "width:100%;max-width:320px;aspect-ratio:1/1;border:3px solid #10B981;border-radius:10px;"
        'overflow:hidden;box-shadow:0 8px 24px rgba(0,0,0,.5)">'
        f"{squares}</div>"
    )


# ---------------------------------------------------------------- TABS
tab_game, tab_chess, tab_goals, tab_hello = st.tabs(
    ["Block Blast", "Chess Corner", "Goals", "Say Hello"]
)

with tab_game:
    render_game()

with tab_chess:
    name, desc, moves_text, moves = OPENINGS[st.session_state.opening_idx]
    pos = start_position()
    for src, dst in moves:
        pos[dst] = pos.pop(src)

    c1, c2 = st.columns([1, 1.2], gap="large")
    with c1:
        st.markdown(chessboard_html(pos), unsafe_allow_html=True)
    with c2:
        st.markdown(
            f"""
<div class="section">
<div class="stat-label">Opening of the moment</div>
<div class="section-title" style="margin-top:0.2rem">{name}</div>
<hr class="rule">
<p>{desc}</p>
<div class="stat-label" style="margin-top:0.8rem">Moves</div>
<p style="font-weight:500;color:#E7F3EC">{moves_text}</p>
</div>
""",
            unsafe_allow_html=True,
        )
        if st.button("Show another opening"):
            st.session_state.opening_idx = random.choice(
                [i for i in range(len(OPENINGS)) if i != st.session_state.opening_idx]
            )
            st.rerun()

with tab_goals:
    st.markdown(
        """
<div class="section">
<div class="row"><span>Academic</span><span>Complete my Bachelor of Science in Mechanical Engineering</span></div>
<div class="row"><span>Skills</span><span>Keep learning and building practical engineering knowledge</span></div>
<div class="row"><span>Chess</span><span>Keep improving, one game at a time</span></div>
</div>
""",
        unsafe_allow_html=True,
    )

with tab_hello:
    visitor = st.text_input("Leave your name", placeholder="Your name here")
    if st.button("Say hello"):
        st.balloons()
        who = visitor.strip() if visitor.strip() else "visitor"
        st.success(f"Thank you for visiting, {who}. It is lovely to meet you.")

st.markdown(
    '<div class="footer-note">Niña Grace Nazareno &nbsp;|&nbsp; Student Profile</div>',
    unsafe_allow_html=True,
)
