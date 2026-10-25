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
# OVERSETTELSER / SPRÅK (UI)
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
        "kjonn_begge": "Begge",
        "kjonn_gutt": "Gutt / Mann",
        "kjonn_jente": "Jente / Kvinne",
        "navnetype": "Velg navnetype:",
        "type_begge": "Begge",
        "type_normale": "Normale",
        "type_rare": "Rare & gøye",
        "okkult_valg_mod": "🦇 Okkult sim-status:",
        "okkult_alternativer": ["Kun menneske", "Bestem okkult-type", "🎲 Tilfeldig (Menneske eller okkult)", "🎲 Kun tilfeldig okkult (Ingen mennesker)"],
        "okkult_type_velg": "Velg okkult-type:",
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
        "kjonn_begge": "Both",
        "kjonn_gutt": "Boy / Man",
        "kjonn_jente": "Girl / Woman",
        "navnetype": "Select name style:",
        "type_begge": "Both",
        "type_normale": "Normal",
        "type_rare": "Rare & funny",
        "okkult_valg_mod": "🦇 Occult sim status:",
        "okkult_alternativer": ["Human only", "Choose occult type", "🎲 Random (Human or occult)", "🎲 Random occult only (No humans)"],
        "okkult_type_velg": "Select occult type:",
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
        "kjonn_begge": "Båda",
        "kjonn_gutt": "Pojke / Man",
        "kjonn_jente": "Flicka / Kvinna",
        "navnetype": "Välj namnstil:",
        "type_begge": "Båda",
        "type_normale": "Normala",
        "type_rare": "Sällsynta & roliga",
        "okkult_valg_mod": "🦇 Okkult simstatus:",
        "okkult_alternativer": ["Endast människa", "Välj okkult typ", "🎲 Slumpmässig (Människa eller okkult)", "🎲 Endast slumpmässig okkult (Inga människor)"],
        "okkult_type_velg": "Välj okkult typ:",
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
        "kjonn_begge": "Begge",
        "kjonn_gutt": "Dreng / Mand",
        "kjonn_jente": "Pige / Kvinde",
        "navnetype": "Vælg navnetype:",
        "type_begge": "Begge",
        "type_normale": "Normale",
        "type_rare": "Sjældne & sjove",
        "okkult_valg_mod": "🦇 Okkult sim-status:",
        "okkult_alternativer": ["Kun menneske", "Vælg okkult type", "🎲 Tilfældig (Menneske eller okkult)", "🎲 Kun tilfældig okkult (Ingen mennesker)"],
        "okkult_type_velg": "Vælg okkult type:",
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
        "kjonn_begge": "Beide",
        "kjonn_gutt": "Junge / Mann",
        "kjonn_jente": "Mädchen / Frau",
        "navnetype": "Namensstil wählen:",
        "type_begge": "Beide",
        "type_normale": "Normal",
        "type_rare": "Selten & lustig",
        "okkult_valg_mod": "🦇 Okkulter Sim-Status:",
        "okkult_alternativer": ["Nur Mensch", "Okkaulftyp wählen", "🎲 Zufällig (Mensch oder okkult)", "🎲 Nur zufälliger Okkult (Keine Menschen)"],
        "okkult_type_velg": "Okkaulftyp wählen:",
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
        "kjonn_begge": "Les deux",
        "kjonn_gutt": "Garçon / Homme",
        "kjonn_jente": "Fille / Femme",
        "navnetype": "Style de nom :",
        "type_begge": "Les deux",
        "type_normale": "Normaux",
        "type_rare": "Rares & drôles",
        "okkult_valg_mod": "🦇 Statut sim occulte :",
        "okkult_alternativer": ["Humain uniquement", "Choisir le type occulte", "🎲 Aléatoire (Humain ou occulte)", "🎲 Occulte aléatoire uniquement (Pas d'humains)"],
        "okkult_type_velg": "Sélectionner le type occulte :",
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
        "kjonn_begge": "Ambos",
        "kjonn_gutt": "Niño / Hombre",
        "kjonn_jente": "Niña / Mujer",
        "navnetype": "Estilo de nombre:",
        "type_begge": "Ambos",
        "type_normale": "Normales",
        "type_rare": "Raros y divertidos",
        "okkult_valg_mod": "🦇 Estado de sim oculto:",
        "okkult_alternativer": ["Solo humano", "Elegir tipo oculto", "🎲 Aleatorio (Humano u oculto)", "🎲 Solo oculto aleatorio (Sin humanos)"],
        "okkult_type_velg": "Seleccionar tipo oculto:",
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
        "fane_sim": "🎲 Generer Sim / Familia",
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
        "kjonn_begge": "Entrambi",
        "kjonn_gutt": "Ragazzo / Uomo",
        "kjonn_jente": "Ragazza / Donna",
        "navnetype": "Stile nome:",
        "type_begge": "Entrambi",
        "type_normale": "Normali",
        "type_rare": "Rari e divertenti",
        "okkult_valg_mod": "🦇 Stato sim occulto:",
        "okkult_alternativer": ["Solo umano", "Scegli tipo occulto", "🎲 Casuale (Umano o occulto)", "🎲 Solo occulto casuale (Nessun umano)"],
        "okkult_type_velg": "Seleziona tipo occulto:",
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
# ALLE NAVNELISTER OG DATABASER
# ==========================================
NAVNE_DB = {
    "Norske navn": {
        "guttenavn_normale": ["Lucas", "Oliver", "Filip", "Emil", "Magnus", "Håkon", "Henrik", "Jonas", "Sander", "Jakob", "Elias", "Oskar", "Kasper", "Noah", "William", "Mathias", "Lukas", "Aksel", "Markus", "Tobias", "Martin", "Fredrik", "Kristian", "Alexander", "Marius", "Andreas", "Daniel", "Sebastian", "Theodor", "Sivert", "Johannes", "Emilian", "Casper", "Aron", "Leander", "Gabriel", "Isak", "Sven", "Knut", "Tor", "Even", "Jon", "Terje", "Per", "Pål", "Espen", "Stian", "Thomas", "Christian", "Bendik", "Mads", "Simen", "Vebjørn", "Eskil", "Sondre", "Brage", "Sturla", "Tage", "Jesper", "Nikolai", "Vetle", "Hermann", "Cornelius", "Adrian", "Julian", "Truls", "Birk", "Sigurd"],
        "guttenavn_rare": ["Gjest", "Torgeir", "Bjarne", "Reidar", "Gudmund", "Oddgeir", "Bjørn-Sture", "Fritjof", "Brynjulf", "Agnar", "Halldor", "Kjell-Bjarne", "Trygve", "Tormod", "Asbjørn", "Ragnar", "Øystein", "Guttorm", "Tore", "Audun", "Jarand", "Gunnar", "Ottar", "Valdemar", "Fridtjof", "Bård", "Yngve", "Dagfinn", "Reinert", "Balder", "Torstein", "Herbjørn", "Varg", "Trond", "Tellef", "Asgeir", "Snorre", "Sigbjørn", "Toralf", "Arnulf", "Einar", "Gorm", "Sturle"],
        "jentenavn_normale": ["Emma", "Nora", "Olivia", "Ella", "Sofie", "Astrid", "Ingrid", "Signe", "Tiril", "Thea", "Ida", "Maja", "Amalie", "Leah", "Sara", "Hanna", "Kaja", "Julie", "Emilie", "Celine", "Hedda", "Tuva", "Vilde", "Live", "Sunniva", "Helena", "Selma", "Martine", "Cornelia", "Victoria", "Mia", "Hennie", "Amelia", "Frida", "Agnes", "Sigrid", "Line", "Silje", "Marte", "Camilla", "Eline", "Stine", "Tonje", "Heidi", "Kristine", "Charlotte", "Pernille", "Johanne", "Marthe", "Cecilie", "Sanna", "Malin", "Ronja", "Ylva", "Oda", "Mille", "Filippa", "Carina", "Elise", "Thale", "Ada", "Matilde", "Elida", "Oline", "Tale", "Alva", "Erle"],
        "jentenavn_rare": ["Gry", "Trude-Lise", "Svanhild", "Asbjørg", "Torbjørg", "Gunnvor", "Kjellaug", "Gunda", "Gunnbjørg", "Solveig", "Borghild", "Gerd", "Ragnhild", "Ragna", "Wenche", "Bergljot", "Aslaug", "Torhild", "Liv", "Gunhild", "Hjordis", "Valborg", "Signhild", "Thora", "Ingebjørg", "Guri", "Berit", "Tordis", "Magnhild", "Oddbjørg", "Rannveig", "Åse", "Siv", "Tora", "Frøydis", "Gunvor", "Rønnaug", "Herborg", "Gunnhild", "Torunn", "Hildur", "Asgjerd", "Signy", "Valdis"],
        "etternavn": ["Hansen", "Johansen", "Olsen", "Andersen", "Pedersen", "Nilsen", "Kristiansen", "Larsen", "Sørensen", "Rasmussen", "Fløte", "Søt", "Knudaas", "Dalland", "Kvack", "Blåbær", "Myhre", "Bakken", "Solheim", "Strand", "Fjell", "Vangen", "Sivertsen", "Tveit", "Krogh", "Stensrud", "Grønn", "Rød", "Gull", "Melk", "Tøffel", "Skinknes", "Vaffel", "Spekesild", "Knoll", "Tott", "Gjørmedal", "Langbein", "Mås", "Berg", "Haugen", "Moen", "Holm", "Dahl", "Eriksen", "Karlsen", "Johnsen", "Pettersen", "Svendsen", "Jakobsen", "Jørgensen", "Henriksen", "Halvorsen", "Mo", "Fredriksen", "Andresen", "Nielsen", "Blom", "Gjesdal", "Svinø", "Fladen", "Kål", "Loffen", "Pølse", "Blyant", "Knall", "Smør", "Stubbe", "Ødegaard", "Nygård", "Fossum", "Sandvik", "Klefstad", "Bjerke", "Moe"]
    },
    "Engelske & Amerikanske navn": {
        "guttenavn_normale": ["Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Theodore", "Ethan", "Alexander", "Mason", "Logan", "Caleb", "Jack", "Owen", "Gabriel", "Carter", "Luke", "Daniel", "Matthew", "David", "Joseph", "Samuel", "John", "Wyatt", "Aiden", "Julian", "Grayson", "Leo", "Isaiah", "Charles", "Thomas", "Josiah", "Hudson", "Christian", "Hunter", "Connor", "Eli", "Ezra", "Aaron", "Landon", "Adrian", "Jonathan", "Nolan", "Jeremiah", "Easton", "Elias", "Colton", "Miles", "Cody", "Blake", "Asher", "Carson", "Austin", "Max", "Tyler", "Brandon", "Kevin", "Cooper", "Parker", "Xavier", "Cole", "Ian", "Dominic", "Jordan", "Brody", "Chase"],
        "guttenavn_rare": ["Barnaby", "Bartholomew", "Cletus", "Ezekiel", "Aloysius", "Giles", "Ignatius", "Montgomery", "Archibald", "Ebenezer", "Zebedee", "Horace", "Clarence", "Eustace", "Percival", "Hubert", "Phineas", "Balthazar", "Cornelius", "Thaddeus", "Rufus", "Ulysses", "Ambrose", "Gervase", "Beauregard", "Ignatz", "Skeeter", "Clyde", "Merle", "Elmer", "Zephyr", "Mortimer", "Gideon", "Gareth", "Cyprian", "Cuthbert"],
        "jentenavn_normale": ["Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Isabella", "Mia", "Evelyn", "Harper", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Aria", "Scarlett", "Grace", "Chloe", "Victoria", "Riley", "Lily", "Aubrey", "Zoey", "Penelope", "Hannah", "Lillian", "Addison", "Ellie", "Stella", "Natalie", "Zoe", "Leah", "Hazel", "Violet", "Aurora", "Savannah", "Audrey", "Brooklyn", "Bella", "Claire", "Skylar", "Lucy", "Paisley", "Everly", "Anna", "Caroline", "Nova", "Maya", "Naomi", "Elena", "Sarah", "Alice", "Samantha", "Ruby", "Piper", "Quinn", "Sadie"],
        "jentenavn_rare": ["Hortense", "Mildred", "Agnes", "Beatrice", "Cressida", "Flementine", "Jezebel", "Persephone", "Gertrude", "Prudence", "Wilhelmina", "Tabitha", "Hephzibah", "Petunia", "Mabel", "Brunhilde", "Eunice", "Gladys", "Maude", "Pansy", "Agatha", "Winifred", "Hermione", "Cornelia", "Gwendolyn", "Blanche", "Beryl", "Enid", "Myrtle", "Opal", "Zenobia", "Clementine", "Elvira", "Morticia", "Wednesday", "Zephyra", "Ophelia", "Hexa", "Belladonna", "Raven", "Thomasin", "Araminta", "Drusilla", "Gwendolen", "Isolde", "Maudlin"],
        "etternavn": ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", "Pancake", "Frizzled", "Doom", "Pudding", "Boots", "Waffle", "Snickerdoodle", "Bubble", "Chaos", "Spoons", "Pendelton", "Cumberbatch", "Butterworth", "Snodgrass", "Pettibone", "Hollingsworth", "Pumpernickel", "Thorn", "Winterbottom", "Sprocket", "Gasket", "Fumble", "Bumblebee", "Dingle", "Snort", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Moore", "Young", "Fluffernutter", "Snoot", "Wigglesworth", "Bumble", "Snicklefritz", "Giggle", "Skunk", "Toadstool", "Pemberton", "Fairchild", "Halloway", "Blackwood", "Sterling", "Wellington"]
    },
    "Svenske navn": {
        "guttenavn_normale": ["Liam", "William", "Hugo", "Noah", "Oliver", "Elias", "Arvid", "Ludvig", "Nils", "Sven", "Björn", "Lars", "Gustav", "Frej"],
        "guttenavn_rare": ["Sture", "Folke", "Tage", "Stellan", "Kjell", "Bo", "Rune", "Yngve"],
        "jentenavn_normale": ["Alice", "Maja", "Elsa", "Astrid", "Wilma", "Freja", "Ebba", "Saga", "Agnes", "Elin", "Ida", "Linnéa", "Lovisa", "Tove"],
        "jentenavn_rare": ["Gunilla", "Ulla", "Birgitta", "Barbro", "Maj-Britt", "Kerstin", "Ingegerd"],
        "etternavn": ["Andersson", "Johansson", "Karlsson", "Nilsson", "Eriksson", "Larsson", "Olsson", "Persson", "Svensson", "Lindberg", "Lindqvist", "Ström"]
    },
    "Danske navn": {
        "guttenavn_normale": ["Noah", "Carl", "Lukas", "Oscar", "Alfred", "Oliver", "Valdemar", "Malthe", "Emil", "Frederik", "Søren", "Mads", "Lasse"],
        "guttenavn_rare": ["Poul", "Holger", "Aage", "Børge", "Ejnar", "Flemming", "Preben"],
        "jentenavn_normale": ["Alma", "Ida", "Clara", "Ella", "Freja", "Emma", "Sofia", "Agnes", "Laura", "Mette", "Nanna", "Katrine", "Lærke"],
        "jentenavn_rare": ["Bodil", "Solveig", "Grethe", "Tove", "Else", "Rigmor", "Vibeke"],
        "etternavn": ["Jensen", "Nielsen", "Hansen", "Pedersen", "Andersen", "Christensen", "Larsen", "Sørensen", "Rasmussen", "Jørgensen"]
    },
    "Franske navn": {
        "guttenavn_normale": ["Gabriel", "Léo", "Raphaël", "Louis", "Arthur", "Jules", "Maël", "Lucas", "Adam", "Hugo", "Édouard", "Henri", "Pierre"],
        "guttenavn_rare": ["Gaston", "Barthélemy", "Alphonse", "Célestin", "Achille", "Firmin"],
        "jentenavn_normale": ["Jade", "Louise", "Emma", "Ambre", "Alice", "Rose", "Anna", "Chloé", "Mia", "Léa", "Camille", "Manon", "Céleste"],
        "jentenavn_rare": ["Georgette", "Solange", "Bernadette", "Jocelyne", "Odette", "Yvonne"],
        "etternavn": ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent", "Fontaine"]
    },
    "Italienske navn": {
        "guttenavn_normale": ["Leonardo", "Francesco", "Tommaso", "Edoardo", "Alessandro", "Lorenzo", "Mattia", "Gabriele", "Riccardo", "Matteo", "Giovanni"],
        "guttenavn_rare": ["Umberto", "Vincenzo", "Gennaro", "Ottavio", "Erasmo"],
        "jentenavn_normale": ["Sofia", "Aurora", "Giulia", "Ginevra", "Beatrice", "Alice", "Vittoria", "Emma", "Ludovica", "Matilde", "Francesca"],
        "jentenavn_rare": ["Concetta", "Addolorata", "Bruna", "Iolanda", "Felicita"],
        "etternavn": ["Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco", "Bruno"]
    },
    "Spanske navn": {
        "guttenavn_normale": ["Hugo", "Mateo", "Martin", "Lucas", "Leo", "Daniel", "Alejandro", "Manuel", "Pablo", "Álvaro", "Carlos", "Diego"],
        "guttenavn_rare": ["Fulgencio", "Eusebio", "Primitivo", "Eleuterio", "Hermenegildo"],
        "jentenavn_normale": ["Lucía", "Sofía", "Martina", "María", "Julia", "Paula", "Valeria", "Emma", "Daniela", "Carla", "Alba", "Carmen"],
        "jentenavn_rare": ["Encarnación", "Agustina", "Candelaria", "Eufemia", "Trinidad"],
        "etternavn": ["García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Sánchez", "Pérez", "Gómez", "Torres"]
    },
    "Tyske navn": {
        "guttenavn_normale": ["Noah", "Matteo", "Finn", "Leon", "Elias", "Paul", "Ben", "Luca", "Emil", "Louis", "Felix", "Maximilian", "Otto"],
        "guttenavn_rare": ["Wilhelm", "Heinrich", "Friedrich", "Gottlieb", "Gunther", "Manfred"],
        "jentenavn_normale": ["Emilia", "Mia", "Sophia", "Emma", "Hannah", "Lina", "Mila", "Ella", "Leni", "Clara", "Greta", "Johanna"],
        "jentenavn_rare": ["Brunhilde", "Gertrud", "Gisela", "Irmgard", "Waltraud", "Heidelinde"],
        "etternavn": ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann"]
    },
    "Japanske navn": {
        "guttenavn_normale": ["Ren", "Haruto", "Minato", "Yuma", "Sota", "Kenji", "Hiroshi", "Takumi", "Kaito", "Daiki", "Ryota"],
        "guttenavn_rare": ["Genji", "Toshio", "Kiyoshi", "Saburo", "Jiro"],
        "jentenavn_normale": ["Himari", "Hina", "Yua", "Sakura", "Akari", "Mei", "Aoi", "Rin", "Kiko", "Yoko", "Hana"],
        "jentenavn_rare": ["Chiyo", "Fumiko", "Katsuko", "Shizuka", "Tomoko"],
        "etternavn": ["Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Ito", "Yamamoto", "Nakamura", "Kobayashi", "Kato"]
    },
    "Koreanske navn": {
        "guttenavn_normale": ["Seojun", "Ha-joon", "Do-yun", "Eun-woo", "Ji-ho", "Min-jun", "Yu-jun", "Jung-woo", "Hyun", "Seok"],
        "guttenavn_rare": ["Dae-sung", "Sang-wook", "Byung-hee", "Man-bok"],
        "jentenavn_normale": ["Ji-an", "Ha-rin", "Seo-ah", "Seo-yun", "Ji-woo", "Min-seo", "Ha-eun", "Yuna", "Soo-jin", "Chae-won"],
        "jentenavn_rare": ["Young-soon", "Sun-ja", "Geum-hee", "Bong-soon"],
        "etternavn": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang", "Cho", "Yoon", "Jang", "Lim"]
    },
    "Fantasy & Magiske navn": {
        "guttenavn_normale": ["Vladislaus", "Malakor", "Zephyr", "Astaroth", "Lucifer", "Asmodeus", "Mortis", "Oberon", "Thorne", "Ignis", "Solomon"],
        "guttenavn_rare": ["Zod", "Azazel", "Mephisto", "Xylar", "Nebula"],
        "jentenavn_normale": ["Lilith", "Raven", "Vespera", "Pandora", "Nyx", "Titania", "Hexia", "Hecate", "Vampira", "Belladonna", "Morgana"],
        "jentenavn_rare": ["Zephyra", "Ophelia", "Hexa", "Banshee", "Cassandra", "Calypso"],
        "etternavn": ["Bloodworth", "Nightshade", "Grimwood", "Blackwood", "Cryptic", "Shadowfen", "Spellbinder", "Moonstone", "Silverfang", "Wormwood", "Graves", "Casket"]
    },
    "Gøye & Kaos-navn": {
        "guttenavn_normale": ["Bjarne", "Banan", "Kevin", "Ronny", "Tøffel", "Kåre", "Preben", "Guttorm", "Skinke", "Pølse", "Svein-Diva"],
        "guttenavn_rare": ["Skeeter", "Clyde", "Merle", "Elmer", "Wile E"],
        "jentenavn_normale": ["Berit", "Diva", "Trude", "Bella", "Gunda", "Gull-Laila", "Kjeks", "Doris", "Søt", "Snusken"],
        "jentenavn_rare": ["Hortense", "Mildred", "Pansy", "Maude", "Gladys"],
        "etternavn": ["Bråkmaker", "Kaos", "Drama", "Rømme", "Bling", "Trøbbel", "Pengepung", "Knall", "Pumpernickel", "Snodgrass", "Wigglesworth", "Skunk", "Toadstool"]
    }
}

okkulte_fornavn = ["Vladislaus", "Count", "Lilith", "Raven", "Shadow", "Dracula", "Nosferatu", "Vespera", "Malakor", "Zephyr", "Pandora", "Grim", "Nyx", "Oberon", "Titania", "Astaroth", "Hexia", "Hecate", "Lucifer", "Vampira"]
okkulte_etternavn = ["Bloodworth", "Nightshade", "Grimwood", "Blackwood", "Cryptic", "Graves", "Shadowfen", "Vampire", "Spellbinder", "Moonstone", "Bones", "Darkness", "Abyss", "Stormrider", "Casket", "Duskwood", "Hexen", "Mourning", "Silverfang", "Wormwood"]

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
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Hest 🐴 (Horse Ranch)", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Trollmann 🪄", "Romvesen 👽", "Varulv 🐺", "Havfrue 🧜‍♀️", "PlantSim 🌱"],
        "karrierer": ["Astronaut", "Kokk", "Kriminell", "Forretningsmann", "Underholder", "Forfatter", "Idrettsutøver", "Hemmelig agent", "Stilist", "Forsker"],
        "trekk": ["Klossete", "Hissig", "Kreativ", "Lat", "Geni", "Matvrak", "Høflig", "Romantisk", "Sjenert", "Overambisiøs"],
        "mal": ["Bli superkjendis", "Mestre matlaging", "Finne sann kjærlighet", "Kjøpe drømmehuset", "Fullføre et aspirasjonsmål"]
    },
    "Sims 3 (Åpen verden)": {
        "trekk_type": "trekk", "har_ung_voksen": True, "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Hest 🐴 (Sims 3: Pets)", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Heks 🪄", "Romvesen 👽", "Varulv 🐺", "Fe 🧚", "Zombie 🧟", "Genie 🧞"],
        "karrierer": ["Arkitekt", "Spøkelsesjeger", "Privatetterforsker", "Musiker", "Politiet", "Medisin", "Politiker", "Militæret", "Journalistikk", "Idrett"],
        "trekk": ["Samler", "Overfladisk", "Pyroman", "Håpløs romantiker", "Eksentrisk", "Besserwisser", "Drømmende"],
        "mal": ["Oppfylle en livslang drøm", "Lære alle ferdigheter", "Eie hele byen", "Se spøkelser i mausoleet"]
    },
    "Sims 2 (Klassisk drama)": {
        "trekk_type": "poeng", "har_ung_voksen": False, "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Zombie 🧟", "PlantSim 🌱", "Servobot 🤖", "Heks 🪄"],
        "karrierer": ["Leker (Toymaking)", "Showbusiness", "Paranormal", "Nattevakt", "Politiet", "Medisin", "Militæret"],
        "stjernetegn": ["Væren", "Tyren", "Tvillingene", "Krepsen", "Løven", "Jomfruen", "Vekten", "Skorpionen", "Skytten", "Stenbukken", "Vannmannen", "Fiskene"],
        "mal": ["Romanse", "Kunnskap", "Familie", "Formue", "Popularitet"]
    },
    "Sims 1 (Retro/Original)": {
        "trekk_type": "trekk", "har_ung_voksen": False, "kan_studere": False,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Magiker 🧙‍♂️", "Spøkelse 👻", "Mime/Klovn 🤡"],
        "karrierer": ["Forretningsliv", "Mote", "Musikk", "Politiet", "Militæret", "Medisin", "Arbeidsledig"],
        "trekk": ["Panisk for brann", "Avhengig av pizza", "Kranglevoren", "Evig uheldig", "Gjerrig", "Stuegris"],
        "mal": ["Bli rik nok til et basseng uten stige", "Overleve spøkelsene i huset", "Få naboene til å like deg", "Kjøpe en magisk dverg"]
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

kat_lister = list(NAVNE_DB.keys())
valgt_kategori = st.sidebar.selectbox(t["kat"], [t["kat_tilfeldig"]] + kat_lister)
valgt_kjonn = st.sidebar.selectbox(t["kjonn"], [t["kjonn_begge"], t["kjonn_gutt"], t["kjonn_jente"]])
valgt_navnetype = st.sidebar.selectbox(t["navnetype"], [t["type_begge"], t["type_normale"], t["type_rare"]])

# --- OKKULT KONTROLL ---
st.sidebar.markdown("---")
okkult_modus = st.sidebar.radio(t["okkult_valg_mod"], t["okkult_alternativer"])
valgt_spesifikk_okkult = None
if okkult_modus == t["okkult_alternativer"][1]: # "Bestem okkult-type"
    valgt_spesifikk_okkult = st.sidebar.selectbox(t["okkult_type_velg"], spill_database[valgt_spill]["okkulte"])

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

def sjekk_og_hent_okkult_status(modus_valg, spill_navn):
    # Returnerer (er_okkult (bool), okkult_type_streng)
    mulige_okkulte = spill_database[spill_navn]["okkulte"]
    
    if modus_valg == t["okkult_alternativer"][0]: # Kun menneske
        return False, "Menneske"
    elif modus_valg == t["okkult_alternativer"][1]: # Bestem okkult-type
        return True, valgt_spesifikk_okkult
    elif modus_valg == t["okkult_alternativer"][2]: # 🎲 Tilfeldig (Menneske eller okkult)
        er_o = random.choice([True, False])
        if er_o:
            return True, random.choice(mulige_okkulte)
        else:
            return False, "Menneske"
    else: # 🎲 Kun tilfeldig okkult (Ingen mennesker)
        return True, random.choice(mulige_okkulte)

def hent_navn_komplett(kategori_valg, kjonn_kode, er_ok, navne_stil):
    if er_ok:
        fornavn = random.choice(okkulte_fornavn)
        etternavn = random.choice(okkulte_etternavn)
        return fornavn, etternavn
        
    if kategori_valg == t["kat_tilfeldig"]:
        tilfeldig_kat_navn = random.choice(list(NAVNE_DB.keys()))
        data = NAVNE_DB[tilfeldig_kat_navn]
    else:
        data = NAVNE_DB.get(kategori_valg, NAVNE_DB["Norske navn"])

    if navne_stil == t["type_normale"]:
        g_liste = data.get("guttenavn_normale", ["Lucas"])
        j_liste = data.get("jentenavn_normale", ["Emma"])
    elif navne_stil == t["type_rare"]:
        g_liste = data.get("guttenavn_rare", ["Bjarne"])
        j_liste = data.get("jentenavn_rare", ["Gry"])
    else:
        g_liste = data.get("guttenavn_normale", []) + data.get("guttenavn_rare", [])
        j_liste = data.get("jentenavn_normale", []) + data.get("jentenavn_rare", [])

    if not g_liste: g_liste = ["Lucas"]
    if not j_liste: j_liste = ["Emma"]

    if kjonn_kode == t["kjonn_gutt"]:
        fornavn = random.choice(g_liste)
    elif kjonn_kode == t["kjonn_jente"]:
        fornavn = random.choice(j_liste)
    else:
        fornavn = random.choice(g_liste + j_liste)
        
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
        er_o, o_type = sjekk_og_hent_okkult_status(okkult_modus, valgt_spill)

        if modus == t["enkel"]:
            fn, en = hent_navn_komplett(valgt_kategori, valgt_kjonn, er_o, valgt_navnetype)
            personlighet, mal = generer_personlighet(valgt_spill)
            
            kan_studere = spill_database[valgt_spill]["kan_studere"]
            er_paa_uni = kan_studere and random.random() < 0.35
            
            alder = "Voksen" if valgt_spill == "Sims 1 (Retro/Original)" else ("Ung voksen" if er_paa_uni else random.choice(["Ung voksen", "Voksen", "Eldre"]))
            karriere = "Fulltidsstudent 📚" if er_paa_uni else random.choice(spill_database[valgt_spill]["karrierer"])
            budsjett = hent_okonomi(1) if legg_til_okonomi else None
            fullt_navn = f"{fn} {en}"

            sart_hendelse = random.choice(rare_hendelser_enkelt)
            historie_bio = f"{fullt_navn} lever et innholdsrikt liv som {alder.lower()}. "
            historie_bio += f"Arbeider for tiden som {karriere}. "
            historie_bio += f"Hovedmålet i livet er å: '{mal}'.\n\n"
            historie_bio += f"Sært trekk / hendelse fra fortiden:\n- {sart_hendelse}"

            res = f"### 🧑 {fullt_navn}\n* **Type:** {o_type}\n* **{t['alder']}:** {alder}\n* **{t['karriere']}:** {karriere}\n"
            if budsjett:
                res += f"* **{t['budsjett']}:** {budsjett}\n"
            res += f"* **{t['personlighet']}:** {personlighet}\n* **{t['livsmal']}:** {mal}"
            
            if legg_til_husdyr:
                res += f"\n* {hent_husdyr_tekst(valgt_spill, valgt_dyreart)}"

            st.success(res)
            st.text_area(t["bio_info"], historie_bio, height=140)

            st.session_state.historikk.insert(0, f"[{valgt_spill}] {fullt_navn} ({o_type}, {alder})")

            if st.button(t["lagre_fav"]):
                st.session_state.favoritter.append(fullt_navn)
                st.success(f"{fullt_navn} {t['lagret']}")

        else:
            # For familie velger vi felles etternavn basert på om første sim er okkult
            _, felles_etter = hent_navn_komplett(valgt_kategori, t["kjonn_begge"], er_o, valgt_navnetype)
            antall_foreldre = random.randint(1, 2)
            antall_barn = 0 if valgt_spill == "Sims 1 (Retro/Original)" else random.randint(0, 4)
            budsjett = hent_okonomi(antall_foreldre + antall_barn) if legg_til_okonomi else None

            st.subheader(f"👨‍👩‍👧‍👦 Familie {felles_etter}")
            if budsjett:
                st.write(f"**{t['budsjett']}:** {budsjett}")

            fam_tekst = f"=== FAMILIE {felles_etter.upper()} ===\n"
            for i in range(antall_foreldre):
                f_er_o, f_o_type = sjekk_og_hent_okkult_status(okkult_modus, valgt_spill)
                fn, _ = hent_navn_komplett(valgt_kategori, valgt_kjonn, f_er_o, valgt_navnetype)
                st.write(f"* **Forelder {i+1} [{f_o_type}]:** {fn} {felles_etter}")
                fam_tekst += f"- {fn} {felles_etter} ({f_o_type})\n"

            for i in range(antall_barn):
                b_er_o, b_o_type = sjekk_og_hent_okkult_status(okkult_modus, valgt_spill)
                fn, _ = hent_navn_komplett(valgt_kategori, valgt_kjonn, b_er_o, valgt_navnetype)
                barn_alder = "Barn" if valgt_spill == "Sims 1 (Retro/Original)" else random.choice(barn_aldre)
                st.write(f"* **Barn {i+1} [{b_o_type}]:** {fn} {felles_etter} ({barn_alder})")
                fam_tekst += f"- Barn: {fn} {felles_etter} ({b_o_type}, {barn_alder})\n"

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
        data = NAVNE_DB.get(valgt_kategori, NAVNE_DB["Norske navn"]) if valgt_kategori != t["kat_tilfeldig"] else random.choice(list(NAVNE_DB.values()))
        alle = data.get("guttenavn_normale", []) + data.get("jentenavn_normale", [])
        er_o, o_type = sjekk_og_hent_okkult_status(okkult_modus, valgt_spill)
        _, etternavn = hent_navn_komplett(valgt_kategori, t["kjonn_begge"], er_o, valgt_navnetype)
        
        if match_bokstav and alle:
            bokstav = random.choice(list(set([n[0] for n in alle])))
            filtrerte = [n for n in alle if n.startswith(bokstav)]
            if len(filtrerte) < (2 if "2" in type_par else 3):
                filtrerte = alle
        else:
            filtrerte = alle

        valgte = random.sample(filtrerte, 2 if "2" in type_par else 3)
        st.subheader(f"👶 Familie {etternavn} [{o_type}]")
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
