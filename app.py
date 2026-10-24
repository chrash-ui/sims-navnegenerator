import random
import streamlit as st

st.set_page_config(page_title="Ultimate Sims Navnegenerator", page_icon="🎮", layout="centered")

# Initialiser historikk i sesjonen hvis den ikke finnes
if "historikk" not in st.session_state:
    st.session_state.historikk = []

st.title("🎮 Ultimate Sims Navnegenerator")
st.write("Skap din neste sim, familie, trekk personlighetstrekk og velg Sims-æra!")

# --- NAVNELISTER (500+ navn) ---
norske_guttenavn_normale = [
    "Lucas", "Oliver", "Filip", "Emil", "Magnus", "Håkon", "Henrik", "Jonas", "Sander", "Jakob",
    "Elias", "Oskar", "Kasper", "Noah", "William", "Mathias", "Lukas", "Aksel", "Markus", "Tobias",
    "Martin", "Fredrik", "Kristian", "Alexander", "Marius", "Andreas", "Daniel", "Sebastian", "Theodor", "Sivert",
    "Johannes", "Emilian", "Casper", "Aron", "Leander", "Gabriel", "Isak", "Sven", "Knut", "Tor",
    "Even", "Jon", "Terje", "Per", "Pål", "Espen", "Stian", "Thomas", "Christian", "Bendik"
]

norske_guttenavn_rare = [
    "Gjest", "Torgeir", "Bjarne", "Reidar", "Gudmund", "Oddgeir", "Bjørn-Sture", "Fritjof",
    "Brynjulf", "Agnar", "Halldor", "Kjell-Bjarne", "Truls", "Trygve", "Tormod", "Asbjørn",
    "Thorbjörn", "Sigurd", "Ragnar", "Øystein", "Guttorm", "Tore", "Audun", "Jarand",
    "Gunnar", "Ottar", "Valdemar", "Fridtjof", "Bård", "Yngve", "Dagfinn", "Reinert"
]

norske_jentenavn_normale = [
    "Emma", "Nora", "Olivia", "Ella", "Sofie", "Astrid", "Ingrid", "Signe", "Tiril", "Thea",
    "Ida", "Maja", "Amalie", "Leah", "Sara", "Hanna", "Kaja", "Julie", "Emilie", "Celine",
    "Hedda", "Tuva", "Vilde", "Live", "Sunniva", "Helena", "Selma", "Martine", "Cornelia", "Victoria",
    "Mia", "Hennie", "Amelia", "Frida", "Agnes", "Sigrid", "Line", "Silje", "Marte", "Camilla",
    "Eline", "Stine", "Tonje", "Heidi", "Kristine", "Charlotte", "Pernille", "Johanne", "Marthe", "Cecilie"
]

norske_jentenavn_rare = [
    "Gry", "Trude-Lise", "Svanhild", "Asbjørg", "Torbjørg", "Gunnvor", "Kjellaug", "Gunda",
    "Gunnbjørg", "Solveig", "Borghild", "Gerd", "Ragnhild", "Ragna", "Wenche", "Bergljot",
    "Aslaug", "Torhild", "Liv", "Gunhild", "Hjordis", "Valborg", "Signhild", "Thora",
    "Ingebjørg", "Guri", "Berit", "Tordis", "Magnhild", "Oddbjørg", "Rannveig", "Åse"
]

engelske_guttenavn_normale = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Theodore",
    "Ethan", "Alexander", "Mason", "Logan", "Caleb", "Jack", "Owen", "Gabriel", "Carter", "Luke",
    "Daniel", "Matthew", "David", "Joseph", "Samuel", "John", "Wyatt", "Aiden", "Julian", "Grayson",
    "Leo", "Isaiah", "Charles", "Thomas", "Josiah", "Hudson", "Christian", "Hunter", "Connor", "Eli",
    "Ezra", "Aaron", "Landon", "Adrian", "Jonathan", "Nolan", "Jeremiah", "Easton", "Elias", "Colton"
]

engelske_guttenavn_rare = [
    "Barnaby", "Bartholomew", "Cletus", "Ezekiel", "Aloysius", "Giles", "Ignatius", "Montgomery",
    "Archibald", "Ebenezer", "Zebedee", "Horace", "Clarence", "Eustace", "Percival", "Hubert",
    "Phineas", "Balthazar", "Cornelius", "Thaddeus", "Rufus", "Ulysses", "Ambrose", "Gervase",
    "Beauregard", "Ignatz", "Skeeter", "Clyde", "Merle", "Elmer", "Wile E"
]

engelske_jentenavn_normale = [
    "Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper",
    "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Aria", "Scarlett", "Grace", "Chloe", "Victoria",
    "Riley", "Lily", "Aubrey", "Zoey", "Penelope", "Hannah", "Lillian", "Addison",
    "Ellie", "Stella", "Natalie", "Zoe", "Leah", "Hazel", "Violet", "Aurora", "Savannah", "Audrey",
    "Brooklyn", "Bella", "Claire", "Skylar", "Lucy", "Paisley", "Everly", "Anna", "Caroline", "Nova"
]

engelske_jentenavn_rare = [
    "Hortense", "Mildred", "Agnes", "Beatrice", "Cressida", "Flementine", "Jezebel", "Persephone",
    "Gertrude", "Prudence", "Wilhelmina", "Tabitha", "Hephzibah", "Petunia", "Mabel", "Brunhilde",
    "Eunice", "Gladys", "Maude", "Pansy", "Agatha", "Winifred", "Hermione", "Cornelia",
    "Gwendolyn", "Blanche", "Beryl", "Enid", "Myrtle", "Opal", "Zenobia", "Clementine"
]

etternavn_norske = [
    "Hansen", "Johansen", "Olsen", "Andersen", "Pedersen", "Nilsen", "Kristiansen", "Larsen", "Sørensen", "Rasmussen",
    "Fløte", "Søt", "Knudaas", "Dalland", "Kvack", "Blåbær", "Myhre", "Bakken", "Solheim", "Strand",
    "Fjell", "Vangen", "Sivertsen", "Tveit", "Krogh", "Stensrud", "Grønn", "Rød", "Gull", "Melk",
    "Tøffel", "Skinknes", "Vaffel", "Spekesild", "Knoll", "Tott", "Gjørmedal", "Langbein", "Mås",
    "Berg", "Haugen", "Moen", "Holm", "Dahl", "Eriksen", "Karlsen", "Johnsen", "Pettersen", "Svendsen",
    "Jakobsen", "Jørgensen", "Henriksen", "Halvorsen", "Mo", "Fredriksen", "Andresen", "Nielsen",
    "Blom", "Gjesdal", "Svinø", "Fladen", "Kål", "Loffen", "Pølse", "Blyant", "Knall", "Smør"
]

etternavn_engelske = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
    "Pancake", "Frizzled", "Doom", "Pudding", "Boots", "Waffle", "Snickerdoodle", "Bubble", "Chaos", "Spoons",
    "Pendelton", "Cumberbatch", "Butterworth", "Snodgrass", "Pettibone", "Hollingsworth", "Pumpernickel",
    "Thorn", "Winterbottom", "Sprocket", "Gasket", "Fumble", "Bumblebee", "Dingle", "Snort",
    "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Moore", "Young",
    "Fluffernutter", "Snoot", "Wigglesworth", "Bumble", "Snicklefritz", "Giggle", "Skunk", "Toadstool", "Mud puddle"
]

trekk_liste = [
    "Klossete", "Hissig", "Kreativ", "Lat", "Geni", "Matvrak", "Høflig", "Romantisk", 
    "Sjenert", "Overambisiøs", "Klein", "Optimist", "Drama-queen", "Besserwisser", "Kaotisk"
]

mal_liste = [
    "Bli rik", "Finne den ekte kjærlighet", "Mestre matlaging og spise alt", 
    "Skape maksimalt med kaos", "Bli verdensberømt", "Bo i et falleferdig skur og overleve", "Bli mestertyv"
]

# --- SIDESTOLPE (INNSTILLINGER) ---
st.sidebar.header("⚙️ Konfigurasjon")
valgt_spill = st.sidebar.selectbox("Velg Sims-versjon:", ["Sims 4 (Moderne)", "Sims 3 (Åpen verden)", "Sims 2 (Klassisk drama)", "Sims 1 (Retro/Original)"])
valgt_modus = st.sidebar.radio("Modus:", ["Enkeltsim", "Familie (Foreldre + Barn)"])
valgt_spraak = st.sidebar.selectbox("Velg språk:", ["Begge", "Norsk", "Engelsk"])
valgt_kjonn = st.sidebar.selectbox("Velg kjønn:", ["Begge", "Gutt", "Jente"])
valgt_type = st.sidebar.selectbox("Velg navnetype:", ["Begge", "Normale", "Rare & gøye"])

full_random = st.sidebar.checkbox("🎲 Fullstendig tilfeldig", value=False)

def hent_enkelt_navn():
    if full_random:
        s = random.choice(["Norsk", "Engelsk"])
        k = random.choice(["Gutt", "Jente"])
        t = random.choice(["Normal", "Rare"])
    else:
        s = random.choice(["Norsk", "Engelsk"]) if valgt_spraak == "Begge" else valgt_spraak
        k = random.choice(["Gutt", "Jente"]) if valgt_kjonn == "Begge" else valgt_kjonn
        t = random.choice(["Normal", "Rare"]) if valgt_type == "Begge" else ("Normal" if valgt_type == "Normale" else "Rare")

    if s == "Norsk":
        liste = (norske_guttenavn_normale if t == "Normal" else norske_guttenavn_rare) if k == "Gutt" else (norske_jentenavn_normale if t == "Normal" else norske_jentenavn_rare)
        etter = random.choice(etternavn_norske)
    else:
        liste = (engelske_guttenavn_normale if t == "Normal" else engelske_guttenavn_rare) if k == "Gutt" else (engelske_jentenavn_normale if t == "Normal" else engelske_jentenavn_rare)
        etter = random.choice(etternavn_engelske)

    fornavn = random.choice(liste)
    trekk = random.sample(trekk_liste, 2)
    mal = random.choice(mal_liste)

    return {
        "navn": f"{fornavn} {etter}",
        "spraak": s,
        "kjonn": k,
        "stil": "Normal" if t == "Normal" else "Rare/Gøy",
        "trekk": f"{trekk[0]} og {trekk[1]}",
        "mal": mal
    }

# --- HOVEDDEL ---
if st.button("✨ Generer nytt!", type="primary", use_container_width=True):
    if valgt_modus == "Enkeltsim":
        sim = hent_enkelt_navn()
        resultat_tekst = f"### 🧑 {sim['navn']}\n* **Språk:** {sim['spraak']} | **Stil:** {sim['stil']}\n* **Trekk:** {sim['trekk']}\n* **Livsmål:** {sim['mal']}"
        st.success(resultat_tekst)
        st.session_state.historikk.insert(0, f"[{valgt_spill}] {sim['navn']} ({sim['trekk']})")
    else:
        # Generer familie med felles etternavn
        s = random.choice(["Norsk", "Engelsk"]) if valgt_spraak == "Begge" else valgt_spraak
        felles_etter = random.choice(etternavn_norske if s == "Norsk" else etternavn_engelske)
        
        # Forelder 1
        f1_for = random.choice(norske_guttenavn_normale if s == "Norsk" else engelske_guttenavn_normale)
        # Forelder 2
        f2_for = random.choice(norske_jentenavn_normale if s == "Norsk" else engelske_jentenavn_normale)
        # Barn
        barn_for = random.choice((norske_guttenavn_normale + norske_jentenavn_normale) if s == "Norsk" else (engelske_guttenavn_normale + engelske_jentenavn_normale))

        fam_tekst = f"### 👨‍👩‍👦 Familie {felles_etter}\n"
        fam_tekst += f"* **Forelder 1:** {f1_for} {felles_etter} (Trekk: {random.choice(trekk_liste)})\n"
        fam_tekst += f"* **Forelder 2:** {f2_for} {felles_etter} (Trekk: {random.choice(trekk_liste)})\n"
        fam_tekst += f"* **Barn:** {barn_for} {felles_etter} (Livsmål: {random.choice(mal_liste)})"
        
        st.success(fam_tekst)
        st.session_state.historikk.insert(0, f"[{valgt_spill}] Familie {felles_etter} ({f1_for}, {f2_for}, {barn_for})")

# --- HISTORIKK ---
if st.session_state.historikk:
    st.markdown("---")
    st.subheader("📜 Tidligere genererte (Historikk)")
    for h in st.session_state.historikk[:5]:  # Vis de 5 siste
        st.text(h)
    
    if st.button("Tøm historikk"):
        st.session_state.historikk = []
        st.rerun()
