import streamlit as st
import random
import time

st.set_page_config(page_title="Slot Maschine", page_icon="🎰", layout="centered")

# --- Styling ---
st.markdown(
    """
    <style>
    .slot-box {
        font-size: 64px;
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        background: #111;
        color: white;
        letter-spacing: 10px;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
    }
    .credit-box {
        font-size: 20px;
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        background: #222;
        color: #00ffcc;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Session State ---
if "credits" not in st.session_state:
    st.session_state.credits = 10

if "result" not in st.session_state:
    st.session_state.result = ["❔", "❔", "❔"]

symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]

st.title("🎰 Mini Slot Maschine")

st.markdown(
    f"<div class='credit-box'>Credits: {st.session_state.credits}</div>",
    unsafe_allow_html=True,
)

slot_display = st.empty()


def animate_spin():
    for _ in range(10):
        temp = [random.choice(symbols) for _ in range(3)]
        slot_display.markdown(
            f"<div class='slot-box'>{' '.join(temp)}</div>",
            unsafe_allow_html=True,
        )
        time.sleep(0.08)


def spin():
    if st.session_state.credits <= 0:
        return

    st.session_state.credits -= 1
    animate_spin()

    result = [random.choice(symbols) for _ in range(3)]
    st.session_state.result = result

    slot_display.markdown(
        f"<div class='slot-box'>{' '.join(result)}</div>",
        unsafe_allow_html=True,
    )

    if result[0] == result[1] == result[2]:
        st.session_state.credits += 5
        st.success("Jackpot! +5 Credits")
    elif len(set(result)) == 2:
        st.session_state.credits += 2
        st.info("Kleiner Gewinn! +2 Credits")


def retry():
    st.session_state.credits = 10
    st.session_state.result = ["❔", "❔", "❔"]
    slot_display.markdown(
        f"<div class='slot-box'>{' '.join(st.session_state.result)}</div>",
        unsafe_allow_html=True,
    )


# Initiale Anzeige
slot_display.markdown(
    f"<div class='slot-box'>{' '.join(st.session_state.result)}</div>",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    if st.session_state.credits > 0:
        st.button("🎲 Spin", use_container_width=True, on_click=spin)

with col2:
    if st.session_state.credits <= 0:
        st.button("🔄 Retry", use_container_width=True, on_click=retry)

if st.session_state.credits <= 0:
    st.error("Keine Credits mehr! Drücke Retry zum Neustart.")
