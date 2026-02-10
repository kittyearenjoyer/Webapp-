import streamlit as st
import random
import hashlib

st.set_page_config(page_title="Ashtar-Orakel", page_icon="✨")

st.title("✨ Ashtar-Sheran Orakel")
st.write("Fiktive, satirische Botschaften aus der galaktischen Föderation.")

name = st.text_input("Dein Name:")

rollen = [
    "wurde für eine geheime Mission ausgewählt",
    "trägt einen verborgenen Sternencode in sich",
    "ist ein inkarniertes Mitglied der Sternenflotte",
    "steht unter direkter Beobachtung",
    "fungiert als kosmischer Verbindungspunkt",
]

mutterschiff = [
    "Das Mutterschiff, das gleichzeitig in mehreren Dimensionen existiert",
    "Ein extradimensionales Mutterschiff außerhalb von Raum und Zeit",
    "Das mehrdimensionale Flaggschiff der Föderation",
    "Ein Mutterschiff, das parallel durch mehrere Realitäten gleitet",
    "Die interdimensionale Kommandozentrale der Flotte",
]

aktionen = [
    "sendet dir verschlüsselte Signale",
    "bereitet deine Aktivierung vor",
    "synchronisiert sich mit deinem Bewusstsein",
    "beobachtet deine Zeitlinie",
    "kalibriert deine Realität",
]

ziele = [
    "um das Gleichgewicht der Erde zu stabilisieren",
    "zur Vorbereitung auf den ersten Kontakt",
    "als Teil eines kosmischen Experiments",
    "um eine verborgene Wahrheit zu enthüllen",
    "für eine bevorstehende Dimensionsverschiebung",
]

if st.button("Kosmische Botschaft empfangen"):
    if name.strip() == "":
        st.warning("Bitte erst einen Namen eingeben.")
    else:
        seed = int(hashlib.sha256(name.encode()).hexdigest(), 16)
        random.seed(seed)

        text = (
            f"Nachricht von Ashtar Sheran: {name} {random.choice(rollen)}. "
            f"{random.choice(mutterschiff)} {random.choice(aktionen)}, "
            f"{random.choice(ziele)}."
        )

        st.success(text)
