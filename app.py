import streamlit as st
import time
import random
import csv
import os

HIGHSCORE_FILE = "highscores.csv"
MAX_SCORES = 5


def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    scores = []
    with open(HIGHSCORE_FILE, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                name, t = row
                scores.append((name, float(t)))
    return sorted(scores, key=lambda x: x[1])[:MAX_SCORES]


def save_highscores(scores):
    with open(HIGHSCORE_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for name, t in scores:
            writer.writerow([name, f"{t:.4f}"])


def update_highscores(name, reaction_time):
    scores = load_highscores()
    scores.append((name, reaction_time))
    scores = sorted(scores, key=lambda x: x[1])[:MAX_SCORES]
    save_highscores(scores)


if "phase" not in st.session_state:
    st.session_state.phase = "idle"
    st.session_state.start_time = 0.0
    st.session_state.wait_until = 0.0
    st.session_state.result = None


st.title("Reaktionszeit-Tester")

name = st.text_input("Name", key="player_name")


def start_round():
    delay = random.uniform(2.0, 5.0)
    st.session_state.wait_until = time.time() + delay
    st.session_state.phase = "waiting"
    st.session_state.result = None


def register_click():
    now = time.time()

    if st.session_state.phase == "waiting":
        if now < st.session_state.wait_until:
            st.session_state.phase = "invalid"
            st.session_state.result = None
        else:
            st.session_state.phase = "ready"
            st.session_state.start_time = now

    elif st.session_state.phase == "ready":
        rt = now - st.session_state.start_time
        st.session_state.result = rt
        st.session_state.phase = "result"
        if name.strip():
            update_highscores(name.strip(), rt)


if st.session_state.phase == "idle":
    st.button("Start", on_click=start_round)
    st.write("Klicke Start und warte auf das Signal.")

elif st.session_state.phase == "waiting":
    st.button("KLICK!", on_click=register_click)
    if time.time() >= st.session_state.wait_until:
        st.session_state.phase = "ready"
        st.session_state.start_time = time.time()
        st.rerun()
    st.write("Warte auf das Signal...")

elif st.session_state.phase == "ready":
    st.button("JETZT KLICKEN!", on_click=register_click)
    st.success("JETZT!")

elif st.session_state.phase == "invalid":
    st.error("Zu früh geklickt! Versuch ungültig.")
    st.button("Neu starten", on_click=lambda: st.session_state.update(phase="idle"))

elif st.session_state.phase == "result":
    st.success(f"Reaktionszeit: {st.session_state.result:.4f} s")
    st.button("Neu starten", on_click=lambda: st.session_state.update(phase="idle"))


st.divider()
st.subheader("Highscores")

highscores = load_highscores()

if highscores:
    for i, (n, t) in enumerate(highscores, 1):
        st.write(f"{i}. {n} — {t:.4f} s")
else:
    st.write("Noch keine Einträge.")
