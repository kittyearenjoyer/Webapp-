import streamlit as st
import random

st.set_page_config(page_title="Rameen Roast Generator")

name = "Rameen"

roasts = [
    f"{name} nennt es Vibe Coding, aber sein Code hat die Stabilität von nassem Toast.",
    f"{name} debuggt nach dem Prinzip: neu starten und hoffen.",
    f"{name}s Code ist ein Abenteuer – niemand weiß, was als Nächstes passiert.",
    f"Wenn Improvisation eine IDE wäre, würde {name} darin coden.",
    f"{name} schreibt Code wie ein DJ mixt: viel Vibe, wenig Struktur.",
    f"Bei {name} ist jeder Bug Teil des kreativen Prozesses.",
    f"{name}s Projekte laufen auf Mut, Chaos und minimaler Planung.",
]

st.title("🔥 Rameen Roast Generator")

if st.button("Roast auslösen"):
    st.subheader(random.choice(roasts))
