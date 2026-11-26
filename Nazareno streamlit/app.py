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
