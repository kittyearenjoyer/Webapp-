import streamlit as st
import random

# Initialisierung des Session State
if "credits" not in st.session_state:
    st.session_state.credits = 10

if "result" not in st.session_state:
    st.session_state.result = ["❔", "❔", "❔"]

symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]

st.title("🎰 Mini Slot Maschine")

st.write(f"**Credits:** {st.session_state.credits}")

def spin():
    if st.session_state.credits <= 0:
        return

    st.session_state.credits -= 1
    result = [random.choice(symbols) for _ in range(3)]
    st.session_state.result = result

    # Gewinnlogik
    if result[0] == result[1] == result[2]:
        st.session_state.credits += 5
        st.success("Jackpot! +5 Credits")
    elif len(set(result)) == 2:
        st.session_state.credits += 2
        st.info("Kleiner Gewinn! +2 Credits")

def retry():
    st.session_state.credits = 10
    st.session_state.result = ["❔", "❔", "❔"]

# Anzeige der Walzen
st.markdown(
    f"<h1 style='text-align: center;'>{' | '.join(st.session_state.result)}</h1>",
    unsafe_allow_html=True
)

# Buttons
if st.session_state.credits > 0:
    st.button("Spin", on_click=spin)
else:
    st.error("Keine Credits mehr!")
    st.button("Retry (neu starten)", on_click=retry)
