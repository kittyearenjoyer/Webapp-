import streamlit as st
import time
import os

# --- UI Setup ---
st.set_page_config(page_title="Streamlit Log Streamer", layout="wide")
st.title("📂 Echtzeit Log-Datei Stream")
st.write("Diese App überwacht die `access.log` und streamt neue Zeilen direkt ins UI.")

LOG_FILE = "access.log"

# Datei initialisieren, falls nicht vorhanden
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("--- Log Start ---\n")

# --- Der Stream-Container ---
# Wir erstellen einen leeren Bereich, den wir später füllen
log_placeholder = st.empty()

def stream_logs():
    # Wir nutzen eine Liste als Puffer für die letzten X Zeilen
    log_history = []
    
    with open(LOG_FILE, "r") as f:
        # Zum Ende der Datei springen
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)  # Kurze Pause, wenn keine neuen Daten da sind
                continue
            
            # Daten-Transformation (unsere "Pipe" Logik)
            clean_line = line.strip()
            if clean_line:
                # Neue Zeile oben hinzufügen
                log_history.insert(0, f"🕒 {time.strftime('%H:%M:%S')} | {clean_line}")
                
                # Nur die letzten 15 Einträge behalten
                log_history = log_history[:15]
                
                # Das UI-Element mit dem neuen Stream-Inhalt überschreiben
                with log_placeholder.container():
                    for entry in log_history:
                        if "ERROR" in entry:
                            st.error(entry)
                        elif "WARN" in entry:
                            st.warning(entry)
                        else:
                            st.code(entry)

# --- Startknopf ---
if st.button("Stream starten"):
    st.info("Überwachung läuft... (Zum Stoppen den Button oben rechts nutzen)")
    stream_logs()
