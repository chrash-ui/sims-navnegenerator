import random
import streamlit as st

st.set_page_config(page_title="Ultimate Sims Navnegenerator", page_icon="🎮", layout="centered")

# Initialiser historikk i sesjonen hvis den ikke finnes
if "historikk" not in st.session_state:
    st.session_state.historikk = []

st.title("🎮 Ultimate Sims Navnegenerator")
st.write("Skap din neste sim, familie med tilfeldig antall barn og alder, trekk unike trekk og utforsk okkulte navn!")

# --- NAVNELISTER ---
norske_guttenavn_normale = [
    "Lucas", "Oliver", "Filip", "Emil", "Magnus", "Håkon", "Henrik", "Jonas", "Sander", "Jakob",
    "Elias", "Oskar", "Kasper", "Noah", "William", "Mathias", "Lukas", "Aksel", "Markus", "Tobias",
    "Martin", "Fredrik", "Kristian", "Alexander", "Marius", "Andreas", "Daniel", "Sebastian", "Theodor", "Sivert",
    "Johannes", "Emilian", "Casper", "Aron", "Leander", "Gabriel", "Isak", "Sven", "Knut", "Tor",
    "Even", "Jon", "Terje", "Per", "Pål", "Espen", "Stian", "Thomas", "Christian", "Bendik",
    "Mads", "Simen", "Tobias", "Vebjørn", "Eskil", "Sondre", "Brage", "Sturla", "Tage", "Aksel"
]

norske_guttenavn_rare = [
    "Gjest", "Torgeir", "Bjarne", "Reidar", "Gudmund", "Oddgeir", "Bjørn-Sture", "Fritjof",
    "Brynjulf", "Agnar", "Halldor", "Kjell-Bjarne", "Truls", "Trygve", "Tormod", "Asbjørn",
    "Thorbjörn", "Sigurd", "Ragnar", "Øystein", "Guttorm", "Tore", "Audun", "Jarand",
    "Gunnar", "Ottar", "Valdemar", "Fridtjof", "Bård", "Yngve", "Dagfinn", "Reinert",
    "Balder", "Torstein", "Herbjørn", "Varg", "Trond", "Tellef", "Asgeir", "Snorre"
]

norske_jentenavn_normale = [
    "Emma", "Nora", "Olivia", "Ella", "Sofie", "Astrid", "Ingrid", "Signe", "Tiril", "Thea",
    "Ida", "Maja", "Amalie", "Leah", "Sara", "Hanna", "Kaja", "Julie", "Emilie", "Celine",
    "Hedda", "Tuva", "Vilde", "Live", "Sunniva", "Helena", "Selma", "Martine", "Cornelia", "Victoria",
    "Mia", "Hennie", "Amelia", "Frida", "Agnes", "Sigrid", "Line", "Silje", "Marte", "Camilla",
    "Eline", "Stine", "Tonje", "Heidi", "Kristine", "Charlotte", "Pernille", "Johanne", "Marthe", "Cecilie",
    "Sanna", "Malin", "Ronja", "Ylva", "Oda", "Mille", "Filippa", "Thea", "Carina", "Elise"
]

norske_jentenavn_
