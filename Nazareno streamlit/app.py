import base64
from pathlib import Path

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
    --bg: #FAF5F2;
    --card: #FFFFFF;
    --ink: #4A3B3F;
    --muted: #8A7A7E;
    --rose: #C98B94;
    --rose-soft: #F3E3E5;
    --sage: #8FA58F;
    --sage-soft: #E6EEE6;
    --line: #EADFDC;
}

html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
    color: var(--ink);
}
.stApp { background: var(--bg); }

#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
.block-container { padding-top: 2.2rem; padding-bottom: 3rem; max-width: 1100px; }

/* Hero */
.hero {
    display: flex; align-items: center; gap: 2.2rem;
    background: linear-gradient(135deg, #FFFFFF 0%, #F8ECEE 100%);
    border: 1px solid var(--line);
    border-radius: 24px;
    padding: 2.2rem 2.6rem;
    box-shadow: 0 8px 30px rgba(201, 139, 148, 0.10);
}
.avatar {
    width: 150px; height: 150px; flex-shrink: 0;
    border-radius: 50%;
    border: 5px solid #FFFFFF;
    box-shadow: 0 0 0 2px var(--rose), 0 10px 24px rgba(201, 139, 148, 0.25);
    object-fit: cover;
    display: flex; align-items: center; justify-content: center;
    background: var(--rose-soft);
    color: var(--rose);
    font-family: 'Cormorant Garamond', serif;
    font-size: 3rem; font-weight: 700; letter-spacing: 2px;
}
.hero-eyebrow {
    font-size: 0.72rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--rose); font-weight: 600; margin-bottom: 0.4rem;
}
.hero-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.9rem; font-weight: 700; line-height: 1.1;
    color: var(--ink); margin: 0;
}
.hero-sub { color: var(--muted); font-weight: 300; margin-top: 0.5rem; font-size: 1.02rem; }
.pill-row { margin-top: 1.1rem; display: flex; gap: 0.6rem; flex-wrap: wrap; }
.pill {
    padding: 0.35rem 0.95rem; border-radius: 999px; font-size: 0.8rem; font-weight: 500;
    background: var(--rose-soft); color: #A8636E;
}
.pill.sage { background: var(--sage-soft); color: #5F7A5F; }

/* Stat cards */
.stat {
    background: var(--card); border: 1px solid var(--line); border-radius: 18px;
    padding: 1.2rem 1.3rem; height: 100%;
    box-shadow: 0 4px 16px rgba(74, 59, 63, 0.04);
    border-top: 3px solid var(--rose);
}
.stat.sage { border-top-color: var(--sage); }
.stat-label {
    font-size: 0.68rem; letter-spacing: 2px; text-transform: uppercase;
    color: var(--muted); font-weight: 500;
}
.stat-value {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.55rem; font-weight: 700; margin-top: 0.25rem; line-height: 1.2;
}

/* Section cards */
.section {
    background: var(--card); border: 1px solid var(--line); border-radius: 18px;
    padding: 1.6rem 1.8rem; height: 100%;
    box-shadow: 0 4px 16px rgba(74, 59, 63, 0.04);
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.5rem; font-weight: 700; margin: 0 0 0.2rem 0;
}
.rule { width: 36px; height: 2px; background: var(--rose); border: 0; margin: 0.4rem 0 1rem 0; }
.section p { color: #6B5D61; line-height: 1.75; font-weight: 300; margin: 0; }

.row { display: flex; justify-content: space-between; gap: 1rem;
       padding: 0.7rem 0; border-bottom: 1px dashed var(--line); font-size: 0.93rem; }
.row:last-child { border-bottom: 0; }
.row span:first-child { color: var(--muted); }
.row span:last-child { font-weight: 500; text-align: right; }

.footer-note { text-align: center; color: var(--muted); font-size: 0.78rem;
               letter-spacing: 1.5px; margin-top: 2.2rem; text-transform: uppercase; }

@media (max-width: 700px) {
    .hero { flex-direction: column; text-align: center; padding: 1.8rem 1.4rem; }
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
<h1 class="hero-name">{PROFILE["name"]}</h1>
<div class="hero-sub">{PROFILE["tagline"]}</div>
<div class="pill-row">
<span class="pill">{PROFILE["age"]} years old</span>
<span class="pill">{PROFILE["address"]}</span>
<span class="pill sage">{PROFILE["interest"]}</span>
</div>
</div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ---------------------------------------------------------------- STAT CARDS
stats = [
    ("Age", f'{PROFILE["age"]} years old', ""),
    ("Location", PROFILE["address"], "sage"),
    ("Program", "BS Mechanical Engineering", ""),
    ("Favorite Pastime", PROFILE["interest"], "sage"),
]
cols = st.columns(4, gap="medium")
for col, (label, value, variant) in zip(cols, stats):
    with col:
        st.markdown(
            f"""
<div class="stat {variant}">
<div class="stat-label">{label}</div>
<div class="stat-value">{value}</div>
</div>
""",
            unsafe_allow_html=True,
        )

st.write("")

# ---------------------------------------------------------------- DETAILS
left, right = st.columns([1.15, 1], gap="medium")

with left:
    st.markdown(
        f"""
<div class="section">
<div class="section-title">About Me</div>
<hr class="rule">
<p>{PROFILE["about"]}</p>
<div style="height:1.4rem"></div>
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

st.markdown(
    '<div class="footer-note">Niña Grace Nazareno &nbsp;|&nbsp; Student Profile</div>',
    unsafe_allow_html=True,
)
