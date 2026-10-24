import random
import streamlit as st

# Lister med faste navn for å nå 500+ kombinasjoner
norske_fornavn = [
    "Emma", "Nora", "Olivia", "Ella", "Sofie", "Astrid", "Ingrid", "Signe", "Tiril", "Thea",
    "Ida", "Maja", "Amalie", "Leah", "Sara", "Hanna", "Kaja", "Julie", "Emilie", "Celine",
    "Lucas", "Oliver", "Filip", "Emil", "Magnus", "Håkon", "Henrik", "Jonas", "Sander", "Jakob",
    "Elias", "Oskar", "Kasper", "Noah", "William", "Mathias", "Lukas", "Aksel", "Markus", "Tobias",
    "Gjest", "Torgeir", "Gry", "Kjell-Bjarne", "Trude-Lise", "Bjarne", "Reidar", "Gudmund", 
    "Svanhild", "Asbjørg", "Torbjørg", "Gunnvor", "Oddgeir", "Kjellaug", "Bjørn-Sture", "Fritjof",
    "Gunda", "Brynjulf", "Gunnbjørg", "Agnar", "Solveig", "Thorbjörn", "Halldor", "Borghild"
]

engelske_fornavn = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Theodore",
    "Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper",
    "Ethan", "Alexander", "Mason", "Logan", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Aria",
    "Barnaby", "Bartholomew", "Cletus", "Ezekiel", "Hortense", "Mildred", "Agnes", "Aloysius", 
    "Beatrice", "Cressida", "Flementine", "Giles", "Ignatius", "Jezebel", "Montgomery", "Persephone",
    "Archibald", "Gertrude", "Ebenezer", "Prudence", "Zebedee", "Wilhelmina", "Horace", "Tabitha"
]

etternavn = [
    "Hansen", "Johansen", "Olsen", "Andersen", "Pedersen", "Nilsen", "Kristiansen", "Larsen", "Sørensen", "Rasmussen",
    "Fløte", "Søt", "Knudaas", "Dalland", "Kvack", "Blåbær", "Myhre", "Bakken", "Solheim", "Strand",
    "Fjell", "Vangen", "Sivertsen", "Tveit", "Krogh", "Stensrud", "Grønn", "Rød", "Gull", "Melk",
    "Tøffel", "Skinknes", "Vaffel", "Spekesild", "Knoll", "Tott", "Gjørmedal", "Langbein", "Mås",
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
    "Pancake", "Frizzled", "Doom", "Pudding", "Boots", "Waffle", "Snickerdoodle", "Bubble", "Chaos", "Spoons",
    "Pendelton", "Cumberbatch", "Butterworth", "Snodgrass", "Pettibone", "Hollingsworth", "Pumpernickel",
    "Thorn", "Winterbottom", "Sprocket", "Gasket", "Fumble", "Bumblebee", "Dingle", "Snort"
]

# Nettside-design
st.title("🎮 Sims Navnegenerator")
st.write("Generer gøye og normale navn til din neste Sim!")

if st.button("🎲 Generer nytt navn", type="primary"):
    spraak = random.choice(["Norsk", "Engelsk"])
    fornavn = random.choice(norske_fornavn if spraak == "Norsk" else engelske_fornavn)
    etter = random.choice(etternavn)
    
    st.header(f"✨ {fornavn} {etter}")
    st.caption(f"Språkstil: {spraak}")
