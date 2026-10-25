import random
import streamlit as st

st.set_page_config(page_title="Sims 4 & Retro Navnegenerator", page_icon="🟢", layout="wide")

# ==========================================
# INITIALISERING AV SESSION STATE (LAGRING)
# ==========================================
if "historikk" not in st.session_state:
    st.session_state.historikk = []
if "favoritter" not in st.session_state:
    st.session_state.favoritter = []

# ==========================================
# NAVNEDATABASE (FLERE KATEGORIER OG NORDISK/INTERNASJONALT)
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

# --- DYRENAVN ---
DYRENAVN = {
    "Hund": ["Buster", "Karo", "Rex", "Balder", "Bruno", "Rambo", "Theo", "Bamse", "Charlie", "Rocky", "Bella", "Luna", "Ayla", "Daisy"],
    "Katt": ["Pusur", "Milling", "Fjonken", "Felix", "Socks", "Tiger", "Simba", "Oliver", "Missen", "Nala", "Cleo", "Sassy"],
    "Hest": ["Storm", "Faksen", "Spirit", "Gorm", "Thunder", "Cinderella", "Varg", "Dronning", "Blakken", "Star"],
    "Smådyr": ["Pip", "Squeak", "Nøtteliten", "Gnagern", "Smule", "Pompel", "Pilt", "Snickers", "Peanut"]
}

# --- SPILLSPESIFIKKE DATA ---
SPILL_DB = {
    "Sims 4 (Moderne)": {
        "kan_studere": True, "har_uv": True,
        "husdyr": ["Hund 🐶", "Katt 🐱", "Hest 🐴 (Horse Ranch)", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Trollmann 🪄", "Romvesen 👽", "Varulv 🐺", "Havfrue 🧜‍♀️", "PlantSim 🌱"],
        "karrierer": ["Astronaut", "Kokk", "Kriminell", "Forretningsmann", "Underholder", "Forfatter", "Idrettsutøver", "Stilist", "Forsker"],
        "trekk": ["Klossete", "Hissig", "Kreativ", "Lat", "Geni", "Matvrak", "Romantisk", "Sjenert", "Overambisiøs"],
        "mal": ["Bli superkjendis", "Mestre matlaging", "Finne sann kjærlighet", "Kjøpe drømmehuset"]
    },
    "Sims 3 (Åpen verden)": {
        "kan_studere": True, "har_uv": True,
        "husdyr": ["Hund 🐶", "Katt 🐱", "Hest 🐴", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Heks 🪄", "Romvesen 👽", "Varulv 🐺", "Fe 🧚", "Zombie 🧟", "Genie 🧞"],
        "karrierer": ["Arkitekt", "Spøkelsesjeger", "Privatetterforsker", "Musiker", "Politiet", "Medisin", "Politiker", "Journalistikk"],
        "trekk": ["Samler", "Overfladisk", "Pyroman", "Håpløs romantiker", "Eksentrisk", "Besserwisser", "Drømmende"],
        "mal": ["Oppfylle en livslang drøm", "Lære alle ferdigheter", "Eie hele byen", "Se spøkelser i mausoleet"]
    },
    "Sims 2 (Klassisk drama)": {
        "kan_studere": True, "har_uv": False,
        "husdyr": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Zombie 🧟", "PlantSim 🌱", "Servobot 🤖", "Heks 🪄"],
        "karrierer": ["Leker (Toymaking)", "Showbusiness", "Paranormal", "Nattevakt", "Politiet", "Medisin", "Militæret"],
        "stjernetegn": ["Væren", "Tyren", "Tvillingene", "Krepsen", "Løven", "Jomfruen", "Vekten", "Skorpionen", "Skytten", "Stenbukken", "Vannmannen", "Fiskene"],
        "mal": ["Romanse", "Kunnskap", "Familie", "Formue", "Popularitet"]
    },
    "Sims 1 (Retro/Original)": {
        "kan_studere": False, "har_uv": False,
        "husdyr": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Magiker 🧙‍♂️", "Spøkelse 👻", "Mime/Klovn 🤡"],
        "karrierer": ["Forretningsliv", "Mote", "Musikk", "Politiet", "Militæret", "Medisin", "Arbeidsledig"],
        "trekk": ["Panisk for brann", "Avhengig av pizza", "Kranglevoren", "Evig uheldig", "Gjerrig", "Stuegris"],
        "mal": ["Bli rik nok til et basseng uten stige", "Overleve spøkelsene", "Få naboene til å like deg", "Kjøpe en magisk dverg"]
    }
}

UTFORDINGER = [
    "🏆 **100 Baby Challenge**: Start med én alene-mamma og fød 100 barn over flest mulig generasjoner uten jobb!",
    "🧱 **Rags to Riches**: Start på en tom tomt med §0. Du kan ikke ta en vanlig jobb før du har bygd et fullverdig hus.",
    "👑 **Legacy Challenge**: Spill gjennom 10 generasjoner i samme familie på samme hovedtomt med strenge arveregler.",
    "🎲 **Random Legacy**: La tilfeldighetene bestemme karriere, antall barn og marital status for hver generasjon.",
    "🦇 **Occult Master**: Få barn med hver eneste overnaturlige Sim-type (Vampyr, Varulv, Romvesen osv.) i samme slektstre."
]

# ==========================================
# HJELPEFUNKSJONER
# ==========================================
def hent_navn(kategori, kjonn):
    data = NAVNE_DB.get(kategori, NAVNE_DB["Norsk"])
    if kjonn == "Gutt / Mann":
        fornavn = random.choice(data["guttenavn"])
    elif kjonn == "Jente / Kvinne":
        fornavn = random.choice(data["jentenavn"])
    else:
        fornavn = random.choice(data["guttenavn"] + data["jentenavn"])
    etternavn = random.choice(data["etternavn"])
    return fornavn, etternavn

def generer_okonomi(antall):
    totalt = 20000 + (antall - 1) * 5000 + random.randint(0, 10) * 1000
    return f"§{totalt:,}".replace(",", " ")

# ==========================================
# SIDESTOLPE / MENY STYLING OG FILTERE
# ==========================================
st.sidebar.title("🟢 Sims Navnegenerator")
valgt_fane = st.sidebar.radio("Velg verktøy:", ["🎲 Generer Sim / Familie", "📑 Generer Mange (Batch 1-100)", "👯 Tvillinger & Slektskap", "🐾 Kjæledyr-generator", "⭐ Favoritter", "📜 Historikk", "🏆 Sims Utfordringer"])

st.sidebar.markdown("---")
valgt_spill = st.sidebar.selectbox("Spillversjon:", list(SPILL_DB.keys()))
valgt_kategori = st.sidebar.selectbox("Navnekategori / Nasjonalitet:", list(NAVNE_DB.keys()))
valgt_kjonn = st.sidebar.selectbox("Kjønn:", ["Begge / Unisex", "Gutt / Mann", "Jente / Kvinne"])
legg_til_okonomi = st.sidebar.checkbox("💰 Inkluder startøkonomi (§)?", value=True)

# ==========================================
# FANE 1: ENKELTSIM / FAMILIE
# ==========================================
if valgt_fane == "🎲 Generer Sim / Familie":
    st.header("✨ Generer Sim eller Husholdning")
    modus = st.radio("Modus:", ["Enkeltsim", "Familie / Husholdning"], horizontal=True)

    if st.button("🚀 Generer Nå!", type="primary", use_container_width=True):
        if modus == "Enkeltsim":
            fn, en = hent_navn(valgt_kategori, valgt_kjonn)
            
            # Spillspesifikke aldersregler
            if valgt_spill == "Sims 1 (Retro/Original)":
                alder = "Voksen"
            else:
                alder = random.choice(["Ung voksen", "Voksen", "Eldre"])

            karriere = random.choice(SPILL_DB[valgt_spill]["karrierer"])
            mal = random.choice(SPILL_DB[valgt_spill]["mal"])
            budsjett = generer_okonomi(1) if legg_til_okonomi else None
            
            fullt_navn = f"{fn} {en}"
            st.session_state.historikk.insert(0, f"[{valgt_spill}] {fullt_navn} ({alder})")

            st.subheader(f"👤 {fullt_navn}")
            st.write(f"**Alder:** {alder} | **Kategori:** {valgt_kategori} | **Karriere:** {karriere}")
            st.write(f"**Livsmål:** {mal}")
            if budsjett:
                st.write(f"**Startbudsjett:** {budsjett}")

            # Kopierbar tekst boks
            bio = f"Navn: {fullt_navn}\nAlder: {alder}\nKarriere: {karriere}\nLivsmål: {mal}\nKategori: {valgt_kategori}"
            st.text_area("📋 Kopier Profil-bio:", bio, height=130)

            if st.button("⭐ Lagre som favoritt"):
                st.session_state.favoritter.append(fullt_navn)
                st.success(f"{fullt_navn} er lagret i favoritter!")

        else:
            _, felles_etternavn = hent_navn(valgt_kategori, "Begge / Unisex")
            antall_voksne = random.randint(1, 2)
            
            if valgt_spill == "Sims 1 (Retro/Original)":
                antall_barn = random.randint(0, 3)
                barn_alder_tekst = "Barn"
            else:
                antall_barn = random.randint(0, 4)
                barn_alder_tekst = "Variert (Baby/Småbarn/Barn/Tenåring)"

            budsjett = generer_okonomi(antall_voksne + antall_barn) if legg_til_okonomi else None

            st.subheader(f"👨‍👩‍👧‍👦 Familie {felles_etternavn} ({valgt_spill})")
            if budsjett:
                st.write(f"**Startøkonomi:** {budsjett}")

            medlemmer_tekst = f"=== FAMILIE {felles_etternavn.upper()} ===\n"
            for i in range(antall_voksne):
                fn, _ = hent_navn(valgt_kategori, valgt_kjonn)
                alder_v = "Voksen" if valgt_spill == "Sims 1 (Retro/Original)" else random.choice(["Ung voksen", "Voksen"])
                st.write(f"* **Voksen {i+1}:** {fn} {felles_etternavn} ({alder_v})")
                medlemmer_tekst += f"- Voksen: {fn} {felles_etternavn} ({alder_v})\n"

            for i in range(antall_barn):
                fn, _ = hent_navn(valgt_kategori, valgt_kjonn)
                st.write(f"* **Barn {i+1}:** {fn} {felles_etternavn} ({barn_alder_tekst})")
                medlemmer_tekst += f"- Barn: {fn} {felles_etternavn} ({barn_alder_tekst})\n"

            st.text_area("📋 Kopier Familie-bio:", medlemmer_tekst, height=160)
            st.session_state.historikk.insert(0, f"[{valgt_spill}] Familie {felles_etternavn} ({antall_voksne} voksne, {antall_barn} barn)")

# ==========================================
# FANE 2: GENERER MANGE (BATCH 1-100 NAVN)
# ==========================================
elif valgt_fane == "📑 Generer Mange (Batch 1-100)":
    st.header("📑 Batch Navnegenerator")
    antall = st.slider("Velg hvor mange navn som skal genereres:", min_value=1, max_value=100, value=10)
    
    if st.button(f"🎲 Generer {antall} navn"):
        genererte = []
        for _ in range(antall):
            fn, en = hent_navn(valgt_kategori, valgt_kjonn)
            fullt = f"{fn} {en}"
            genererte.append(fullt)
            st.session_state.historikk.insert(0, f"[{valgt_kategori}] {fullt}")

        st.subheader("Generert Navneliste:")
        samlet_tekst = "\n".join(genererte)
        st.text_area("Kopier alle navne rad for rad:", samlet_tekst, height=250)

# ==========================================
# FANE 3: TVILLINGER & SLEKTSKAP
# ==========================================
elif valgt_fane == "👯 Tvillinger & Slektskap":
    st.header("👯 Tvillinger & Matchende Navn")
    st.write("Generer navn med bokstavrim (alliterasjon) eller matchende tema for tvillinger/trillinger!")
    
    type_par = st.radio("Velg type:", ["Tvillinger (2)", "Trillinger (3)"])
     match_bokstav = st.checkbox("Tving samme startbokstav (Bokstavrim)", value=True)

    if st.button("✨ Generer Matchende Navn"):
        data = NAVNE_DB[valgt_kategori]
        alle_navn = data["guttenavn"] + data["jentenavn"]
        _, etternavn = hent_navn(valgt_kategori, "Begge / Unisex")

        if match_bokstav:
            bokstav = random.choice(list(set([n[0] for n in alle_navn])))
            filtrerte = [n for n in alle_navn if n.startswith(bokstav)]
            if len(filtrerte) < (2 if "Tvillinger" in type_par else 3):
                filtrerte = alle_navn  # fallback om listen blir for kort
        else:
            filtrerte = alle_navn

        antall_trekk = 2 if "Tvillinger" in type_par else 3
        valgte = random.sample(filtrerte, antall_trekk)
        
        st.subheader(f"👶 {type_par} - Familie {etternavn}")
        for v in valgte:
            st.write(f"* **{v} {etternavn}**")

# ==========================================
# FANE 4: KJÆLEDYR-GENERATOR
# ==========================================
elif valgt_fane == "🐾 Kjæledyr-generator":
    st.header("🐾 Kjæledyr Navnegenerator")
    valgt_dyr = st.selectbox("Velg dyreart:", ["Hund", "Katt", "Hest", "Smådyr"])
    
    if st.button("🐾 Generer Kjæledyrnavn"):
        navn = random.choice(DYRENAVN[valgt_dyr])
        st.success(f"Ditt nye {valgt_dyr.lower()} sin navn er: **{navn}** 🐾")

# ==========================================
# FANE 5: FAVORITTER
# ==========================================
elif valgt_fane == "⭐ Favoritter":
    st.header("⭐ Lagrede Favoritter")
    if not st.session_state.favoritter:
        st.info("Ingen favoritter er lagret ennå. Klikk på '⭐ Lagre som favoritt' når du genererer enkeltsimmer!")
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

# ==========================================
# FANE 6: HISTORIKK
# ==========================================
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

# ==========================================
# FANE 7: UTFORDINGER
# ==========================================
elif valgt_fane == "🏆 Sims Utfordringer":
    st.header("🏆 Sims Utfordringer & Spillregler")
    st.write("Trenger du ny inspirasjon til spilløkten din? Generer en tilfeldig utfordring!")
    
    if st.button("🎲 Trekk en tilfeldig utfordring"):
        st.info(random.choice(UTFORDINGER))
