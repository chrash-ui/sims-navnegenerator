import random
import streamlit as st

st.set_page_config(page_title="Ultimate Sims Navnegenerator", page_icon="🎮", layout="wide")

# ==========================================
# INITIALISERING AV SESSION STATE (LAGRING)
# ==========================================
if "historikk" not in st.session_state:
    st.session_state.historikk = []
if "favoritter" not in st.session_state:
    st.session_state.favoritter = []

# ==========================================
# NAVNEDATABASE
# ==========================================
NAVNE_DB = {
    "Norsk": {
        "guttenavn": ["Lucas", "Oliver", "Filip", "Emil", "Magnus", "Håkon", "Henrik", "Jonas", "Sander", "Jakob", "Aksel", "Sivert", "Birk", "Sigurd", "Trygve", "Tormod"],
        "jentenavn": ["Emma", "Nora", "Olivia", "Ella", "Sofie", "Astrid", "Ingrid", "Signe", "Tiril", "Thea", "Amalie", "Hedda", "Ronja", "Ylva", "Oda", "Frida"],
        "etternavn": ["Hansen", "Johansen", "Olsen", "Pedersen", "Nilsen", "Berg", "Haugen", "Solheim", "Strand", "Fjell", "Ødegaard", "Nygård", "Sandvik", "Bjerke"]
    },
    "Svensk": {
        "guttenavn": ["Liam", "William", "Hugo", "Noah", "Oliver", "Elias", "Arvid", "Ludvig", "Nils", "Sven", "Björn", "Lars", "Gustav", "Frej"],
        "jentenavn": ["Alice", "Maja", "Elsa", "Astrid", "Wilma", "Freja", "Ebba", "Saga", "Agnes", "Elin", "Ida", "Linnéa", "Lovisa", "Tove"],
        "etternavn": ["Andersson", "Johansson", "Karlsson", "Nilsson", "Eriksson", "Larsson", "Olsson", "Persson", "Svensson", "Lindberg", "Lindqvist"]
    },
    "Dansk": {
        "guttenavn": ["Noah", "Carl", "Lukas", "Oscar", "Alfred", "Oliver", "Valdemar", "Malthe", "Emil", "Frederik", "Søren", "Mads", "Lasse"],
        "jentenavn": ["Alma", "Ida", "Clara", "Ella", "Freja", "Emma", "Sofia", "Agnes", "Laura", "Mette", "Nanna", "Katrine", "Lærke"],
        "etternavn": ["Jensen", "Nielsen", "Hansen", "Pedersen", "Andersen", "Christensen", "Larsen", "Sørensen", "Rasmussen", "Jørgensen"]
    },
    "Engelsk / Amerikansk": {
        "guttenavn": ["Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Theodore", "Mason", "Ethan", "Caleb", "Wyatt"],
        "jentenavn": ["Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper", "Scarlett", "Grace", "Chloe", "Violet"],
        "etternavn": ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Taylor", "Anderson", "White", "Harris", "Martin"]
    },
    "Fransk": {
        "guttenavn": ["Gabriel", "Léo", "Raphaël", "Louis", "Arthur", "Jules", "Maël", "Lucas", "Adam", "Hugo", "Édouard", "Henri", "Pierre"],
        "jentenavn": ["Jade", "Louise", "Emma", "Ambre", "Alice", "Rose", "Anna", "Chloé", "Mia", "Léa", "Camille", "Manon", "Céleste"],
        "etternavn": ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent", "Fontaine"]
    },
    "Italiensk": {
        "guttenavn": ["Leonardo", "Francesco", "Tommaso", "Edoardo", "Alessandro", "Lorenzo", "Mattia", "Gabriele", "Riccardo", "Matteo", "Giovanni"],
        "jentenavn": ["Sofia", "Aurora", "Giulia", "Ginevra", "Beatrice", "Alice", "Vittoria", "Emma", "Ludovica", "Matilde", "Francesca"],
        "etternavn": ["Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco", "Bruno"]
    },
    "Spansk": {
        "guttenavn": ["Hugo", "Mateo", "Martin", "Lucas", "Leo", "Daniel", "Alejandro", "Manuel", "Pablo", "Álvaro", "Carlos", "Diego"],
        "jentenavn": ["Lucía", "Sofía", "Martina", "María", "Julia", "Paula", "Valeria", "Emma", "Daniela", "Carla", "Alba", "Carmen"],
        "etternavn": ["García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Torres"]
    },
    "Tysk": {
        "guttenavn": ["Noah", "Matteo", "Finn", "Leon", "Elias", "Paul", "Ben", "Luca", "Emil", "Louis", "Felix", "Maximilian", "Otto"],
        "jentenavn": ["Emilia", "Mia", "Sophia", "Emma", "Hannah", "Lina", "Mila", "Ella", "Leni", "Clara", "Greta", "Johanna"],
        "etternavn": ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann"]
    },
    "Japansk": {
        "guttenavn": ["Ren", "Haruto", "Minato", "Yuma", "Sota", "Kenji", "Hiroshi", "Takumi", "Kaito", "Daiki", "Ryota"],
        "jentenavn": ["Himari", "Hina", "Yua", "Sakura", "Akari", "Mei", "Aoi", "Rin", "Kiko", "Yoko", "Hana"],
        "etternavn": ["Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Ito", "Yamamoto", "Nakamura", "Kobayashi", "Kato"]
    },
    "Koreansk": {
        "guttenavn": ["Seojun", "Ha-joon", "Do-yun", "Eun-woo", "Ji-ho", "Min-jun", "Yu-jun", "Jung-woo", "Hyun", "Seok"],
        "jentenavn": ["Ji-an", "Ha-rin", "Seo-ah", "Seo-yun", "Ji-woo", "Min-seo", "Ha-eun", "Yuna", "Soo-jin", "Chae-won"],
        "etternavn": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang", "Cho", "Yoon", "Jang", "Lim"]
    },
    "Fantasy & Magisk": {
        "guttenavn": ["Vladislaus", "Malakor", "Zephyr", "Astaroth", "Lucifer", "Asmodeus", "Mortis", "Oberon", "Thorne", "Ignis", "Solomon"],
        "jentenavn": ["Lilith", "Raven", "Vespera", "Pandora", "Nyx", "Titania", "Hexia", "Hecate", "Vampira", "Belladonna", "Morgana"],
        "etternavn": ["Bloodworth", "Nightshade", "Grimwood", "Blackwood", "Cryptic", "Shadowfen", "Spellbinder", "Moonstone", "Silverfang", "Wormwood"]
    },
    "Gøye, Kaos & Morsomme": {
        "guttenavn": ["Bjarne", "Banan", "Kevin", "Ronny", "Tøffel", "Kåre", "Preben", "Guttorm", "Skinke", "Pølse", "Svein-Diva"],
        "jentenavn": ["Berit", "Diva", "Trude", "Bella", "Gunda", "Gull-Laila", "Kjeks", "Doris", "Søt", "Snusken"],
        "etternavn": ["Bråkmaker", "Kaos", "Drama", "Rømme", "Bling", "Trøbbel", "Pengepung", "Knall", "Pumpernickel", "Snodgrass", "Wigglesworth"]
    },
    "Gammeldags & Klassisk": {
        "guttenavn": ["Archibald", "Bartholomew", "Cornelius", "Ebenezer", "Giles", "Horace", "Ignatius", "Montgomery", "Percival", "Thaddeus"],
        "jentenavn": ["Agatha", "Beatrice", "Cressida", "Gertrude", "Hortense", "Maude", "Mildred", "Prudence", "Tabitha", "Wilhelmina"],
        "etternavn": ["Butterworth", "Fairchild", "Halloway", "Pemberton", "Pettibone", "Sterling", "Wellington", "Winterbottom"]
    }
}

# --- DYRENAVN OG TREKK ---
DYRENAVN = {
    "Hund": ["Buster", "Karo", "Rex", "Balder", "Bruno", "Rambo", "Theo", "Bamse", "Charlie", "Rocky", "Bella", "Luna", "Ayla", "Daisy"],
    "Katt": ["Pusur", "Milling", "Fjonken", "Felix", "Socks", "Tiger", "Simba", "Oliver", "Missen", "Nala", "Cleo", "Sassy"],
    "Hest": ["Storm", "Faksen", "Spirit", "Gorm", "Thunder", "Cinderella", "Varg", "Dronning", "Blakken", "Star"],
    "Smådyr": ["Pip", "Squeak", "Nøtteliten", "Gnagern", "Smule", "Pompel", "Pilt", "Snickers", "Peanut"]
}
DYRE_TREKK = ["Leken 🎾", "Lat 😴", "Aggressiv 💢", "Kosete ❤️", "Uavhengig 🐾", "Fryktsom 💨", "Nysgjerrig 🔍"]

# --- SPILLSPESIFIKKE DATA ---
spill_database = {
    "Sims 4 (Moderne)": {
        "trekk_type": "trekk",
        "har_ung_voksen": True,
        "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Hest 🐴 (Horse Ranch)", "Lite kjæledyr (Gnager/Fugl) 🐹"],
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
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Hest 🐴 (Sims 3: Pets)", "Lite kjæledyr (Fugl/Krypdyr/Gnager) 🐹"],
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
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr (Fugl / Marsvin) 🐹"],
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
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr (Fugl / Iguana) 🐹"],
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

# --- HISTORIE-ELEMENTER FOR BIO ---
hvordan_mottets = [
    "møttes ved et uhell da begge prøvde å ta den siste grillede osten i et nabolagsselskap",
    "møttes på biblioteket mens de lette etter den samme støvete trylleformelboken",
    "ble kjent etter at den ene krasjet en fest i nabohuset uten å være invitert",
    "møttes på universitetsområdet etter å ha forbyttet ryggsekker under fadderuka",
    "møttes på det lokale loppemarkedet mens de kranglet om en magisk dvergstatue",
    "ble ført sammen av en tilfeldig lynnedslagsepisode ved det offentlige bassenget"
]

rare_hendelser_enkelt = [
    "Presterte engang å brenne ned hele kjøkkenet mens vedkommende prøvde å smøre en brødskive.",
    "Ble en gang bortført av romvesener mitt på natten, og kom tilbake med en ubendig trang til å lære sjakk.",
    "Har en hemmelig vane med å snakke med hagegnomer når ingen andre ser på.",
    "Ble en gang låst inne i et rom fordi noen glemte å bygge en dør.",
    "Er overbevist om at huset deres er besøkt av et spøkelse som konstant flytter på tøflene.",
    "Kjøpte en gang 40 marsvin på én dag og måtte bygge et eget rom til dem."
]

rare_hendelser_fam = [
    "Hele familien ble en gang kastet ut av den lokale parken etter at barna prøvde å selge usynlig saft.",
    "Foreldrene har en intern avtale om å aldri snakke om den gangen de kom til å fjerne stigen fra bassenget mens naboen svømte.",
    "Huset deres lukter kanskje konstant av brent pizza, men sammen holder de humøret oppe uansett.",
    "Det ryktes i nabolaget at familien har gjemt en skatt under rådhuset, men ingen tør å spørre dem.",
    "Familien har en ubrytelig tradisjon om å danse panisk hver gang det begynner å regne."
]

dynamikk_liste = [
    "Familien kjennetegnes av høyt konfliktnivå ved middagsbordet, men de stiller alltid opp for hverandre når det gjelder.",
    "Husholdningen er preget av kaos og kreativt rot, hvor alle gjør akkurat som de selv vil.",
    "Dette er en svært ambisiøs og strukturert familie som planlegger hver minste detalj av hverdagen.",
    "En rolig og harmonisk husholdning hvor hovedfokuset er å nyte livet og ta ting som det kommer."
]

relasjonsstatuser = [
    "Singel 💔", 
    "Gift 💍", 
    "Forlovet 💎", 
    "Skilt ⚡", 
    "Det er komplisert... 🎭"
]

studieretninger = ["Biologi 🧬", "Drama & Teater 🎭", "Medisin 🩺", "Fysikk & Vitenskap 🔬", "Kunst & Design 🎨", "Historie & Litteratur 📚", "Juss & Politikk ⚖️", "Bedriftsøkonomi 💼"]

# ==========================================
# SIDESTOLPE
# ==========================================
st.sidebar.header("⚙️ Konfigurasjon")
valgt_fane = st.sidebar.radio("Verktøy:", [
    "🎲 Generer Sim / Familie", 
    "👯 Tvillinger & Slektskap", 
    "🐾 Kjæledyr-generator", 
    "⭐ Favoritter", 
    "📜 Historikk"
])

st.sidebar.markdown("---")
valgt_spill = st.sidebar.selectbox("Velg Sims-versjon:", list(spill_database.keys()))
valgt_kategori = st.sidebar.selectbox("Navnekategori / Nasjonalitet:", list(NAVNE_DB.keys()))
valgt_kjonn = st.sidebar.selectbox("Velg kjønn:", ["Begge / Unisex", "Gutt / Mann", "Jente / Kvinne"])

# --- OKKULT & HUSDYR & ØKONOMI ---
st.sidebar.markdown("---")
er_okkult = st.sidebar.checkbox("🦇 Er okkult sim?", value=False)
valgt_okkult_type = None
if er_okkult:
    tilgjengelige_okkulte = spill_database[valgt_spill]["okkulte"]
    valgt_okkult_type = st.sidebar.selectbox("Velg okkult-type:", ["Tilfeldig okkult"] + tilgjengelige_okkulte)

legg_til_husdyr = st.sidebar.checkbox("🐾 Legg til husdyr (Pets)?", value=False)
valgt_dyreart = "🎲 Tilfeldig dyr"
if legg_til_husdyr:
    tilgjengelige_dyr = spill_database[valgt_spill]["husdyr_mulige"]
    valgt_dyreart = st.sidebar.selectbox("Velg dyreart:", ["🎲 Tilfeldig dyr"] + tilgjengelige_dyr)

legg_til_okonomi = st.sidebar.checkbox("💰 Inkluder startøkonomi (§)?", value=True)

# ==========================================
# HJELPEFUNKSJONER
# ==========================================
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

def hent_navn_komplett(kategori, kjonn_kode, er_ok):
    if er_ok:
        fornavn = random.choice(NAVNE_DB["Fantasy & Magisk"]["guttenavn"] + NAVNE_DB["Fantasy & Magisk"]["jentenavn"])
        etternavn = random.choice(["Bloodworth", "Nightshade", "Grimwood", "Blackwood", "Cryptic", "Graves"])
        return fornavn, etternavn
        
    data = NAVNE_DB.get(kategori, NAVNE_DB["Norsk"])
    if kjonn_kode == "Gutt / Mann":
        fornavn = random.choice(data["guttenavn"])
    elif kjonn_kode == "Jente / Kvinne":
        fornavn = random.choice(data["jentenavn"])
    else:
        fornavn = random.choice(data["guttenavn"] + data["jentenavn"])
    etternavn = random.choice(data["etternavn"])
    return fornavn, etternavn

def hent_husdyr_tekst(spill, valgt_art):
    mulige_arter = spill_database[spill]["husdyr_mulige"]
    if valgt_art == "🎲 Tilfeldig dyr":
        art = random.choice(mulige_arter)
    else:
        art = valgt_art
    
    if "Hund" in art:
        dyre_navn = random.choice(DYRENAVN["Hund"])
    elif "Katt" in art:
        dyre_navn = random.choice(DYRENAVN["Katt"])
    elif "Hest" in art:
        dyre_navn = random.choice(DYRENAVN["Hest"])
    else:
        dyre_navn = random.choice(DYRENAVN["Smådyr"])
        
    trekk = random.choice(DYRE_TREKK)
    return f"🐾 Husdyr: {dyre_navn} ({art}) — Trekk: {trekk}"

def hent_okonomi(antall_personer):
    base_sum = 20000
    tillegg = (antall_personer - 1) * 5000
    tilfeldig_ekstra = random.randint(0, 10) * 1000
    totalt = base_sum + tillegg + tilfeldig_ekstra
    return f"§{totalt:,}".replace(",", " ")

# ==========================================
# HOVEDDEL / FANER
# ==========================================
if valgt_fane == "🎲 Generer Sim / Familie":
    st.title("🎮 Ultimate Sims Navnegenerator")
    st.write("Skap din neste sim eller familie med spilltrofaste aldersregler, kjæledyr, karrierer og bakgrunnshistorie!")
    
    modus = st.radio("Modus:", ["Enkeltsim", "Familie (Dynamisk antall barn & alder)"], horizontal=True)

    if st.button("✨ Generer nytt!", type="primary", use_container_width=True):
        if modus == "Enkeltsim":
            k_kode = valgt_kjonn
            fn, en = hent_navn_komplett(valgt_kategori, k_kode, er_okkult)
            personlighet, mal = generer_personlighet(valgt_spill)
            
            kan_ha_universitet = spill_database[valgt_spill]["kan_studere"]
            studie_info = ""
            er_paa_universitet = False
            
            if kan_ha_universitet and random.random() < 0.35:
                er_paa_universitet = True
                studie_info = f"🎓 Studerer på universitetet: {random.choice(studieretninger)}"
                relasjon = "Student 🎒"
            else:
                relasjon = random.choice(relasjonsstatuser)

            karriere_liste = spill_database[valgt_spill]["karrierer"]
            karriere = random.choice(karriere_liste) if not er_paa_universitet else "Fulltidsstudent 📚"

            # Aldersregler basert på spill
            if valgt_spill == "Sims 1 (Retro/Original)":
                alder = "Voksen"
            elif valgt_spill == "Sims 2 (Klassisk drama)":
                alder = "Ung voksen" if er_paa_universitet else random.choice(["Voksen", "Eldre"])
            else:
                if er_paa_universitet:
                    alder = "Ung voksen"
                else:
                    har_uv = spill_database[valgt_spill]["har_ung_voksen"]
                    alder = random.choice(["Ung voksen", "Voksen", "Eldre"] if har_uv else ["Voksen", "Eldre"])

            kjonn_visning = "Mann / Gutt 👨" if k_kode == "Gutt / Mann" else ("Kvinne / Jente 👩" if k_kode == "Jente / Kvinne" else random.choice(["Mann / Gutt 👨", "Kvinne / Jente 👩"]))
            budsjett = hent_okonomi(1) if legg_til_okonomi else None
            fullt_navn = f"{fn} {en}"

            sart_hendelse = random.choice(rare_hendelser_enkelt)
            historie_bio = f"{fullt_navn} lever et innholdsrikt liv som {alder.lower()}. "
            historie_bio += f"Arbeider for tiden som {karriere}. "
            historie_bio += f"Hovedmålet i livet er å: '{mal}'.\n\n"
            historie_bio += f"Sært trekk / hendelse fra fortiden:\n- {sart_hendelse}"
            
            if legg_til_husdyr:
                husdyr_tekst_streng = hent_husdyr_tekst(valgt_spill, valgt_dyreart)
                historie_bio += f"\n\nBor sammen med et kjæledyr: {husdyr_tekst_streng}"

            resultat_tekst = f"### 🧑 {fullt_navn}\n* **Kjønn:** {kjonn_visning}\n* **Alder:** {alder}\n* **Livssituasjon / Relasjon:** {relasjon}\n* **Karriere / Jobb:** {karriere}\n"
            if studie_info:
                resultat_tekst += f"* {studie_info}\n"
            if budsjett:
                resultat_tekst += f"* **Startbudsjett:** {budsjett}\n"
            resultat_tekst += f"* **Spill:** {valgt_spill}\n* **Personlighet:** {personlighet}\n* **Livsmål/Ambisjon:** {mal}"
            
            if legg_til_husdyr:
                resultat_tekst += f"\n* {hent_husdyr_tekst(valgt_spill, valgt_dyreart)}"

            st.success(resultat_tekst)
            
            st.markdown("### 📖 Bakgrunnshistorie & Bio")
            st.text_area("Bruk knappen øverst til høyre i boksen for å kopiere bioen:", historie_bio, height=200)

            st.session_state.historikk.insert(0, f"[{valgt_spill}] {fullt_navn} ({alder})")

            if st.button("⭐ Lagre som favoritt"):
                st.session_state.favoritter.append(fullt_navn)
                st.success(f"{fullt_navn} er lagret i favoritter!")

        else:
            passende_okkulte = spill_database[valgt_spill]["okkulte"]
            kan_ha_universitet = spill_database[valgt_spill]["kan_studere"]
            er_universitets_verden = kan_ha_universitet and random.random() < 0.25

            if er_okkult:
                felles_etter = random.choice(["Bloodworth", "Nightshade", "Grimwood", "Blackwood", "Cryptic", "Graves"])
                fam_o_type = valgt_okkult_type if valgt_okkult_type and valgt_okkult_type != "Tilfeldig okkult" else random.choice(passende_okkulte)
                familie_okkult_tekst = f" [{fam_o_type}]"
            else:
                data_kat = NAVNE_DB.get(valgt_kategori, NAVNE_DB["Norsk"])
                felles_etter = random.choice(data_kat["etternavn"])
                familie_okkult_tekst = ""

            antall_foreldre = random.choice([1, 2])
            foreldre_liste = []
            foreldre_navn_kun = []
            karriere_liste = spill_database[valgt_spill]["karrierer"]
            
            if er_universitets_verden:
                fam_status = "Universitetsstudenter / Kollektiv 🎓"
            elif antall_foreldre == 2:
                fam_status = "Gifte / Partnere 💍"
            else:
                fam_status = random.choice(["Alene-forelder 🧑‍👦", "Skilt / Delt omsorg ⚡"])

            for i in range(antall_foreldre):
                k_kode = valgt_kjonn if valgt_kjonn != "Begge / Unisex" else random.choice(["Gutt / Mann", "Jente / Kvinne"])
                k_tekst = "Mann 👨" if k_kode == "Gutt / Mann" else "Kvinne 👩"
                fornavn, _ = hent_navn_komplett(valgt_kategori, k_kode, er_okkult)
                foreldre_navn_kun.append(fornavn)
                
                if er_universitets_verden:
                    alder = "Ung voksen"
                    forelder_jobb = "Student 📚"
                    forelder_studie = f" | 🎓 Studier: {random.choice(studieretninger)}"
                else:
                    if valgt_spill == "Sims 1 (Retro/Original)":
                        alder = "Voksen"
                    elif valgt_spill == "Sims 2 (Klassisk drama)":
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

            totalt_medlemmer = antall_foreldre + antall_barn
            budsjett = hent_okonomi(totalt_medlemmer) if legg_til_okonomi else None

            barn_liste = []
            for i in range(antall_barn):
                k_kode = random.choice(["Gutt / Mann", "Jente / Kvinne"])
                k_tekst = "Gutt 👦" if k_kode == "Gutt / Mann" else "Jente 👧"
                fornavn, _ = hent_navn_komplett(valgt_kategori, k_kode, er_okkult)
                
                if valgt_spill == "Sims 1 (Retro/Original)":
                    alder = "Barn"
                else:
                    alder = random.choice(barn_aldre)
                    
                pers, mal = generer_personlighet(valgt_spill)
                barn_liste.append(f"**Barn {i+1} [{k_tekst}] ({alder}):** {fornavn} {felles_etter} *({pers} — Mål: {mal})*")

            mote_historie = f"De voksne i husholdningen ({' og '.join(foreldre_navn_kun)}) {random.choice(hvordan_mottets)}." if antall_foreldre > 1 else f"{foreldre_navn_kun[0]} starter et nytt kapittel på egenhånd."
            fam_dynamikk = random.choice(dynamikk_liste)
            fam_sært = random.choice(rare_hendelser_fam)
            
            bio_tekst = f"=== FAMILIE-HISTORIE: FAMILIE {felles_etter.upper()} ({valgt_spill}) ===\n"
            bio_tekst += f"Status: {fam_status}\n"
            if budsjett:
                bio_tekst += f"Startøkonomi: {budsjett}\n"
            bio_tekst += f"\nHvordan de fant sammen / Bakgrunn:\n{mote_historie}\n\n"
            bio_tekst += f"Familiedynamikk:\n{fam_dynamikk}\n\n"
            bio_tekst += f"Sær hendelse i familiens fortid:\n{fam_sært}\n"
            
            if legg_til_husdyr:
                husdyr_tekst_streng = hent_husdyr_tekst(valgt_spill, valgt_dyreart)
                bio_tekst += f"\nHusdyr i familien: {husdyr_tekst_streng}\n"

            fam_tekst = f"### 👨‍👩‍👧‍👦 Familie {felles_etter}{familie_okkult_tekst} ({valgt_spill})\n"
            fam_tekst += f"* **Familie-status:** {fam_status}\n"
            if budsjett:
                fam_tekst += f"* **Startbudsjett:** {budsjett}\n"
            fam_tekst += "\n" + "\n".join(foreldre_liste) + "\n\n"
            
            if barn_liste:
                fam_tekst += "**Barn inngår i husholdningen:**\n" + "\n".join(barn_liste) + "\n\n"
            else:
                if er_universitets_verden and valgt_spill == "Sims 2 (Klassisk drama)":
                    fam_tekst += "*Ingen barn her (Sims 2-universitetet tillater ikke barn i studenthusholdninger).* \n\n"
                else:
                    fam_tekst += "*Ingen barn i denne husholdningen ennå.*\n\n"

            if legg_til_husdyr:
                fam_tekst += f"**Husdyr i husholdningen:**\n* {hent_husdyr_tekst(valgt_spill, valgt_dyreart)}"

            st.success(fam_tekst)
            
            st.markdown("### 📖 Bakgrunnshistorie & Bio")
            st.text_area("Bruk knappen øverst til høyre i boksen for å kopiere familiehistorien:", bio_tekst, height=260)

            st.session_state.historikk.insert(0, f"[{valgt_spill}] Familie {felles_etter} ({antall_foreldre} voksne, {antall_barn} barn)")

elif valgt_fane == "👯 Tvillinger & Slektskap":
    st.header("👯 Tvillinger & Matchende Navn")
    st.write("Generer navn med bokstavrim (alliterasjon) eller matchende tema for tvillinger/trillinger!")
    
    type_par = st.radio("Velg type:", ["Tvillinger (2)", "Trillinger (3)"])
    match_bokstav = st.checkbox("Tving samme startbokstav (Bokstavrim)", value=True)

    if st.button("✨ Generer Matchende Navn"):
        data = NAVNE_DB[valgt_kategori]
        alle_navn = data["guttenavn"] + data["jentenavn"]
        _, etternavn = hent_navn_komplett(valgt_kategori, "Begge / Unisex", False)

        if match_bokstav:
            bokstav = random.choice(list(set([n[0] for n in alle_navn])))
            filtrerte = [n for n in alle_navn if n.startswith(bokstav)]
            if len(filtrerte) < (2 if "Tvillinger" in type_par else 3):
                filtrerte = alle_navn
        else:
            filtrerte = alle_navn

        antall_trekk = 2 if "Tvillinger" in type_par else 3
        valgte = random.sample(filtrerte, antall_trekk)
        
        st.subheader(f"👶 {type_par} - Familie {etternavn}")
        for v in valgte:
            st.write(f"* **{v} {etternavn}**")

elif valgt_fane == "🐾 Kjæledyr-generator":
    st.header("🐾 Kjæledyr Navnegenerator")
    valgt_dyr_fane = st.selectbox("Velg dyreart:", ["🎲 Tilfeldig dyr"] + spill_database[valgt_spill]["husdyr_mulige"])
    
    if st.button("🐾 Generer Kjæledyrnavn"):
        resultat_dyr = hent_husdyr_tekst(valgt_spill, valgt_dyr_fane)
        st.success(resultat_dyr)

elif valgt_fane == "⭐ Favoritter":
    st.header("⭐ Lagrede Favoritter")
    if not st.session_state.favoritter:
        st.info("Ingen favoritter er lagret ennå. Klikk på '⭐ Lagre som favoritt' når du genererer en enkeltsim!")
    else:
        st.write("Dine favorittnavn:")
        for idx, fav in enumerate(st.session_state.favoritter):
            col1, col2 = st.columns([4, 1])
            col1.write(f"**{idx+1}. {fav}**")
            if col2.button("❌ Fjern", key=f"del_{idx}"):
                st.session_state.favoritter.pop(idx)
                st.rerun()

        st.markdown("---")
        fav_tekst = "\n".join(st.session_state.favoritter)
        st.text_area("📋 Kopier alle favoritter:", fav_tekst, height=150)
        st.download_button("💾 Last ned favoritter som tekstfil", fav_tekst, file_name="sims_favoritter.txt")

elif valgt_fane == "📜 Historikk":
    st.header("📜 Genereringshistorikk")
    if not st.session_state.historikk:
        st.info("Ingen historikk ennå.")
    else:
        for item in st.session_state.historikk[:20]:
            st.write(f"* {item}")

        if st.button("🗑️ Tøm Historikk"):
            st.session_state.historikk = []
            st.rerun()
