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

norske_jentenavn_rare = [
    "Gry", "Trude-Lise", "Svanhild", "Asbjørg", "Torbjørg", "Gunnvor", "Kjellaug", "Gunda",
    "Gunnbjørg", "Solveig", "Borghild", "Gerd", "Ragnhild", "Ragna", "Wenche", "Bergljot",
    "Aslaug", "Torhild", "Liv", "Gunhild", "Hjordis", "Valborg", "Signhild", "Thora",
    "Ingebjørg", "Guri", "Berit", "Tordis", "Magnhild", "Oddbjørg", "Rannveig", "Åse",
    "Siv", "Tora", "Frøydis", "Gunvor", "Rønnaug", "Herborg", "Ylva", "Sunniva"
]

engelske_guttenavn_normale = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Theodore",
    "Ethan", "Alexander", "Mason", "Logan", "Caleb", "Jack", "Owen", "Gabriel", "Carter", "Luke",
    "Daniel", "Matthew", "David", "Joseph", "Samuel", "John", "Wyatt", "Aiden", "Julian", "Grayson",
    "Leo", "Isaiah", "Charles", "Thomas", "Josiah", "Hudson", "Christian", "Hunter", "Connor", "Eli",
    "Ezra", "Aaron", "Landon", "Adrian", "Jonathan", "Nolan", "Jeremiah", "Easton", "Elias", "Colton",
    "Miles", "Cody", "Blake", "Asher", "Carson", "Austin", "Max", "Tyler", "Brandon", "Kevin"
]

engelske_guttenavn_rare = [
    "Barnaby", "Bartholomew", "Cletus", "Ezekiel", "Aloysius", "Giles", "Ignatius", "Montgomery",
    "Archibald", "Ebenezer", "Zebedee", "Horace", "Clarence", "Eustace", "Percival", "Hubert",
    "Phineas", "Balthazar", "Cornelius", "Thaddeus", "Rufus", "Ulysses", "Ambrose", "Gervase",
    "Beauregard", "Ignatz", "Skeeter", "Clyde", "Merle", "Elmer", "Wile E",
    "Aloysius", "Zephyr", "Bartholomew", "Mortimer", "Ignatius", "Thaddeus", "Gideon", "Barnaby"
]

engelske_jentenavn_normale = [
    "Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper",
    "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Aria", "Scarlett", "Grace", "Chloe", "Victoria",
    "Riley", "Lily", "Aubrey", "Zoey", "Penelope", "Hannah", "Lillian", "Addison",
    "Ellie", "Stella", "Natalie", "Zoe", "Leah", "Hazel", "Violet", "Aurora", "Savannah", "Audrey",
    "Brooklyn", "Bella", "Claire", "Skylar", "Lucy", "Paisley", "Everly", "Anna", "Caroline", "Nova",
    "Maya", "Naomi", "Elena", "Sarah", "Alice", "Samantha", "Ruby", "Piper", "Quinn", "Sadie"
]

engelske_jentenavn_rare = [
    "Hortense", "Mildred", "Agnes", "Beatrice", "Cressida", "Flementine", "Jezebel", "Persephone",
    "Gertrude", "Prudence", "Wilhelmina", "Tabitha", "Hephzibah", "Petunia", "Mabel", "Brunhilde",
    "Eunice", "Gladys", "Maude", "Pansy", "Agatha", "Winifred", "Hermione", "Cornelia",
    "Gwendolyn", "Blanche", "Beryl", "Enid", "Myrtle", "Opal", "Zenobia", "Clementine",
    "Elvira", "Morticia", "Wednesday", "Zephyra", "Ophelia", "Hexa", "Belladonna", "Raven"
]

okkulte_fornavn = [
    "Vladislaus", "Count", "Lilith", "Raven", "Shadow", "Dracula", "Nosferatu", "Vespera",
    "Malakor", "Zephyr", "Pandora", "Grim", "Nyx", "Oberon", "Titania", "Astaroth",
    "Hexia", "Zeus", "Hecate", "Lucifer", "Vampira", "Nebula", "Xylar", "Zod",
    "Asmodeus", "Mortis", "Vesper", "Sable", "Thorne", "Midnight", "Eclipse", "Banshee"
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

okkulte_etternavn = [
    "Bloodworth", "Nightshade", "Grimwood", "Blackwood", "Cryptic", "Graves", "Shadowfen",
    "Vampire", "Spellbinder", "Moonstone", "Bones", "Darkness", "Abyss", "Stormrider", "Casket"
]

# --- SPILLSPESIFIKKE TREKK OG LIVSMÅL ---
spill_database = {
    "Sims 4 (Moderne)": {
        "trekk": ["Klossete", "Hissig", "Kreativ", "Lat", "Geni", "Matvrak", "Høflig", "Romantisk", "Sjenert", "Overambisiøs", "Innadvendt", "Selskapssyk"],
        "mal": ["Bli superkjendis", "Mestre matlaging", "Finne sann kjærlighet", "Kjøpe drømmehuset", "Fullføre et aspirasjonsmål"]
    },
    "Sims 3 (Åpen verden)": {
        "trekk": ["Samler", "Overfladisk", "Pyroman", "Håpløs romantiker", "Eksentrisk", "Besserwisser", "Naturist", "Drømmende", "Leken", "Kynisk"],
        "mal": ["Oppfylle en livslang drøm", "Lære alle ferdigheter", "Eie hele byen", "Se spøkelser i mausoleet", "Bli mestertyv"]
    },
    "Sims 2 (Klassisk drama)": {
        "trekk": ["Dramatisk", "Lidenskapelig", "Sjalus", "Målrettet", "Festsugen", "Innesluttet", "Eplekjekk", "Høyt på pæra", "Mystisk"],
        "mal": ["Ha 20 elskere samtidig", "Få 10 i alle ferdigheter", "Fylle livsmålet (Knowledge/Fortune)", "Avdekke familiedrama", "Finne igjen Bella Goth"]
    },
    "Sims 1 (Retro/Original)": {
        "trekk": ["Panisk for brann", "Avhengig av pizza", "Kranglevoren", "Evig uheldig", "Gjerrig", "Stuegris", "Tvangsmessig rydder"],
        "mal": ["Bli rik nok til et basseng uten stige", "Overleve spøkelsene i huset", "Få naboene til å like deg", "Kjøpe en magisk dverg", "Unngå marsvin-syken"]
    }
}

voksne_aldre = ["Ung voksen", "Voksen", "Eldre"]
barn_aldre = ["Baby", "Småbarn (Toddler)", "Barn", "Tenåring"]

# --- SIDESTOLPE (INNSTILLINGER) ---
st.sidebar.header("⚙️ Konfigurasjon")
valgt_spill = st.sidebar.selectbox("Velg Sims-versjon:", list(spill_database.keys()))
valgt_modus = st.sidebar.radio("Modus:", ["Enkeltsim", "Familie (Dynamisk antall barn & alder)"])
valgt_spraak = st.sidebar.selectbox("Velg språk:", ["Begge", "Norsk", "Engelsk"])
valgt_kjonn = st.sidebar.selectbox("Velg kjønn:", ["Begge", "Gutt", "Jente"])
valgt_type = st.sidebar.selectbox("Velg navnetype:", ["Begge", "Normale", "Rare & gøye", "Okkult 🦇"])

full_random = st.sidebar.checkbox("🎲 Fullstendig tilfeldig", value=False)

def hent_fornavn(kjonn, stil, spraak):
    if stil == "Okkult":
        return random.choice(okkulte_fornavn)
    if spraak == "Norsk":
        if kjonn == "Gutt":
            return random.choice(norske_guttenavn_normale if stil == "Normal" else norske_guttenavn_rare)
        else:
            return random.choice(norske_jentenavn_normale if stil == "Normal" else norske_jentenavn_rare)
    else:
        if kjonn == "Gutt":
            return random.choice(engelske_guttenavn_normale if stil == "Normal" else engelske_guttenavn_rare)
        else:
            return random.choice(engelske_jentenavn_normale if stil == "Normal" else engelske_jentenavn_rare)

def hent_enkelt_navn():
    if full_random:
        s = random.choice(["Norsk", "Engelsk"])
        k = random.choice(["Gutt", "Jente"])
        t = random.choice(["Normal", "Rare", "Okkult"])
    else:
        s = random.choice(["Norsk", "Engelsk"]) if valgt_spraak == "Begge" else valgt_spraak
        k = random.choice(["Gutt", "Jente"]) if valgt_kjonn == "Begge" else valgt_kjonn
        if valgt_type == "Begge":
            t = random.choice(["Normal", "Rare", "Okkult"])
        elif valgt_type == "Normale":
            t = "Normal"
        elif valgt_type == "Rare & gøye":
            t = "Rare"
        else:
            t = "Okkult"

    if t == "Okkult":
        etter = random.choice(okkulte_etternavn)
        spraak_tekst = "Okkult / Overnaturlig"
    else:
        etter = random.choice(etternavn_norske if s == "Norsk" else etternavn_engelske)
        spraak_tekst = s

    fornavn = hent_fornavn(k, t, s)
    spill_trekk = spill_database[valgt_spill]["trekk"]
    spill_mal = spill_database[valgt_spill]["mal"]
    
    trekk = random.sample(spill_trekk, min(2, len(spill_trekk)))
    mal = random.choice(spill_mal)
    alder = random.choice(voksne_aldre + barn_aldre)

    return {
        "navn": f"{fornavn} {etter}",
        "spraak": spraak_tekst,
        "kjonn": k,
        "stil": t,
        "alder": alder,
        "trekk": f"{trekk[0]} og {trekk[1]}",
        "mal": mal
    }

# --- HOVEDDEL ---
if st.button("✨ Generer nytt!", type="primary", use_container_width=True):
    spill_trekk = spill_database[valgt_spill]["trekk"]
    spill_mal = spill_database[valgt_spill]["mal"]

    if valgt_modus == "Enkeltsim":
        sim = hent_enkelt_navn()
        resultat_tekst = f"### 🧑 {sim['navn']}\n* **Alder:** {sim['alder']}\n* **Spill:** {valgt_spill}\n* **Stil/Språk:** {sim['spraak']} ({sim['stil']})\n* **Trekk:** {sim['trekk']}\n* **Livsmål:** {sim['mal']}"
        st.success(resultat_tekst)
        st.session_state.historikk.insert(0, f"[{valgt_spill}] {sim['navn']} ({sim['alder']}) - {sim['trekk']}")
    else:
        # Generer familie med variert antall barn og alder
        s = random.choice(["Norsk", "Engelsk"]) if valgt_spraak == "Begge" else valgt_spraak
        t = "Okkult" if valgt_type == "Okkult 🦇" else ("Normal" if valgt_type == "Normale" else ("Rare" if valgt_type == "Rare & gøye" else random.choice(["Normal", "Rare"])))

        if t == "Okkult":
            felles_etter = random.choice(okkulte_etternavn)
        else:
            felles_etter = random.choice(etternavn_norske if s == "Norsk" else etternavn_engelske)

        # Foreldre (1 eller 2 foreldre)
        antall_foreldre = random.choice([1, 2])
        foreldre_liste = []
        for i in range(antall_foreldre):
            k = random.choice(["Gutt", "Jente"])
            fornavn = hent_fornavn(k, t, s)
            alder = random.choice(voksne_aldre)
            trekk = random.choice(spill_trekk)
            foreldre_liste.append(f"**Forelder {i+1} ({alder}):** {fornavn} {felles_etter} *(Trekk: {trekk})*")

        # Barn (0 til 4 barn)
        antall_barn = random.randint(0, 4)
        barn_liste = []
        for i in range(antall_barn):
            k = random.choice(["Gutt", "Jente"])
            fornavn = hent_fornavn(k, t, s)
            alder = random.choice(barn_aldre)
            trekk = random.choice(spill_trekk)
            barn_liste.append(f"**Barn {i+1} ({alder}):** {fornavn} {felles_etter} *(Trekk/Mål: {trekk})*")

        fam_tekst = f"### 👨‍👩‍👧‍👦 Familie {felles_etter} ({valgt_spill})\n"
        fam_tekst += "\n".join(foreldre_liste) + "\n\n"
        if barn_liste:
            fam_tekst += "**Barn inngår i husholdningen:**\n" + "\n".join(barn_liste)
        else:
            fam_tekst += "*Ingen barn i denne husholdningen ennå.*"

        st.success(fam_tekst)
        st.session_state.historikk.insert(0, f"[{valgt_spill}] Familie {felles_etter} ({antall_foreldre} voksne, {antall_barn} barn)")

# --- HISTORIKK ---
if st.session_state.historikk:
    st.markdown("---")
    st.subheader("📜 Tidligere genererte (Historikk)")
    for h in st.session_state.historikk[:5]:
        st.text(h)
    
    if st.button("Tøm historikk"):
        st.session_state.historikk = []
        st.rerun()
