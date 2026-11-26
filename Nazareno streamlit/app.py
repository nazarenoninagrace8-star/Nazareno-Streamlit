# ==========================================
# PROFILE IMAGE
# ==========================================

def load_image():
    base = Path(__file__).parent

    for filename in ["profile.jpg", "profile.jpeg", "profile.png"]:
        path = base / filename

        if path.exists():
            return path

    return None


# ==========================================
# PROFILE HEADER
# ==========================================

img = load_image()

if img:
    extension = img.suffix.lower()

    if extension == ".png":
        mime_type = "image/png"
    else:
        mime_type = "image/jpeg"

    encoded_image = base64.b64encode(
        img.read_bytes()
    ).decode()

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
            <span class="pill">{PROFILE["age"]} years old</span>
            <span class="pill">{PROFILE["address"]}</span>
            <span class="pill">{PROFILE["interest"]}</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
