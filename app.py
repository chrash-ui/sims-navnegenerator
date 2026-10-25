import random
import streamlit as st

st.set_page_config(page_title="Ultimate Sims Navnegenerator", page_icon="🎮", layout="centered")

# Initialiser historikk i sesjonen hvis den ikke finnes
if "historikk" not in st.session_state:
    st.session_state.historikk = []

st.title("🎮 Ultimate Sims Navnegenerator")
st.write("Skap din neste sim eller familie med spilltilpassede kjæledyr og dyretrekk, utvidede navnelister og karrierer!")

# --- UTVIDEDE NAVNELISTER ---
norske_guttenavn_normale = [
    "Lucas", "Oliver", "Filip", "Emil", "Magnus", "Håkon", "Henrik", "Jonas", "Sander", "Jakob",
    "Elias", "Oskar", "Kasper", "Noah", "William", "Mathias", "Lukas", "Aksel", "Markus", "Tobias",
    "Martin", "Fredrik", "Kristian", "Alexander", "Marius", "Andreas", "Daniel", "Sebastian", "Theodor", "Sivert",
    "Johannes", "Emilian", "Casper", "Aron", "Leander", "Gabriel", "Isak", "Sven", "Knut", "Tor",
    "Even", "Jon", "Terje", "Per", "Pål", "Espen", "Stian", "Thomas", "Christian", "Bendik",
    "Mads", "Simen", "Tobias", "Vebjørn", "Eskil", "Sondre", "Brage", "Sturla", "Tage", "Aksel",
    "Jesper", "Nikolai", "Vetle", "Hermann", "Cornelius", "Adrian", "Julian", "Truls", "Birk", "Sigurd"
]

norske_guttenavn_rare = [
    "Gjest", "Torgeir", "Bjarne", "Reidar", "Gudmund", "Oddgeir", "Bjørn-Sture", "Fritjof",
    "Brynjulf", "Agnar", "Halldor", "Kjell-Bjarne", "Truls", "Trygve", "Tormod", "Asbjørn",
    "Thorbjörn", "Sigurd", "Ragnar", "Øystein", "Guttorm", "Tore", "Audun", "Jarand",
    "Gunnar", "Ottar", "Valdemar", "Fridtjof", "Bård", "Yngve", "Dagfinn", "Reinert",
    "Balder", "Torstein", "Herbjørn", "Varg", "Trond", "Tellef", "Asgeir", "Snorre",
    "Ottar", "Sigbjørn", "Reidar", "Toralf", "Arnulf", "Einar", "Gorm", "Sturle"
]

norske_jentenavn_normale = [
    "Emma", "Nora", "Olivia", "Ella", "Sofie", "Astrid", "Ingrid", "Signe", "Tiril", "Thea",
    "Ida", "Maja", "Amalie", "Leah", "Sara", "Hanna", "Kaja", "Julie", "Emilie", "Celine",
    "Hedda", "Tuva", "Vilde", "Live", "Sunniva", "Helena", "Selma", "Martine", "Cornelia", "Victoria",
    "Mia", "Hennie", "Amelia", "Frida", "Agnes", "Sigrid", "Line", "Silje", "Marte", "Camilla",
    "Eline", "Stine", "Tonje", "Heidi", "Kristine", "Charlotte", "Pernille", "Johanne", "Marthe", "Cecilie",
    "Sanna", "Malin", "Ronja", "Ylva", "Oda", "Mille", "Filippa", "Thea", "Carina", "Elise",
    "Signe", "Thale", "Ada", "Johanne", "Matilde", "Elida", "Oline", "Tale", "Alva", "Erle"
]

norske_jentenavn_rare = [
    "Gry", "Trude-Lise", "Svanhild", "Asbjørg", "Torbjørg", "Gunnvor", "Kjellaug", "Gunda",
    "Gunnbjørg", "Solveig", "Borghild", "Gerd", "Ragnhild", "Ragna", "Wenche", "Bergljot",
    "Aslaug", "Torhild", "Liv", "Gunhild", "Hjordis", "Valborg", "Signhild", "Thora",
    "Ingebjørg", "Guri", "Berit", "Tordis", "Magnhild", "Oddbjørg", "Rannveig", "Åse",
    "Siv", "Tora", "Frøydis", "Gunvor", "Rønnaug", "Herborg", "Ylva", "Sunniva",
    "Gunnhild", "Torunn", "Rønnaug", "Hildur", "Asgjerd", "Signy", "Valdis"
]

engelske_guttenavn_normale = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Theodore",
    "Ethan", "Alexander", "Mason", "Logan", "Caleb", "Jack", "Owen", "Gabriel", "Carter", "Luke",
    "Daniel", "Matthew", "David", "Joseph", "Samuel", "John", "Wyatt", "Aiden", "Julian", "Grayson",
    "Leo", "Isaiah", "Charles", "Thomas", "Josiah", "Hudson", "Christian", "Hunter", "Connor", "Eli",
    "Ezra", "Aaron", "Landon", "Adrian", "Jonathan", "Nolan", "Jeremiah", "Easton", "Elias", "Colton",
    "Miles", "Cody", "Blake", "Asher", "Carson", "Austin", "Max", "Tyler", "Brandon", "Kevin",
    "Cooper", "Parker", "Xavier", "Cole", "Ian", "Dominic", "Jordan", "Brody", "Carson", "Chase"
]

engelske_guttenavn_rare = [
    "Barnaby", "Bartholomew", "Cletus", "Ezekiel", "Aloysius", "Giles", "Ignatius", "Montgomery",
    "Archibald", "Ebenezer", "Zebedee", "Horace", "Clarence", "Eustace", "Percival", "Hubert",
    "Phineas", "Balthazar", "Cornelius", "Thaddeus", "Rufus", "Ulysses", "Ambrose", "Gervase",
    "Beauregard", "Ignatz", "Skeeter", "Clyde", "Merle", "Elmer", "Wile E",
    "Zephyr", "Mortimer", "Gideon", "Gareth", "Bartholomew", "Cyprian", "Cuthbert"
]

engelske_jentenavn_normale = [
    "Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper",
    "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Aria", "Scarlett", "Grace", "Chloe", "Victoria",
    "Riley", "Lily", "Aubrey", "Zoey", "Penelope", "Hannah", "Lillian", "Addison",
    "Ellie", "Stella", "Natalie", "Zoe", "Leah", "Hazel", "Violet", "Aurora", "Savannah", "Audrey",
    "Brooklyn", "Bella", "Claire", "Skylar", "Lucy", "Paisley", "Everly", "Anna", "Caroline", "Nova",
    "Maya", "Naomi", "Elena", "Sarah", "Alice", "Samantha", "Ruby", "Piper", "Quinn", "Sadie",
    "Stella", "Hazel", "Aurora", "Penelope", "Savannah", "Audrey", "Claire", "Skylar"
]

engelske_jentenavn_rare = [
    "Hortense", "Mildred", "Agnes", "Beatrice", "Cressida", "Flementine", "Jezebel", "Persephone",
    "Gertrude", "Prudence", "Wilhelmina", "Tabitha", "Hephzibah", "Petunia", "Mabel", "Brunhilde",
    "Eunice", "Gladys", "Maude", "Pansy", "Agatha", "Winifred", "Hermione", "Cornelia",
    "Gwendolyn", "Blanche", "Beryl", "Enid", "Myrtle", "Opal", "Zenobia", "Clementine",
    "Elvira", "Morticia", "Wednesday", "Zephyra", "Ophelia", "Hexa", "Belladonna", "Raven",
    "Thomasin", "Araminta", "Drusilla", "Gwendolen", "Isolde", "Maudlin"
]

okkulte_fornavn = [
    "Vladislaus", "Count", "Lilith", "Raven", "Shadow", "Dracula", "Nosferatu", "Vespera",
    "Malakor", "Zephyr", "Pandora", "Grim", "Nyx", "Oberon", "Titania", "Astaroth",
    "Hexia", "Zeus", "Hecate", "Lucifer", "Vampira", "Nebula", "Xylar", "Zod",
    "Asmodeus", "Mortis", "Vesper", "Sable", "Thorne", "Midnight", "Eclipse", "Banshee",
    "Malakor", "Azazel", "Mephisto", "Cassandra", "Calypso", "Pandora", "Hecate"
]

# --- DYRENAVN LISTER ---
hundehun_navn = ["Buster", "Karo", "Rex", "Balder", "Bruno", "Rambo", "Theo", "Bamse", "Charlie", "Rocky", "Thor", "Cooper", "Tyson", "Milo"]
hundehun_jente = ["Bella", "Luna", "Ayla", "Maja", "Mira", "Stella", "Freia", "Zelda", "Daisy", "Saga", "Ronja", "Nala"]
katt_navn = ["Pusur", "Milling", "Fjonken", "Felix", "Socks", "Tiger", "Simba", "Oliver", "Nils", "Laban"]
katt_jente = ["Missen", "Nala", "Cleo", "Sassy", "Minni", "Pia", "Siri", "Lily"]
hest_navn = ["Storm", "Faksen", "Spirit", "Gorm", "Thunder", "Cinderella", "Varg", "Dronning", "Blakken", "Star"]
lite_dyr_navn = ["Pip", "Squeak", "Nøtteliten", "Gnagern", "Smule", "Pompel", "Pilt", "Fjonken", "Snickers"]

etternavn_norske = [
    "Hansen", "Johansen", "Olsen", "Andersen", "Pedersen", "Nilsen", "Kristiansen", "Larsen", "Sørensen", "Rasmussen",
    "Fløte", "Søt", "Knudaas", "Dalland", "Kvack", "Blåbær", "Myhre", "Bakken", "Solheim", "Strand",
    "Fjell", "Vangen", "Sivertsen", "Tveit", "Krogh", "Stensrud", "Grønn", "Rød", "Gull", "Melk",
    "Tøffel", "Skinknes", "Vaffel", "Spekesild", "Knoll", "Tott", "Gjørmedal", "Langbein", "Mås",
    "Berg", "Haugen", "Moen", "Holm", "Dahl", "Eriksen", "Karlsen", "Johnsen", "Pettersen", "Svendsen",
    "Jakobsen", "Jørgensen", "Henriksen", "Halvorsen", "Mo", "Fredriksen", "Andresen", "Nielsen",
    "Blom", "Gjesdal", "Svinø", "Fladen", "Kål", "Loffen", "Pølse", "Blyant", "Knall", "Smør",
    "Stubbe", "Ødegaard", "Nygård", "Fossum", "Sandvik", "Klefstad", "Bjerke", "Moe"
]

etternavn_engelske = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
    "Pancake", "Frizzled", "Doom", "Pudding", "Boots", "Waffle", "Snickerdoodle", "Bubble", "Chaos", "Spoons",
    "Pendelton", "Cumberbatch", "Butterworth", "Snodgrass", "Pettibone", "Hollingsworth", "Pumpernickel",
    "Thorn", "Winterbottom", "Sprocket", "Gasket", "Fumble", "Bumblebee", "Dingle", "Snort",
    "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Moore", "Young",
    "Fluffernutter", "Snoot", "Wigglesworth", "Bumble", "Snicklefritz", "Giggle", "Skunk", "Toadstool", "Mud puddle",
    "Pemberton", "Fairchild", "Halloway", "Blackwood", "Sterling", "Wellington"
]

okkulte_etternavn = [
    "Bloodworth", "Nightshade", "Grimwood", "Blackwood", "Cryptic", "Graves", "Shadowfen",
    "Vampire", "Spellbinder", "Moonstone", "Bones", "Darkness", "Abyss", "Stormrider", "Casket",
    "Duskwood", "Hexen", "Mourning", "Silverfang", "Wormwood"
]

relasjonsstatuser = [
    "Singel 💔", 
    "Gift 💍", 
    "Forlovet 💎", 
    "Skilt ⚡", 
    "Det er komplisert... 🎭"
]

studieretninger = ["Biologi 🧬", "Drama & Teater 🎭", "Medisin 🩺", "Fysikk & Vitenskap 🔬", "Kunst & Design 🎨", "Historie & Litteratur 📚", "Juss & Politikk ⚖️", "Bedriftsøkonomi 💼"]

# --- SPILLSPESIFIKKE DATA (MED TILPASSEDE HUSDYR OG DYRETREKK) ---
spill_database = {
    "Sims 4 (Moderne)": {
        "trekk_type": "trekk",
        "har_ung_voksen": True,
        "kan_studere": True,
        "husdyr": ["Hund 🐶", "Katt 🐱", "Hest 🐴 (Horse Ranch)", "Lite kjæledyr (Gnager/Fugl) 🐹"],
        "dyre_trekk": ["Leken 🎾", "Lat 😴", "Aggressiv 💢", "Kosete ❤️", "Uavhengig 🐾", "Fryktsom 💨", "Nysgjerrig 🔍", "Troublemaker 😈", "Aktiv ⚡"],
        "okkulte": [
            "Vampyr 🦇 (Sims 4: Vampires)", 
            "Trollmann / Spellcaster 🪄 (Sims 4: Realm of Magic)", 
            "Romvesen 👽 (Sims 4: Get to Work)", 
            "Varulv 🐺 (Sims 4: Werewolves)", 
            "Havfrue 🧜‍♀️ (Sims 4: Island Living)", 
            "PlantSim 🌱 (Sims 4: Utfordring/Event)"
        ],
        "karrierer": ["Astronaut", "Kokk", "Kriminell", "Forretningsmann", "Underholder", "Forfatter", "Idrettsutøver", "Hemmelig agent", "Stilist", "Forsker"],
        "trekk": ["Klossete", "Hissig", "Kreativ", "Lat", "Geni", "Matvrak", "Høflig", "Romantisk", "Sjenert", "Overambisiøs", "Innadvendt", "Selskapssyk"],
        "mal": ["Bli superkjendis", "Mestre matlaging", "Finne sann kjærlighet", "Kjøpe drømmehuset", "Fullføre et aspirasjonsmål"]
    },
    "Sims 3 (Åpen verden)": {
        "trekk_type": "trekk",
        "har_ung_voksen": True,
        "kan_studere": True,
        "husdyr": ["Hund 🐶", "Katt 🐱", "Hest 🐴 (Sims 3: Pets)", "Lite kjæledyr (Fugl/Krypdyr/Gnager) 🐹"],
        "dyre_trekk": ["Aggressiv 💢", "Eventyrlysten 🧭", "Uavhengig 🐾", "Lat 😴", "Stolt 👑", "Leken 🎾", "Destruktiv 💥", "Jeger 🎯", "Skittgris 🐷", "Nervøs 🫨"],
        "okkulte": [
            "Vampyr 🦇 (Sims 3: Late Night / Supernatural)", 
            "Heks / Warlock 🪄 (Sims 3: Supernatural)", 
            "Romvesen 👽 (Sims 3: Seasons)", 
            "Varulv 🐺 (Sims 3: Supernatural)", 
            "Fe / Fairy 🧚 (Sims 3: Supernatural)", 
            "Zombie 🧟 (Sims 3: Supernatural)", 
            "Genie / Ånd i flaske 🧞 (Sims 3: Showtime)"
        ],
        "karrierer": ["Arkitekt", "Spøkelsesjeger", "Privatetterforsker", "Musiker", "Politiet", "Medisin", "Politiker", "Militæret", "Journalistikk", "Idrett"],
        "trekk": ["Samler", "Overfladisk", "Pyroman", "Håpløs romantiker", "Eksentrisk", "Besserwisser", "Naturist", "Drømmende", "Leken", "Kynisk"],
        "mal": ["Oppfylle en livslang drøm", "Lære alle ferdigheter", "Eie hele byen", "Se spøkelser i mausoleet", "Bli mestertyv"]
    },
    "Sims 2 (Klassisk drama)": {
        "trekk_type": "poeng",
        "har_ung_voksen": False,
        "kan_studere": True,
        "husdyr": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr (Fugl / Marsvin) 🐹"],
        "dyre_trekk": ["Vennlig 😊", "Kranglevoren 😾", "Aktiv ⚡", "Lat 😴", "Uavhengig 🐾", "Krevende 💅", "Leken 🎾", "Støyende 📢"],
        "okkulte": [
            "Vampyr 🦇 (Sims 2: Nightlife)", 
            "Zombie 🧟 (Sims 2: University)", 
            "PlantSim / Plantesim 🌱 (Sims 2: Seasons)", 
            "Servobot / Robot 🤖 (Sims 2: Open for Business)", 
            "Heks / Trollmann 🪄 (Sims 2: Apartment Life)"
        ],
        "karrierer": ["Leker (Toymaking)", "Showbusiness", "Paranormal", "Nattevakt", "Politiet", "Medisin", "Militæret", "Lovens lange arm", "Kokk", "Idrett"],
        "stjernetegn": ["Væren", "Tyren", "Tvillingene", "Krepsen", "Løven", "Jomfruen", "Vekten", "Skorpionen", "Skytten", "Stenbukken", "Vannmannen", "Fiskene"],
        "mal": ["Romanse (Romance)", "Kunnskap (Knowledge)", "Familie (Family)", "Formue (Fortune)", "Popularitet (Popularity)"]
    },
    "Sims 1 (Retro/Original)": {
        "trekk_type": "trekk",
        "har_ung_voksen": False,
        "kan_studere": False,
        "husdyr": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr (Fugl / Iguana) 🐹"],
        "dyre_trekk": ["Stuegris 🐷", "Høytlytt 📢", "Destruktiv 💥", "Kosete ❤️", "Uavhengig 🐾", "Kranglevoren 😾"],
        "okkulte": [
            "Magiker / Trollmann 🧙‍♂️ (Sims 1: Makin' Magic)", 
            "Ghoul / Spøkelse 👻 (Sims 1: Livin' Large)", 
            "Mime / Klovn 🤡 (Sims 1: Base/Expansion)"
        ],
        "karrierer": ["Forretningsliv", "Mote", "Musikk", "Politiet", "Militæret", "Medisin", "Ekstremt", "Arbeidsledig / Drifter"],
        "trekk": ["Panisk for brann", "Avhengig av pizza", "Kranglevoren", "Evig uheldig", "Gjerrig", "Stuegris", "Tvangsmessig rydder"],
        "mal": ["Bli rik nok til et basseng uten stige", "Overleve spøkelsene i huset", "Få naboene til å like deg", "Kjøpe en magisk dverg", "Unngå marsvin-syken"]
    }
}

barn_aldre = ["Baby", "Småbarn (Toddler)", "Barn", "Tenåring"]

# --- SIDESTOLPE (INNSTILLINGER) ---
st.sidebar.header("⚙️ Konfigurasjon")
valgt_spill = st.sidebar.selectbox("Velg Sims-versjon:", list(spill_database.keys()))
valgt_modus = st.sidebar.radio("Modus:", ["Enkeltsim", "Familie (Dynamisk antall barn & alder)"])
valgt_spraak = st.sidebar.selectbox("Velg språk:", ["Begge", "Norsk", "Engelsk"])
valgt_kjonn = st.sidebar.selectbox("Velg kjønn:", ["Begge", "Gutt / Mann", "Jente / Kvinne"])
valgt_type = st.sidebar.selectbox("Velg navnetype:", ["Begge", "Normale", "Rare & gøye"])

# --- OKKULT & HUSDYR ---
st.sidebar.markdown("---")
er_okkult = st.sidebar.checkbox("🦇 Er okkult sim?", value=False)
valgt_okkult_type = None
if er_okkult:
    tilgjengelige_okkulte = spill_database[valgt_spill]["okkulte"]
    valgt_okkult_type = st.sidebar.selectbox("Velg okkult-type:", ["Tilfeldig okkult"] + tilgjengelige_okkulte)

legg_til_husdyr = st.sidebar.checkbox("🐾 Legg til husdyr (Pets)?", value=False)

full_random = st.sidebar.checkbox("🎲 Fullstendig tilfeldig", value=False)

def generer_personlighet(spill_navn):
    data = spill_database[spill_navn]
    if data["trekk_type"] == "poeng":
        tegn = random.choice(data["stjernetegn"])
        rotete = random.randint(1, 10)
        sjenert = random.randint(1, 10)
        lat = random.randint(1, 10)
        alvorlig = random.randint(1, 10)
        gjerrig = random.randint(1, 10)
        
        poeng_str = f"Stjernetegn: **{tegn}** | Rotete: {rotete}/10 | Sjenert: {sjenert}/10 | Lat: {lat}/10 | Alvorlig: {alvorlig}/10 | Gjerrig: {gjerrig}/10"
        mal = random.choice(data["mal"])
        return poeng_str, mal
    else:
        trekk = random.sample(data["trekk"], min(2, len(data["trekk"])))
        mal = random.choice(data["mal"])
        return f"{trekk[0]} og {trekk[1]}", mal

def hent_fornavn(kjonn_kode, er_ok, spraak):
    if er_ok:
        return random.choice(okkulte_fornavn)
    if spraak == "Norsk":
        if kjonn_kode == "Gutt":
            return random.choice(norske_guttenavn_normale if valgt_type != "Rare & gøye" else norske_guttenavn_rare)
        else:
            return random.choice(norske_jentenavn_normale if valgt_type != "Rare & gøye" else norske_jentenavn_rare)
    else:
        if kjonn_kode == "Gutt":
            return random.choice(engelske_guttenavn_normale if valgt_type != "Rare & gøye" else engelske_guttenavn_rare)
        else:
            return random.choice(engelske_jentenavn_normale if valgt_type != "Rare & gøye" else engelske_jentenavn_rare)

def hent_husdyr_tekst(spill):
    mulige_arter = spill_database[spill]["husdyr"]
    art = random.choice(mulige_arter)
    
    if "Hund" in art:
        dyre_navn = random.choice(hundehun_navn + hundehun_jente)
    elif "Katt" in art:
        dyre_navn = random.choice(katt_navn + katt_jente)
    elif "Hest" in art:
        dyre_navn = random.choice(hest_navn)
    else:
        dyre_navn = random.choice(lite_dyr_navn)
        
    mulige_dyre_trekk = spill_database[spill]["dyre_trekk"]
    trekk = random.choice(mulige_dyre_trekk)
    return f"🐾 **Husdyr:** {dyre_navn} ({art}) — *Trekk: {trekk}*"

def hent_enkelt_navn():
    if full_random:
        s = random.choice(["Norsk", "Engelsk"])
        k_kode = random.choice(["Gutt", "Jente"])
        lokal_okkult = random.choice([True, False])
    else:
        s = random.choice(["Norsk", "Engelsk"]) if valgt_spraak == "Begge" else valgt_spraak
        if valgt_kjonn == "Begge":
            k_kode = random.choice(["Gutt", "Jente"])
        elif valgt_kjonn == "Gutt / Mann":
            k_kode = "Gutt"
        else:
            k_kode = "Jente"
        lokal_okkult = er_okkult

    passende_okkulte = spill_database[valgt_spill]["okkulte"]

    if lokal_okkult:
        etter = random.choice(okkulte_etternavn)
        spraak_tekst = "Okkult / Overnaturlig"
        if valgt_okkult_type and valgt_okkult_type != "Tilfeldig okkult":
            valgt_o = valgt_okkult_type
        else:
            valgt_o = random.choice(passende_okkulte)
        stil_tekst = f"Okkult ({valgt_o})"
    else:
        etter = random.choice(etternavn_norske if s == "Norsk" else etternavn_engelske)
        spraak_tekst = s
        stil_tekst = "Normal" if valgt_type == "Normale" else ("Rare & gøy" if valgt_type == "Rare & gøye" else random.choice(["Normal", "Rare & gøy"]))

    fornavn = hent_fornavn(k_kode, lokal_okkult, s)
    personlighet, mal = generer_personlighet(valgt_spill)
    
    kan_ha_universitet = spill_database[valgt_spill]["kan_studere"]
    studie_info = ""
    er_paa_universitet = False
    
    if kan_ha_universitet and random.random() < 0.35:
        er_paa_universitet = True
        studie_info = f"🎓 Studerer på universitetet: **{random.choice(studieretninger)}**"
        relasjon = "Student 🎒"
    else:
        relasjon = random.choice(relasjonsstatuser)

    karriere_liste = spill_database[valgt_spill]["karrierer"]
    karriere = random.choice(karriere_liste) if not er_paa_universitet else "Fulltidsstudent 📚"

    if valgt_spill == "Sims 2 (Klassisk drama)":
        alder = "Ung voksen" if er_paa_universitet else random.choice(["Voksen", "Eldre"])
    elif valgt_spill == "Sims 1 (Retro/Original)":
        alder = random.choice(["Voksen", "Eldre"])
    else:
        if er_paa_universitet:
            alder = "Ung voksen"
        else:
            har_uv = spill_database[valgt_spill]["har_ung_voksen"]
            alder = random.choice(["Ung voksen", "Voksen", "Eldre"] if har_uv else ["Voksen", "Eldre"])

    kjonn_visning = "Mann / Gutt 👨" if k_kode == "Gutt" else "Kvinne / Jente 👩"

    return {
        "navn": f"{fornavn} {etter}",
        "kjonn": kjonn_visning,
        "spraak": spraak_tekst,
        "stil": stil_tekst,
        "alder": alder,
        "relasjon": relasjon,
        "karriere": karriere,
        "studie": studie_info,
        "personlighet": personlighet,
        "mal": mal
    }

# --- HOVEDDEL ---
if st.button("✨ Generer nytt!", type="primary", use_container_width=True):
    if valgt_modus == "Enkeltsim":
        sim = hent_enkelt_navn()
        resultat_tekst = f"### 🧑 {sim['navn']}\n* **Kjønn:** {sim['kjonn']}\n* **Alder:** {sim['alder']}\n* **Livssituasjon / Relasjon:** {sim['relasjon']}\n* **Karriere / Jobb:** {sim['karriere']}\n"
        if sim['studie']:
            resultat_tekst += f"* {sim['studie']}\n"
        resultat_tekst += f"* **Spill:** {valgt_spill}\n* **Stil/Språk:** {sim['spraak']} ({sim['stil']})\n* **Personlighet:** {sim['personlighet']}\n* **Livsmål/Ambisjon:** {sim['mal']}"
        
        if legg_til_husdyr:
            resultat_tekst += f"\n* {hent_husdyr_tekst(valgt_spill)}"

        st.success(resultat_tekst)
        st.session_state.historikk.insert(0, f"[{valgt_spill}] {sim['navn']} ({sim['kjonn']}, {sim['alder']})")
    else:
        s = random.choice(["Norsk", "Engelsk"]) if valgt_spraak == "Begge" else valgt_spraak
        passende_okkulte = spill_database[valgt_spill]["okkulte"]
        kan_ha_universitet = spill_database[valgt_spill]["kan_studere"]
        er_universitets_verden = kan_ha_universitet and random.random() < 0.25

        if er_okkult:
            felles_etter = random.choice(okkulte_etternavn)
            if valgt_okkult_type and valgt_okkult_type != "Tilfeldig okkult":
                fam_o_type = valgt_okkult_type
            else:
                fam_o_type = random.choice(passende_okkulte)
            familie_okkult_tekst = f" [{fam_o_type}]"
        else:
            felles_etter = random.choice(etternavn_norske if s == "Norsk" else etternavn_engelske)
            familie_okkult_tekst = ""

        antall_foreldre = random.choice([1, 2])
        foreldre_liste = []
        karriere_liste = spill_database[valgt_spill]["karrierer"]
        
        if er_universitets_verden:
            fam_status = "Universitetsstudenter / Kollektiv 🎓"
        elif antall_foreldre == 2:
            fam_status = "Gifte / Partnere 💍"
        else:
            fam_status = random.choice(["Alene-forelder 🧑‍👦", "Skilt / Delt omsorg ⚡"])

        for i in range(antall_foreldre):
            k_kode = random.choice(["Gutt", "Jente"])
            k_tekst = "Mann 👨" if k_kode == "Gutt" else "Kvinne 👩"
            fornavn = hent_fornavn(k_kode, er_okkult, s)
            
            if er_universitets_verden:
                alder = "Ung voksen"
                forelder_jobb = "Student 📚"
                forelder_studie = f" | 🎓 Studier: {random.choice(studieretninger)}"
            else:
                if valgt_spill == "Sims 2 (Klassisk drama)" or valgt_spill == "Sims 1 (Retro/Original)":
                    alder = random.choice(["Voksen", "Eldre"])
                else:
                    har_uv = spill_database[valgt_spill]["har_ung_voksen"]
                    alder = random.choice(["Ung voksen", "Voksen", "Eldre"] if har_uv else ["Voksen", "Eldre"])
                
                forelder_jobb = random.choice(karriere_liste)
                forelder_studie = ""
                if alder in ["Ung voksen", "Voksen"] and random.random() < 0.25:
                    forelder_studie = f" | 🎓 Studier: {random.choice(studieretninger)}"

            pers, _ = generer_personlighet(valgt_spill)
            foreldre_liste.append(f"**Forelder {i+1} [{k_tekst}] ({alder}):** {fornavn} {felles_etter} *(Jobb: {forelder_jobb} | {pers}{forelder_studie})*")

        if er_universitets_verden:
            antall_barn = 0
        else:
            antall_barn = random.randint(0, 4)

        barn_liste = []
        for i in range(antall_barn):
            k_kode = random.choice(["Gutt", "Jente"])
            k_tekst = "Gutt 👦" if k_kode == "Gutt" else "Jente 👧"
            fornavn = hent_fornavn(k_kode, er_okkult, s)
            alder = random.choice(barn_aldre)
            pers, mal = generer_personlighet(valgt_spill)
            barn_liste.append(f"**Barn {i+1} [{k_tekst}] ({alder}):** {fornavn} {felles_etter} *({pers} — Mål: {mal})*")

        fam_tekst = f"### 👨‍👩‍👧‍👦 Familie {felles_etter}{familie_okkult_tekst} ({valgt_spill})\n"
        fam_tekst += f"* **Familie-status:** {fam_status}\n\n"
        fam_tekst += "\n".join(foreldre_liste) + "\n\n"
        
        if barn_liste:
            fam_tekst += "**Barn inngår i husholdningen:**\n" + "\n".join(barn_liste) + "\n\n"
        else:
            if er_universitets_verden and valgt_spill == "Sims 2 (Klassisk drama)":
                fam_tekst += "*Ingen barn her (Sims 2-universitetet tillater ikke barn i studenthusholdninger).* \n\n"
            else:
                fam_tekst += "*Ingen barn i denne husholdningen ennå.*\n\n"

        if legg_til_husdyr:
            fam_tekst += f"**Husdyr i husholdningen:**\n* {hent_husdyr_tekst(valgt_spill)}"

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
