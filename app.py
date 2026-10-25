import random
import streamlit as st

st.set_page_config(page_title="Ultimate Sims Navnegenerator", page_icon="🎮", layout="centered")

# ==========================================
# INITIALISERING AV SESSION STATE
# ==========================================
if "historikk" not in st.session_state:
    st.session_state.historikk = []
if "favoritter" not in st.session_state:
    st.session_state.favoritter = []

# ==========================================
# OVERSETTELSER / SPRÅK
# ==========================================
TEKSTER = {
    "Norsk": {
        "tittel": "🎮 Ultimate Sims Navnegenerator",
        "beskrivelse": "Skap din neste sim eller familie med spilltrofaste aldersregler, kjæledyr, karrierer og bakgrunnshistorie!",
        "konfig": "⚙️ Konfigurasjon",
        "spill": "Velg Sims-versjon:",
        "kat": "Navnekategori / Nasjonalitet:",
        "kat_tilfeldig": "🎲 Helt tilfeldig (Bland alt)",
        "kjonn": "Velg kjønn:",
        "kjonn_begge": "Begge / Unisex",
        "kjonn_gutt": "Gutt / Mann",
        "kjonn_jente": "Jente / Kvinne",
        "okkult": "🦇 Er okkult sim?",
        "okkult_valg": "Velg okkult-type:",
        "okkult_tilfeldig": "Tilfeldig okkult",
        "husdyr_check": "🐾 Legg til husdyr (Pets)?",
        "husdyr_valg": "Velg dyreart:",
        "dyr_tilfeldig": "🎲 Tilfeldig dyr",
        "okonomi": "💰 Inkluder startøkonomi (§)?",
        "generer": "✨ Generer nytt!",
        "modus": "Modus:",
        "enkel": "Enkeltsim",
        "familie": "Familie (Dynamisk antall barn & alder)",
        "alder": "Alder",
        "karriere": "Karriere / Jobb",
        "livsmal": "Livsmål / Ambisjon",
        "budsjett": "Startbudsjett",
        "personlighet": "Personlighet",
        "bio_tittel": "📖 Bakgrunnshistorie & Bio",
        "bio_info": "Bruk knappen øverst til høyre i boksen for å kopiere bioen:",
        "lagre_fav": "⭐ Lagre som favoritt",
        "lagret": "er lagret i favoritter!",
        "fane_sim": "🎲 Generer Sim / Familie",
        "fane_tvillinger": "👯 Tvillinger & Slektskap",
        "fane_dyr": "🐾 Kjæledyr-generator",
        "fane_fav": "⭐ Favoritter",
        "fane_hist": "📜 Historikk",
        "ui_sprog": "🌍 Velg språk (Grensesnitt):"
    },
    "English": {
        "tittel": "🎮 Ultimate Sims Name Generator",
        "beskrivelse": "Create your next sim or family with game-faithful age rules, pets, careers, and background story!",
        "konfig": "⚙️ Configuration",
        "spill": "Select Sims version:",
        "kat": "Name category / Nationality:",
        "kat_tilfeldig": "🎲 Completely Random (Mix all)",
        "kjonn": "Select gender:",
        "kjonn_begge": "Both / Unisex",
        "kjonn_gutt": "Boy / Man",
        "kjonn_jente": "Girl / Woman",
        "okkult": "🦇 Is occult sim?",
        "okkult_valg": "Select occult type:",
        "okkult_tilfeldig": "Random occult",
        "husdyr_check": "🐾 Add pets?",
        "husdyr_valg": "Select pet type:",
        "dyr_tilfeldig": "🎲 Random pet",
        "okonomi": "💰 Include starting funds (§)?",
        "generer": "✨ Generate new!",
        "modus": "Mode:",
        "enkel": "Single Sim",
        "familie": "Family (Dynamic children & age)",
        "alder": "Age",
        "karriere": "Career / Job",
        "livsmal": "Life Goal / Ambition",
        "budsjett": "Starting Budget",
        "personlighet": "Personality",
        "bio_tittel": "📖 Background Story & Bio",
        "bio_info": "Use the button in the top right of the box to copy the bio:",
        "lagre_fav": "⭐ Save as favorite",
        "lagret": "is saved to favorites!",
        "fane_sim": "🎲 Generate Sim / Family",
        "fane_tvillinger": "👯 Twins & Kinship",
        "fane_dyr": "🐾 Pet Generator",
        "fane_fav": "⭐ Favorites",
        "fane_hist": "📜 History",
        "ui_sprog": "🌍 Select Language (UI):"
    },
    "Svenska": {
        "tittel": "🎮 Ultimate Sims Namngenerator",
        "beskrivelse": "Skapa din nästa sim eller familj med spelstrogna åldersregler, husdjur, karriärer och bakgrundshistoria!",
        "konfig": "⚙️ Konfiguration",
        "spill": "Välj Sims-version:",
        "kat": "Namnkategori / Nationalitet:",
        "kat_tilfeldig": "🎲 Helt slumpmässigt (Blanda alla)",
        "kjonn": "Välj kön:",
        "kjonn_begge": "Båda / Unisex",
        "kjonn_gutt": "Pojke / Man",
        "kjonn_jente": "Flicka / Kvinna",
        "okkult": "🦇 Är okkult sim?",
        "okkult_valg": "Välj okkult typ:",
        "okkult_tilfeldig": "Slumpmässig okkult",
        "husdyr_check": "🐾 Lägg till husdjur (Pets)?",
        "husdyr_valg": "Välj husdjursart:",
        "dyr_tilfeldig": "🎲 Slumpmässigt djur",
        "okonomi": "💰 Inkludera startkapital (§)?",
        "generer": "✨ Generera ny!",
        "modus": "Läge:",
        "enkel": "Enkeltsim",
        "familie": "Familj (Dynamiskt antal barn & ålder)",
        "alder": "Ålder",
        "karriere": "Karriär / Jobb",
        "livsmal": "Livsmål / Ambition",
        "budsjett": "Startbudget",
        "personlighet": "Personlighet",
        "bio_tittel": "📖 Bakgrundshistoria & Bio",
        "bio_info": "Använd knappen uppe till höger i rutan för att kopiera bion:",
        "lagre_fav": "⭐ Spara som favorit",
        "lagret": "har sparats i favoriter!",
        "fane_sim": "🎲 Generera Sim / Familj",
        "fane_tvillinger": "👯 Tvillingar & Släkt",
        "fane_dyr": "🐾 Husdjursgenerator",
        "fane_fav": "⭐ Favoriter",
        "fane_hist": "📜 Historik",
        "ui_sprog": "🌍 Välj språk (Gränssnitt):"
    },
    "Dansk": {
        "tittel": "🎮 Ultimate Sims Navnegenerator",
        "beskrivelse": "Skab din næste sim eller familie med spiltrofaste aldersregler, kæledyr, karrierer og baggrundshistorie!",
        "konfig": "⚙️ Konfiguration",
        "spill": "Vælg Sims-version:",
        "kat": "Navnekategori / Nationalitet:",
        "kat_tilfeldig": "🎲 Helt tilfældig (Bland alt)",
        "kjonn": "Vælg køn:",
        "kjonn_begge": "Begge / Unisex",
        "kjonn_gutt": "Dreng / Mand",
        "kjonn_jente": "Pige / Kvinde",
        "okkult": "🦇 Er okkult sim?",
        "okkult_valg": "Vælg okkult type:",
        "okkult_tilfeldig": "Tilfældig okkult",
        "husdyr_check": "🐾 Tilføj kæledyr (Pets)?",
        "husdyr_valg": "Vælg kæledyrsart:",
        "dyr_tilfeldig": "🎲 Tilfældig dyr",
        "okonomi": "💰 Inkluder startøkonomi (§)?",
        "generer": "✨ Generer ny!",
        "modus": "Tilstand:",
        "enkel": "Enkeltsim",
        "familie": "Familie (Dynamisk antal børn & alder)",
        "alder": "Alder",
        "karriere": "Karriere / Job",
        "livsmal": "Livsmål / Ambition",
        "budsjett": "Startbudget",
        "personlighet": "Personlighed",
        "bio_tittel": "📖 Baggrundshistorie & Bio",
        "bio_info": "Brug knappen øverst til højre i boksen for at kopiere bioen:",
        "lagre_fav": "⭐ Gem som favorit",
        "lagret": "er gemt i favoritter!",
        "fane_sim": "🎲 Generer Sim / Familie",
        "fane_tvillinger": "👯 Tvillinger & Slægt",
        "fane_dyr": "🐾 Kæledyrsgenerator",
        "fane_fav": "⭐ Favoritter",
        "fane_hist": "📜 Historik",
        "ui_sprog": "🌍 Vælg sprog (Brugerflade):"
    },
    "Deutsch": {
        "tittel": "🎮 Ultimate Sims Namensgenerator",
        "beskrivelse": "Erstelle deinen nächsten Sim oder deine Familie mit originalgetreuen Altersregeln, Haustieren, Karrieren und Hintergrundgeschichte!",
        "konfig": "⚙️ Konfiguration",
        "spill": "Sims-Version wählen:",
        "kat": "Namenskategorie / Nationalität:",
        "kat_tilfeldig": "🎲 Völlig zufällig (Alles mischen)",
        "kjonn": "Geschlecht wählen:",
        "kjonn_begge": "Beide / Unisex",
        "kjonn_gutt": "Junge / Mann",
        "kjonn_jente": "Mädchen / Frau",
        "okkult": "🦇 Okkulter Sim?",
        "okkult_valg": "Okkaulftyp wählen:",
        "okkult_tilfeldig": "Zufälliger Okkult",
        "husdyr_check": "🐾 Haustiere hinzufügen?",
        "husdyr_valg": "Haustierart wählen:",
        "dyr_tilfeldig": "🎲 Zufälliges Tier",
        "okonomi": "💰 Startkapital einbeziehen (§)?",
        "generer": "✨ Neu generieren!",
        "modus": "Modus:",
        "enkel": "Einzelner Sim",
        "familie": "Familie (Dynamische Kinder & Alter)",
        "alder": "Alter",
        "karriere": "Karriere / Job",
        "livsmal": "Lebensziel / Ambition",
        "budsjett": "Startbudget",
        "personlighet": "Persönlichkeit",
        "bio_tittel": "📖 Hintergrundgeschichte & Bio",
        "bio_info": "Benutze den Button oben rechts im Kasten, um die Bio zu kopieren:",
        "lagre_fav": "⭐ Als Favorit speichern",
        "lagret": "wurde zu den Favoriten hinzugefügt!",
        "fane_sim": "🎲 Sim / Familie generieren",
        "fane_tvillinger": "👯 Zwillinge & Verwandtschaft",
        "fane_dyr": "🐾 Haustier-Generator",
        "fane_fav": "⭐ Favoriten",
        "fane_hist": "📜 Verlauf",
        "ui_sprog": "🌍 Sprache wählen (UI):"
    },
    "Français": {
        "tittel": "🎮 Générateur de Noms Sims Ultime",
        "beskrivelse": "Créez votre prochain sim ou famille avec des règles d'âge fidèles au jeu, des animaux, des carrières et une histoire !",
        "konfig": "⚙️ Configuration",
        "spill": "Sélectionner la version des Sims :",
        "kat": "Catégorie de nom / Nationalité :",
        "kat_tilfeldig": "🎲 Totalement aléatoire (Tout mélanger)",
        "kjonn": "Sélectionner le genre :",
        "kjonn_begge": "Les deux / Unisexe",
        "kjonn_gutt": "Garçon / Homme",
        "kjonn_jente": "Fille / Femme",
        "okkult": "🦇 Sim occulte ?",
        "okkult_valg": "Sélectionner le type occulte :",
        "okkult_tilfeldig": "Occulte aléatoire",
        "husdyr_check": "🐾 Ajouter des animaux ?",
        "husdyr_valg": "Sélectionner le type d'animal :",
        "dyr_tilfeldig": "🎲 Animal aléatoire",
        "okonomi": "💰 Inclure les fonds de départ (§) ?",
        "generer": "✨ Générer de nouveau !",
        "modus": "Mode :",
        "enkel": "Sim unique",
        "familie": "Famille (Enfants dynamiques et âge)",
        "alder": "Âge",
        "karriere": "Carrière / Emploi",
        "livsmal": "Objectif de vie / Ambition",
        "budsjett": "Budget de départ",
        "personlighet": "Personnalité",
        "bio_tittel": "📖 Histoire de fond & Bio",
        "bio_info": "Utilisez le bouton en haut à droite de la boîte pour copier la bio :",
        "lagre_fav": "⭐ Enregistrer dans les favoris",
        "lagret": "a été enregistré dans les favoris !",
        "fane_sim": "🎲 Générer Sim / Famille",
        "fane_tvillinger": "👯 Jumeaux & Parenté",
        "fane_dyr": "🐾 Générateur d'animaux",
        "fane_fav": "⭐ Favoris",
        "fane_hist": "📜 Historique",
        "ui_sprog": "🌍 Choisir la langue (IU) :"
    },
    "Español": {
        "tittel": "🎮 Generador de Nombres Sims Definitivo",
        "beskrivelse": "¡Crea tu próximo sim o familia con reglas de edad fieles al juego, mascotas, carreras e historia de fondo!",
        "konfig": "⚙️ Configuración",
        "spill": "Seleccionar versión de Los Sims:",
        "kat": "Categoría de nombre / Nacionalidad:",
        "kat_tilfeldig": "🎲 Completamente aleatorio (Mezclar todo)",
        "kjonn": "Seleccionar género:",
        "kjonn_begge": "Ambos / Unisex",
        "kjonn_gutt": "Niño / Hombre",
        "kjonn_jente": "Niña / Mujer",
        "okkult": "🦇 ¿Sim oculto?",
        "okkult_valg": "Seleccionar tipo oculto:",
        "okkult_tilfeldig": "Oculto aleatorio",
        "husdyr_check": "🐾 ¿Añadir mascotas?",
        "husdyr_valg": "Seleccionar tipo de mascota:",
        "dyr_tilfeldig": "🎲 Mascota aleatoria",
        "okonomi": "💰 ¿Incluir fondos iniciales (§)?",
        "generer": "✨ ¡Generar nuevo!",
        "modus": "Modo:",
        "enkel": "Sim individual",
        "familie": "Familia (Hijos y edad dinámicos)",
        "alder": "Edad",
        "karriere": "Carrera / Trabajo",
        "livsmal": "Meta de vida / Ambición",
        "budsjett": "Presupuesto inicial",
        "personlighet": "Personalidad",
        "bio_tittel": "📖 Historia de fondo y Biografía",
        "bio_info": "Usa el botón en la esquina superior derecha de la caja para copiar la biografía:",
        "lagre_fav": "⭐ Guardar como favorito",
        "lagret": "se ha guardado en favoritos!",
        "fane_sim": "🎲 Generar Sim / Familia",
        "fane_tvillinger": "👯 Gemelos y Parentesco",
        "fane_dyr": "🐾 Generador de Mascotas",
        "fane_fav": "⭐ Favoritos",
        "fane_hist": "📜 Historial",
        "ui_sprog": "🌍 Seleccionar idioma (IU):"
    },
    "Italiano": {
        "tittel": "🎮 Generatore di Nomi Sims Definitivo",
        "beskrivelse": "Crea il tuo prossimo sim o famiglia con regole di età fedeli al gioco, animali domestici, carriere e storia!",
        "konfig": "⚙️ Configurazione",
        "spill": "Seleziona versione di The Sims:",
        "kat": "Categoria nome / Nazionalità:",
        "kat_tilfeldig": "🎲 Completamente casuale (Mischia tutto)",
        "kjonn": "Seleziona genere:",
        "kjonn_begge": "Entrambi / Unisex",
        "kjonn_gutt": "Ragazzo / Uomo",
        "kjonn_jente": "Ragazza / Donna",
        "okkult": "🦇 Sim occulto?",
        "okkult_valg": "Seleziona tipo occulto:",
        "okkult_tilfeldig": "Occulto casuale",
        "husdyr_check": "🐾 Aggiungere animali domestici?",
        "husdyr_valg": "Seleziona tipo di animale:",
        "dyr_tilfeldig": "🎲 Animale casuale",
        "okonomi": "💰 Includere fondi iniziali (§)?",
        "generer": "✨ Genera nuovo!",
        "modus": "Modalità:",
        "enkel": "Sim singolo",
        "familie": "Famiglia (Bambini ed età dinamici)",
        "alder": "Età",
        "karriere": "Carriera / Lavoro",
        "livsmal": "Obiettivo di vita / Ambizione",
        "budsjett": "Budget iniziale",
        "personlighet": "Personalità",
        "bio_tittel": "📖 Storia di fondo e Bio",
        "bio_info": "Usa il pulsante in alto a destra del box per copiare la biografia:",
        "lagre_fav": "⭐ Salva come preferito",
        "lagret": "è stato salvato nei preferiti!",
        "fane_sim": "🎲 Genera Sim / Famiglia",
        "fane_tvillinger": "👯 Gemelli e Parentela",
        "fane_dyr": "🐾 Generatore Animali",
        "fane_fav": "⭐ Preferiti",
        "fane_hist": "📜 Cronologia",
        "ui_sprog": "🌍 Seleziona lingua (UI):"
    }
}

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
    }
}

DYRENAVN = {
    "Hund": ["Buster", "Karo", "Rex", "Balder", "Bruno", "Rambo", "Theo", "Bamse", "Charlie", "Rocky", "Bella", "Luna", "Ayla", "Daisy"],
    "Katt": ["Pusur", "Milling", "Fjonken", "Felix", "Socks", "Tiger", "Simba", "Oliver", "Missen", "Nala", "Cleo", "Sassy"],
    "Hest": ["Storm", "Faksen", "Spirit", "Gorm", "Thunder", "Cinderella", "Varg", "Dronning", "Blakken", "Star"],
    "Smådyr": ["Pip", "Squeak", "Nøtteliten", "Gnagern", "Smule", "Pompel", "Pilt", "Snickers", "Peanut"]
}
DYRE_TREKK = ["Leken 🎾", "Lat 😴", "Aggressiv 💢", "Kosete ❤️", "Uavhengig 🐾", "Fryktsom 💨", "Nysgjerrig 🔍"]

spill_database = {
    "Sims 4 (Moderne)": {
        "trekk_type": "trekk", "har_ung_voksen": True, "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Hest 🐴", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Trollmann 🪄", "Romvesen 👽", "Varulv 🐺", "Havfrue 🧜‍♀️", "PlantSim 🌱"],
        "karrierer": ["Astronaut", "Kokk", "Kriminell", "Forretningsmann", "Underholder", "Forfatter", "Idrettsutøver", "Forsker"],
        "trekk": ["Klossete", "Hissig", "Kreativ", "Lat", "Geni", "Matvrak", "Romantisk", "Sjenert"],
        "mal": ["Bli superkjendis", "Mestre matlaging", "Finne sann kjærlighet", "Kjøpe drømmehuset"]
    },
    "Sims 3 (Åpen verden)": {
        "trekk_type": "trekk", "har_ung_voksen": True, "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Hest 🐴", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Heks 🪄", "Romvesen 👽", "Varulv 🐺", "Fe 🧚", "Zombie 🧟", "Genie 🧞"],
        "karrierer": ["Arkitekt", "Spøkelsesjeger", "Musiker", "Politiet", "Medisin", "Politiker", "Militæret"],
        "trekk": ["Samler", "Overfladisk", "Pyroman", "Håpløs romantiker", "Eksentrisk", "Drømmende"],
        "mal": ["Oppfylle en livslang drøm", "Lære alle ferdigheter", "Eie hele byen"]
    },
    "Sims 2 (Klassisk drama)": {
        "trekk_type": "poeng", "har_ung_voksen": False, "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Zombie 🧟", "PlantSim 🌱", "Servobot 🤖", "Heks 🪄"],
        "karrierer": ["Leker", "Showbusiness", "Paranormal", "Politiet", "Medisin", "Militæret", "Kokk"],
        "stjernetegn": ["Væren", "Tyren", "Tvillingene", "Krepsen", "Løven", "Jomfruen", "Vekten", "Skorpionen", "Skytten", "Stenbukken", "Vannmannen", "Fiskene"],
        "mal": ["Romanse", "Kunnskap", "Familie", "Formue", "Popularitet"]
    },
    "Sims 1 (Retro/Original)": {
        "trekk_type": "trekk", "har_ung_voksen": False, "kan_studere": False,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Magiker 🧙‍♂️", "Spøkelse 👻", "Mime/Klovn 🤡"],
        "karrierer": ["Forretningsliv", "Mote", "Musikk", "Politiet", "Militæret", "Medisin", "Arbeidsledig"],
        "trekk": ["Panisk for brann", "Avhengig av pizza", "Kranglevoren", "Evig uheldig", "Gjerrig"],
        "mal": ["Bli rik nok til et basseng uten stige", "Overleve spøkelsene", "Få naboene til å like deg"]
    }
}

barn_aldre = ["Baby", "Småbarn (Toddler)", "Barn", "Tenåring"]
hvordan_mottets = ["møttes ved et uhell da begge prøvde å ta den siste grillede osten", "møttes på biblioteket", "ble kjent på en fest", "møttes på universitetsområdet"]
rare_hendelser_enkelt = ["Presterte å brenne ned kjøkkenet.", "Ble bortført av romvesener.", "Snakker med hagegnomer.", "Kjøpte 40 marsvin."]
rare_hendelser_fam = ["Ble kastet ut av parken for usynlig saft-salg.", "Huset lukter brent pizza."]
dynamikk_liste = ["Høyt konfliktnivå ved middagsbordet.", "Kaos og kreativt rot.", "Amisiøs og strukturert."]
relasjonsstatuser = ["Singel 💔", "Gift 💍", "Forlovet 💎", "Skilt ⚡", "Komplisert... 🎭"]
studieretninger = ["Biologi 🧬", "Drama 🎭", "Medisin 🩺", "Fysikk 🔬", "Kunst 🎨", "Historie 📚", "Juss ⚖️", "Økonomi 💼"]

# ==========================================
# SIDESTOLPE / MENY
# ==========================================
st.sidebar.title("🟢 Sims Generator")

# SPRÅKVELGER KNAPP / MENY
valgt_ui_spraak = st.sidebar.selectbox("🌍 Select Language / Velg språk:", list(TEKSTER.keys()))
t = TEKSTER[valgt_ui_spraak]

valgt_fane = st.sidebar.radio(t["konfig"], [
    t["fane_sim"], 
    t["fane_tvillinger"], 
    t["fane_dyr"], 
    t["fane_fav"], 
    t["fane_hist"]
])

st.sidebar.markdown("---")
valgt_spill = st.sidebar.selectbox(t["spill"], list(spill_database.keys()))

# Kategori med valg for "Helt tilfeldig (Bland alt)"
kat_lister = list(NAVNE_DB.keys())
valgt_kategori = st.sidebar.selectbox(t["kat"], [t["kat_tilfeldig"]] + kat_lister)

valgt_kjonn = st.sidebar.selectbox(t["kjonn"], [t["kjonn_begge"], t["kjonn_gutt"], t["kjonn_jente"]])

st.sidebar.markdown("---")
er_okkult = st.sidebar.checkbox(t["okkult"], value=False)
valgt_okkult_type = None
if er_okkult:
    tilgjengelige_okkulte = spill_database[valgt_spill]["okkulte"]
    valgt_okkult_type = st.sidebar.selectbox(t["okkult_valg"], [t["okkult_tilfeldig"]] + tilgjengelige_okkulte)

legg_til_husdyr = st.sidebar.checkbox(t["husdyr_check"], value=False)
valgt_dyreart = "🎲 Tilfeldig dyr"
if legg_til_husdyr:
    tilgjengelige_dyr = spill_database[valgt_spill]["husdyr_mulige"]
    valgt_dyreart = st.sidebar.selectbox(t["husdyr_valg"], [t["dyr_tilfeldig"]] + tilgjengelige_dyr)

legg_til_okonomi = st.sidebar.checkbox(t["okonomi"], value=True)

# ==========================================
# HJELPEFUNKSJONER
# ==========================================
def generer_personlighet(spill_navn):
    data = spill_database[spill_navn]
    if data["trekk_type"] == "poeng":
        tegn = random.choice(data["stjernetegn"])
        return f"Stjernetegn: **{tegn}** | Rotete: {random.randint(1,10)}/10", random.choice(data["mal"])
    else:
        trekk = random.sample(data["trekk"], min(2, len(data["trekk"])))
        return f"{trekk[0]} og {trekk[1]}", random.choice(data["mal"])

def hent_navn_komplett(kategori_valg, kjonn_kode, er_ok):
    if er_ok:
        fornavn = random.choice(["Vladislaus", "Lilith", "Raven", "Shadow", "Dracula", "Pandora"])
        etternavn = random.choice(["Bloodworth", "Nightshade", "Grimwood", "Blackwood"])
        return fornavn, etternavn
        
    if kategori_valg == t["kat_tilfeldig"]:
        # Velg en tilfeldig nasjonalitet fra databasen
        tilfeldig_kat_navn = random.choice(list(NAVNE_DB.keys()))
        data = NAVNE_DB[tilfeldig_kat_navn]
    else:
        data = NAVNE_DB.get(kategori_valg, NAVNE_DB["Norsk"])

    if kjonn_kode == t["kjonn_gutt"]:
        fornavn = random.choice(data["guttenavn"])
    elif kjonn_kode == t["kjonn_jente"]:
        fornavn = random.choice(data["jentenavn"])
    else:
        fornavn = random.choice(data["guttenavn"] + data["jentenavn"])
    etternavn = random.choice(data["etternavn"])
    return fornavn, etternavn

def hent_husdyr_tekst(spill, valgt_art):
    mulige_arter = spill_database[spill]["husdyr_mulige"]
    if valgt_art == t["dyr_tilfeldig"]:
        art = random.choice(mulige_arter)
    else:
        art = valgt_art
    
    if "Hund" in art:
        dn = random.choice(DYRENAVN["Hund"])
    elif "Katt" in art:
        dn = random.choice(DYRENAVN["Katt"])
    elif "Hest" in art:
        dn = random.choice(DYRENAVN["Hest"])
    else:
        dn = random.choice(DYRENAVN["Smådyr"])
        
    return f"🐾 Husdyr: {dn} ({art}) — Trekk: {random.choice(DYRE_TREKK)}"

def hent_okonomi(antall):
    return f"§{20000 + (antall - 1) * 5000 + random.randint(0, 10) * 1000:,}".replace(",", " ")

# ==========================================
# HOVEDDEL / FANER
# ==========================================
if valgt_fane == t["fane_sim"]:
    st.title(t["tittel"])
    st.write(t["beskrivelse"])
    
    modus = st.radio(t["modus"], [t["enkel"], t["familie"]], horizontal=True)

    if st.button(t["generer"], type="primary", use_container_width=True):
        if modus == t["enkel"]:
            fn, en = hent_navn_komplett(valgt_kategori, valgt_kjonn, er_okkult)
            personlighet, mal = generer_personlighet(valgt_spill)
            
            kan_studere = spill_database[valgt_spill]["kan_studere"]
            er_paa_uni = kan_studere and random.random() < 0.35
            
            alder = "Voksen" if valgt_spill == "Sims 1 (Retro/Original)" else ("Ung voksen" if er_paa_uni else random.choice(["Ung voksen", "Voksen", "Eldre"]))
            karriere = "Fulltidsstudent 📚" if er_paa_uni else random.choice(spill_database[valgt_spill]["karrierer"])
            budsjett = hent_okonomi(1) if legg_til_okonomi else None
            fullt_navn = f"{fn} {en}"

            res = f"### 🧑 {fullt_navn}\n* **{t['alder']}:** {alder}\n* **{t['karriere']}:** {karriere}\n"
            if budsjett:
                res += f"* **{t['budsjett']}:** {budsjett}\n"
            res += f"* **{t['personlighet']}:** {personlighet}\n* **{t['livsmal']}:** {mal}"
            
            if legg_til_husdyr:
                res += f"\n* {hent_husdyr_tekst(valgt_spill, valgt_dyreart)}"

            st.success(res)
            st.text_area(t["bio_info"], f"Navn: {fullt_navn}\nAlder: {alder}\nKarriere: {karriere}", height=120)

            st.session_state.historikk.insert(0, f"[{valgt_spill}] {fullt_navn} ({alder})")

            if st.button(t["lagre_fav"]):
                st.session_state.favoritter.append(fullt_navn)
                st.success(f"{fullt_navn} {t['lagret']}")

        else:
            _, felles_etter = hent_navn_komplett(valgt_kategori, t["kjonn_begge"], er_okkult)
            antall_foreldre = random.randint(1, 2)
            antall_barn = 0 if valgt_spill == "Sims 1 (Retro/Original)" else random.randint(0, 4)
            budsjett = hent_okonomi(antall_foreldre + antall_barn) if legg_til_okonomi else None

            st.subheader(f"👨‍👩‍👧‍👦 Familie {felles_etter}")
            if budsjett:
                st.write(f"**{t['budsjett']}:** {budsjett}")

            fam_tekst = f"=== FAMILIE {felles_etter.upper()} ===\n"
            for i in range(antall_foreldre):
                fn, _ = hent_navn_komplett(valgt_kategori, valgt_kjonn, er_okkult)
                st.write(f"* **Forelder {i+1}:** {fn} {felles_etter}")
                fam_tekst += f"- {fn} {felles_etter}\n"

            for i in range(antall_barn):
                fn, _ = hent_navn_komplett(valgt_kategori, valgt_kjonn, er_okkult)
                barn_alder = "Barn" if valgt_spill == "Sims 1 (Retro/Original)" else random.choice(barn_aldre)
                st.write(f"* **Barn {i+1}:** {fn} {felles_etter} ({barn_alder})")
                fam_tekst += f"- Barn: {fn} {felles_etter} ({barn_alder})\n"

            if legg_til_husdyr:
                h_txt = hent_husdyr_tekst(valgt_spill, valgt_dyreart)
                st.write(f"**{h_txt}**")
                fam_tekst += f"\n{h_txt}"

            st.text_area(t["bio_info"], fam_tekst, height=150)
            st.session_state.historikk.insert(0, f"[{valgt_spill}] Familie {felles_etter}")

elif valgt_fane == t["fane_tvillinger"]:
    st.header(t["fane_tvillinger"])
    type_par = st.radio("Type:", ["Tvillinger (2)", "Trillinger (3)"])
    match_bokstav = st.checkbox("Tving samme startbokstav", value=True)

    if st.button("✨ Generer"):
        data = NAVNE_DB.get(valgt_kategori, NAVNE_DB["Norsk"]) if valgt_kategori != t["kat_tilfeldig"] else NAVNE_DB["Norsk"]
        alle = data["guttenavn"] + data["jentenavn"]
        _, etternavn = hent_navn_komplett(valgt_kategori, t["kjonn_begge"], False)
        
        valgte = random.sample(alle, 2 if "2" in type_par else 3)
        st.subheader(f"👶 Familie {etternavn}")
        for v in valgte:
            st.write(f"* **{v} {etternavn}**")

elif valgt_fane == t["fane_dyr"]:
    st.header(t["fane_dyr"])
    valgt_dyr_fane = st.selectbox("Dyreart:", [t["dyr_tilfeldig"]] + spill_database[valgt_spill]["husdyr_mulige"])
    if st.button("🐾 Generer"):
        st.success(hent_husdyr_tekst(valgt_spill, valgt_dyr_fane))

elif valgt_fane == t["fane_fav"]:
    st.header(t["fane_fav"])
    if not st.session_state.favoritter:
        st.info("Ingen favoritter lagret.")
    else:
        for idx, fav in enumerate(st.session_state.favoritter):
            c1, c2 = st.columns([4, 1])
            c1.write(f"**{idx+1}. {fav}**")
            if c2.button("❌", key=f"del_{idx}"):
                st.session_state.favoritter.pop(idx)
                st.rerun()

elif valgt_fane == t["fane_hist"]:
    st.header(t["fane_hist"])
    if not st.session_state.historikk:
        st.info("Ingen historikk.")
    else:
        for item in st.session_state.historikk[:20]:
            st.write(f"* {item}")
        if st.button("🗑️ Tøm"):
            st.session_state.historikk = []
            st.rerun()
