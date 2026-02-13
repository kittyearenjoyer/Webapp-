import streamlit as st
import random

st.set_page_config(page_title="Rameen Roast Generator")

name = "Rameen"

roasts = [
    f"{name} ich lösche deinen DC Server.",
    f"{name} zerstört Arbeitsplätze.",
    f"{name} kann meine Eier lecken.",
    f"{name} ist ein Hurensohn",
    f"{name}, vibecoden ist scheiße.",
    f"{name} soll sich ficken gehen.",
    f"{name} ist zu dumm um Discord Bots zu managen.",
]

st.title("🔥 Rameen Roast Generator")

if st.button("Roast auslösen"):
    st.subheader(random.choice(roasts))
