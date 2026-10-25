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
# NAVNE- OG SPILDATABASE
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

# Sims 4 pakker med verdener
SIMS_4_PAKKER = {
    "The Sims 4: Get to Work": {
        "husdyr": ["Lite kjæledyr 🐹"], "okkult": ["Romvesen 👽"], "karriere": ["Læge", "Detektiv", "Forsker"], "trekk": ["Aktiv", "Vitenskapelig"], "mal": ["Mestre vitenskapen"], "verdener": ["Magnolia Promenade"]
    },
    "The Sims 4: Get Together": {
        "husdyr": [], "okkult": [], "karriere": ["DJ", "Barista"], "trekk": ["Sosial", "Danseglad"], "mal": ["Starte den beste klubben"], "verdener": ["Windenburg"]
    },
    "The Sims 4: City Living": {
        "husdyr": [], "okkult": [], "karriere": ["Politiker", "Kritiker", "Sosiale medier"], "trekk": ["Kulturinteressert", "Matglad"], "mal": ["Bli byens politiker"], "verdener": ["San Myshuno"]
    },
    "The Sims 4: Cats & Dogs": {
        "husdyr": ["Hund 🐶", "Katt 🐱"], "okkult": [], "karriere": ["Veterinær"], "trekk": ["Dyrevenn"], "mal": ["Åpne den beste dyreklinikken"], "verdener": ["Brindleton Bay"]
    },
    "The Sims 4: Seasons": {
        "husdyr": [], "okkult": ["PlantSim 🌱"], "karriere": ["Botaniker", "Gartner"], "trekk": ["Elsker kulden", "Naturglad"], "mal": ["Mestre alle årstidens høytider"], "verdener": []
    },
    "The Sims 4: Get Famous": {
        "husdyr": [], "okkult": [], "karriere": ["Skuespiller", "Influenser"], "trekk": ["Ambisiøs", "Kjendisgal"], "mal": ["Bli en verdensberømt superkjendis"], "verdener": ["Del Sol Valley"]
    },
    "The Sims 4: Island Living": {
        "husdyr": [], "okkult": ["Havfrue 🧜‍♀️"], "karriere": ["Miljøarbeider", "Livredder"], "trekk": ["Barn av havet", "Avslappet"], "mal": ["Beskytt øyas natur og kultur"], "verdener": ["Sulani"]
    },
    "The Sims 4: Discover University": {
        "husdyr": [], "okkult": [], "karriere": ["Ingeniør", "Advokat", "Professor"], "trekk": ["Akademisk", "Strukturert"], "mal": ["Graduer med toppkarakterer"], "verdener": ["Britechester"]
    },
    "The Sims 4: Eco Lifestyle": {
        "husdyr": [], "okkult": [], "karriere": ["Sivilforsker", "Skaper / Håndverker"], "trekk": ["Miljøbevisst", "Gjenvinner"], "mal": ["Gjør hele nabolaget grønt"], "verdener": ["Evergreen Harbor"]
    },
    "The Sims 4: Snowy Escape": {
        "husdyr": [], "okkult": [], "karriere": ["Lønnsslave", "Turistguide"], "trekk": ["Eventyrlysten", "Harmonisk"], "mal": ["Mestre alle fjellløyper"], "verdener": ["Mt. Komorebi"]
    },
    "The Sims 4: Cottage Living": {
        "husdyr": ["Hund 🐶", "Katt 🐱"], "okkult": [], "karriere": ["Gårdbruker"], "trekk": ["Selvforsynt", "Hjemmekjær"], "mal": ["Lev det perfekte gårds- og landsbylivet"], "verdener": ["Henford-on-Bagley"]
    },
    "The Sims 4: High School Years": {
        "husdyr": [], "okkult": [], "karriere": ["Streamer (Deltid)"], "trekk": ["Tenåringsopprør", "Populær"], "mal": ["Bli skolemester og prom-konge/-dronning"], "verdener": ["Copperdale"]
    },
    "The Sims 4: Growing Together": {
        "husdyr": [], "okkult": [], "karriere": ["Hjemmearbeider"], "trekk": ["Familiekjær", "Støttende"], "mal": ["Bygg en sammensveiset storfamilie"], "verdener": ["San Sequoia"]
    },
    "The Sims 4: Horse Ranch": {
        "husdyr": ["Hest 🐴"], "okkult": [], "karriere": ["Hestetrener", "Ranch-eier"], "trekk": ["Hesteglad", "Utefugl"], "mal": ["Vinn mesterskap i hestesport"], "verdener": ["Chestnut Ridge"]
    },
    "The Sims 4: For Rent": {
        "husdyr": [], "okkult": [], "karriere": ["Utleier", "Eiendomsmegler"], "trekk": ["Forretningsorientert", "Nysgjerrig"], "mal": ["Eie og administrere hele nabolaget"], "verdener": ["Tomarang"]
    },
    "The Sims 4: Lovestruck": {
        "husdyr": [], "okkult": [], "karriere": ["Matchmaker"], "trekk": ["Romantisk", "Flørtende"], "mal": ["Finn den store kjærlighet og opplev alt"], "verdener": ["Ciudad Enamorada"]
    },
    "The Sims 4: Life & Death": {
        "husdyr": [], "okkult": ["Spøkelse 👻", "Vampyr 🦇"], "karriere": ["Begravelsesagent", "Nekromantiker"], "trekk": ["Fascinert av døden", "Melankolsk"], "mal": ["Løs livets og dødens store mysterier"], "verdener": ["Ravenwood"]
    },
    "The Sims 4: Businesses & Hobbies": {
        "husdyr": [], "okkult": [], "karriere": ["Bedriftsgründer", "Hobbyentreprenør"], "trekk": ["Håndverker", "Innovativ"], "mal": ["Bygg opp en suksessfull forretningsimperium"], "verdener": ["Grand Bazar"]
    },
    "The Sims 4: Enchanted by Nature": {
        "husdyr": [], "okkult": ["Fe 🧚", "PlantSim 🌱"], "karriere": ["Skogvokter", "Naturforsker"], "trekk": ["Ett med naturen", "Magi-tiltrukket"], "mal": ["Beherske skogens eldgamle hemmeligheter"], "verdener": ["Glimmerbrook"]
    },
    "The Sims 4: Adventure Awaits": {
        "husdyr": [], "okkult": [], "karriere": ["Arkeolog", "Skattejeger"], "trekk": ["Fryktløs", "Nysgjerrig"], "mal": ["Finn verdens glemte skatter og tapte ruiner"], "verdener": ["Selvadorada"]
    },
    "The Sims 4: Royalty & Legacy": {
        "husdyr": [], "okkult": ["Kongelig Blod 👑"], "karriere": ["Høykonge / Monark 👑", "Kronprins(esse) 👑", "Diplomat"], "trekk": ["Kongelig verdighet", "Autoritær"], "mal": ["Etabler et mektig dynasti og hersk over riket i generasjoner"], "verdener": ["Oakhaven Castle"]
    }
}

spill_database = {
    "Sims 4 (Moderne)": {
        "trekk_type": "trekk", "har_ung_voksen": True, "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Trollmann 🪄", "Romvesen 👽", "Varulv 🐺", "Havfrue 🧜‍♀️", "PlantSim 🌱", "Fe 🧚", "Kongelig Blod 👑"],
        "karrierer": ["Astronaut", "Kokk", "Kriminell", "Forretningsmann", "Underholder", "Forfatter", "Idrettsutøver", "Hemmelig agent", "Stilist", "Forsker"],
        "trekk": ["Klossete", "Hissig", "Kreativ", "Lat", "Geni", "Matvrak", "Høflig", "Romantisk", "Sjenert", "Overambisiøs"],
        "mal": ["Bli superkjendis", "Mestre matlaging", "Finne sann kjærlighet", "Kjøpe drømmehuset", "Fullføre et aspirasjonsmål"],
        "verdener": ["Willow Creek", "Oasis Springs", "Newcrest", "Forgotten Hollow", "Glimmerbrook", "Strangerville", "Batuu", "Moonwood Mill"]
    },
    "Sims 3 (Åpen verden)": {
        "trekk_type": "trekk", "har_ung_voksen": True, "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Hest 🐴 (Sims 3: Pets)", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Heks 🪄", "Romvesen 👽", "Varulv 🐺", "Fe 🧚", "Zombie 🧟", "Genie 🧞", "Konge / Monark 👑"],
        "karrierer": ["Arkitekt", "Spøkelsesjeger", "Privatetterforsker", "Musiker", "Politiet", "Medisin", "Politiker", "Militæret", "Journalistikk", "Idrett", "Konge / Monark 👑"],
        "trekk": ["Samler", "Overfladisk", "Pyroman", "Håpløs romantiker", "Eksentrisk", "Besserwisser", "Drømmende"],
        "mal": ["Oppfylle en livslang drøm", "Lære alle ferdigheter", "Eie hele byen", "Se spøkelser i mausoleet"],
        "verdener": ["Sunset Valley", "Twinbrook", "Bridgeport", "Appaloosa Plains", "Starlight Shores", "Lunar Lakes", "Lucky Palms", "Sunlit Tides", "Monte Vista", "Dragon Valley", "Midnight Hollow", "Roaring Heights"]
    },
    "Sims 2 (Klassisk drama)": {
        "trekk_type": "poeng", "har_ung_voksen": False, "kan_studere": True,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Vampyr 🦇", "Zombie 🧟", "PlantSim 🌱", "Servobot 🤖", "Heks 🪄", "Konge / Monark 👑"],
        "karrierer": ["Leker (Toymaking)", "Showbusiness", "Paranormal", "Nattevakt", "Politiet", "Medisin", "Militæret", "Konge / Monark 👑"],
        "stjernetegn": ["Væren", "Tyren", "Tvillingene", "Krepsen", "Løven", "Jomfruen", "Vekten", "Skorpionen", "Skytten", "Stenbukken", "Vannmannen", "Fiskene"],
        "mal": ["Romanse", "Kunnskap", "Familie", "Formue", "Popularitet"],
        "verdener": ["Pleasantview", "Strangetown", "Veronaville", "Belladonna Cove", "Riverblossom Hills"]
    },
    "Sims 1 (Retro/Original)": {
        "trekk_type": "trekk", "har_ung_voksen": False, "kan_studere": False,
        "husdyr_mulige": ["Hund 🐶", "Katt 🐱", "Lite kjæledyr 🐹"],
        "okkulte": ["Magiker 🧙‍♂️", "Spøkelse 👻", "Mime/Klovn 🤡", "Konge / Monark 👑"],
        "karrierer": ["Forretningsliv", "Mote", "Musikk", "Politiet", "Militæret", "Medisin", "Arbeidsledig", "Konge / Monark 👑"],
        "trekk": ["Panisk for brann", "Avhengig av pizza", "Kranglevoren", "Evig uheldig", "Gjerrig", "Stuegris"],
        "mal": ["Bli rik nok til et basseng uten stige", "Overleve spøkelsene i huset", "Få naboene til å like deg", "Kjøpe en magisk dverg"],
        "verdener": ["Originalnabolaget", "Magitid", "Ferieøya", "Studio Town"]
    }
}

barn_aldre = ["Baby", "Småbarn (Toddler)", "Barn", "Tenåring"]
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

st.sidebar.title("🟢 Sims Navnegenerator")

valgt_fane = st.sidebar.radio("⚙️ Konfigurasjon", [
    "🎲 Generer Sim / Familie", 
    "👯 Tvillinger & Slektskap", 
    "🐾 Kjæledyr-generator", 
    "🌍 Verden-generator", 
    "⭐ Favoritter", 
    "📜 Historikk"
])

st.sidebar.markdown("---")
valgt_spill = st.sidebar.selectbox("Velg Sims-versjon:", list(spill_database.keys()))

aktive_pakker_husdyr = []
aktive_pakker_okkult = []
aktive_pakker_karriere = []
aktive_pakker_trekk = []
aktive_pakker_mal = []
aktive_pakker_verdener = []

# Dynamisk pakkevelger for Sims 4
if valgt_spill == "Sims 4 (Moderne)":
    st.sidebar.markdown("---")
    st.sidebar.subheader("📦 Velg dine Sims 4 pakker:")
    
    if "valgte_pakker" not in st.session_state:
        st.session_state.valgte_pakker = {pakke: True for pakke in SIMS_4_PAKKER.keys()}
        
    for pakkenavn in SIMS_4_PAKKER.keys():
        st.session_state.valgte_pakker[pakkenavn] = st.sidebar.checkbox(pakkenavn, value=st.session_state.valgte_pakker[pakkenavn])
        
    for pakkenavn, aktiv in st.session_state.valgte_pakker.items():
        if aktiv:
            data = SIMS_4_PAKKER[pakkenavn]
            aktive_pakker_husdyr.extend(data["husdyr"])
            aktive_pakker_okkult.extend(data["okkult"])
            aktive_pakker_karriere.extend(data["karriere"])
            aktive_pakker_trekk.extend(data["trekk"])
            aktive_pakker_mal.extend(data["mal"])
            aktive_pakker_verdener.extend(data["verdener"])

kat_lister = list(NAVNE_DB.keys())
valgt_kategori = st.sidebar.selectbox("Navnekategori / Nasjonalitet:", ["🎲 Helt tilfeldig (Bland alt)"] + kat_lister)
valgt_kjonn = st.sidebar.selectbox("Velg kjønn:", ["Begge", "Gutt / Mann", "Jente / Kvinne"])
valgt_navnetype = st.sidebar.selectbox("Velg navnetype:", ["Begge", "Normale", "Rare & gøye"])

st.sidebar.markdown("---")

mulige_okkulte_typer = list(set(spill_database[valgt_spill]["okkulte"] + aktive_pakker_okkult))

okkult_modus = st.sidebar.radio("🦇 Okkult sim-status:", ["Kun menneske", "Bestem okkult-type", "🎲 Tilfeldig (Menneske eller okkult)", "🎲 Kun tilfeldig okkult (Ingen mennesker)"])
valgt_spesifikk_okkult = None
if okkult_modus == "Bestem okkult-type":
    valgt_spesifikk_okkult = st.sidebar.selectbox("Velg okkult-type:", mulige_okkulte_typer)

legg_til_husdyr = st.sidebar.checkbox("🐾 Legg til husdyr (Pets)?", value=False)
valgt_dyreart = "🎲 Tilfeldig dyr"
if legg_til_husdyr:
    tilgjengelige_dyr = list(set(spill_database[valgt_spill]["husdyr_mulige"] + aktive_pakker_husdyr))
    valgt_dyreart = st.sidebar.selectbox("Velg dyreart:", ["🎲 Tilfeldig dyr"] + tilgjengelige_dyr)

legg_til_verden = st.sidebar.checkbox("🌍 Velg verden/nabolag?", value=True)
valgt_verden_valg = "🎲 Tilfeldig verden"
if legg_til_verden:
    mulige_verdener_liste = list(set(spill_database[valgt_spill]["verdener"] + aktive_pakker_verdener)) if valgt_spill == "Sims 4 (Moderne)" else spill_database[valgt_spill]["verdener"]
    if not mulige_verdener_liste:
        mulige_verdener_liste = ["Standard nabolag"]
    valgt_verden_valg = st.sidebar.selectbox("Velg verden:", ["🎲 Tilfeldig verden"] + sorted(mulige_verdener_liste))

legg_til_okonomi = st.sidebar.checkbox("💰 Inkluder startøkonomi (§)?", value=True)

def hent_verden_tekst(spill_navn, valgt_v):
    mulige_verdener = list(set(spill_database[spill_navn]["verdener"] + aktive_pakker_verdener)) if spill_navn == "Sims 4 (Moderne)" else spill_database[spill_navn]["verdener"]
    if not mulige_verdener:
        mulige_verdener = ["Standard nabolag"]
        
    if valgt_v == "🎲 Tilfeldig verden":
        return random.choice(mulige_verdener)
    return valgt_v

def generer_personlighet(spill_navn):
    base_data = spill_database[spill_navn]
    
    if base_data.get("trekk_type") == "poeng":
        tegn = random.choice(base_data["stjernetegn"])
        mulige_mal = base_data.get("mal", ["Romanse", "Kunnskap"])
        return f"Stjernetegn: **{tegn}** | Rotete: {random.randint(1,10)}/10", random.choice(mulige_mal)
    else:
        base_trekk = base_data.get("trekk", ["Klossete", "Kreativ"])
        mulige_trekk = list(set(base_trekk + aktive_pakker_trekk))
        base_mal = base_data.get("mal", ["Mestre matlaging"])
        mulige_mal = list(set(base_mal + aktive_pakker_mal))
        
        trekk = random.sample(mulige_trekk, min(2, len(mulige_trekk)))
        return f"{trekk[0]} og {trekk[1]}", random.choice(mulige_mal)

def sjekk_og_hent_okkult_status(modus_valg, spill_navn):
    mulige_okkulte = list(set(spill_database[spill_navn]["okkulte"] + aktive_pakker_okkult))
    if modus_valg == "Kun menneske":
        return False, "Menneske"
    elif modus_valg == "Bestem okkult-type":
        return True, valgt_spesifikk_okkult
    elif modus_valg == "🎲 Tilfeldig (Menneske eller okkult)":
        er_o = random.choice([True, False])
        return (True, random.choice(mulige_okkulte)) if er_o else (False, "Menneske")
    else:
        return True, random.choice(mulige_okkulte)

def hent_navn_komplett(kategori_valg, kjonn_kode, er_ok, navne_stil):
    if er_ok:
        fornavn = random.choice(okkulte_fornavn)
        etternavn = random.choice(okkulte_etternavn)
        return fornavn, etternavn
        
    if kategori_valg == "🎲 Helt tilfeldig (Bland alt)":
        tilfeldig_kat_navn = random.choice(list(NAVNE_DB.keys()))
        data = NAVNE_DB[tilfeldig_kat_navn]
    else:
        data = NAVNE_DB.get(kategori_valg, NAVNE_DB["Norske navn"])

    if navne_stil == "Normale":
        g_liste = data.get("guttenavn_normale", ["Lucas"])
        j_liste = data.get("jentenavn_normale", ["Emma"])
    elif navne_stil == "Rare & gøye":
        g_liste = data.get("guttenavn_rare", ["Bjarne"])
        j_liste = data.get("jentenavn_rare", ["Gry"])
    else:
        g_liste = data.get("guttenavn_normale", []) + data.get("guttenavn_rare", [])
        j_liste = data.get("jentenavn_normale", []) + data.get("jentenavn_rare", [])

    if not g_liste: g_liste = ["Lucas"]
    if not j_liste: j_liste = ["Emma"]

    if kjonn_kode == "Gutt / Mann":
        fornavn = random.choice(g_liste)
    elif kjonn_kode == "Jente / Kvinne":
        fornavn = random.choice(j_liste)
    else:
        fornavn = random.choice(g_liste + j_liste)
        
    etternavn = random.choice(data["etternavn"])
    return fornavn, etternavn

def hent_husdyr_tekst(spill, valgt_art):
    mulige_arter = list(set(spill_database[spill]["husdyr_mulige"] + aktive_pakker_husdyr))
    if not mulige_arter:
        mulige_arter = ["Hund 🐶"]
        
    if valgt_art == "🎲 Tilfeldig dyr":
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

if valgt_fane == "🎲 Generer Sim / Familie":
    st.title("🎮 Ultimate Sims Navnegenerator")
    st.write("Skap din neste sim eller familie med full støtte for verdener, nabolag, pakker og titler!")
    
    modus = st.radio("Modus:", ["Enkeltsim", "Familie (Dynamisk antall barn & alder)"], horizontal=True)

    if st.button("✨ Generer nytt!", type="primary", use_container_width=True):
        er_o, o_type = sjekk_og_hent_okkult_status(okkult_modus, valgt_spill)
        verden = hent_verden_tekst(valgt_spill, valgt_verden_valg) if legg_til_verden else "Ingen spesifisert verden"

        if modus == "Enkeltsim":
            fn, en = hent_navn_komplett(valgt_kategori, valgt_kjonn, er_o, valgt_navnetype)
            personlighet, mal = generer_personlighet(valgt_spill)
            
            mulige_karrierer = list(set(spill_database[valgt_spill]["karrierer"] + aktive_pakker_karriere))
            kan_studere = spill_database[valgt_spill]["kan_studere"]
            er_paa_uni = kan_studere and random.random() < 0.35
            
            alder = "Voksen" if valgt_spill == "Sims 1 (Retro/Original)" else ("Ung voksen" if er_paa_uni else random.choice(["Ung voksen", "Voksen", "Eldre"]))
            karriere = "Fulltidsstudent 📚" if er_paa_uni else random.choice(mulige_karrierer)
            budsjett = hent_okonomi(1) if legg_til_okonomi else None
            fullt_navn = f"{fn} {en}"

            sart_hendelse = random.choice(rare_hendelser_enkelt)
            historie_bio = f"{fullt_navn} lever et innholdsrikt liv som {alder.lower()} ({o_type}) i verdenen {verden}.\n"
            historie_bio += f"Arbeider for tiden som {karriere}.\n"
            historie_bio += f"Hovedmålet i livet er å: '{mal}'.\n\n"
            historie_bio += f"Sært trekk / hendelse fra fortiden:\n- {sart_hendelse}"
            
            if legg_til_husdyr:
                historie_bio += f"\n\nBor sammen med et kjæledyr: {hent_husdyr_tekst(valgt_spill, valgt_dyreart)}"

            res = f"### 🧑 {fullt_navn}\n"
            if legg_til_verden:
                res += f"* **Verden / Nabolag:** 🌍 {verden}\n"
            res += f"* **Type:** {o_type}\n* **Alder:** {alder}\n* **Karriere / Jobb / Tittel:** {karriere}\n"
            if budsjett:
                res += f"* **Startbudsjett:** {budsjett}\n"
            res += f"* **Personlighet:** {personlighet}\n* **Livsmål / Ambisjon:** {mal}"
            
            if legg_til_husdyr:
                res += f"\n* {hent_husdyr_tekst(valgt_spill, valgt_dyreart)}"

            st.success(res)
            
            st.markdown("### 📖 Bakgrunnshistorie & Bio")
            st.text_area("Bruk knappen øverst til høyre i boksen for å kopiere bioen:", historie_bio, height=200)

            st.session_state.historikk.insert(0, f"[{valgt_spill} - {verden}] {fullt_navn} ({o_type}, {alder})")

            if st.button("⭐ Lagre som favoritt"):
                st.session_state.favoritter.append(f"{fullt_navn} ({verden})")
                st.success(f"{fullt_navn} er lagret i favoritter!")

        else:
            _, felles_etter = hent_navn_komplett(valgt_kategori, "Begge", er_o, valgt_navnetype)
            antall_foreldre = random.randint(1, 2)
            antall_barn = 0 if valgt_spill == "Sims 1 (Retro/Original)" else random.randint(0, 4)
            budsjett = hent_okonomi(antall_foreldre + antall_barn) if legg_til_okonomi else None

            foreldre_tekst_liste = []
            foreldre_navn_kun = []
            
            if antall_foreldre == 2:
                fam_status = "Gifte / Partnere 💍"
            else:
                fam_status = random.choice(["Alene-forelder 🧑‍👦", "Skilt / Delt omsorg ⚡"])

            fam_tekst = f"=== FAMILIE-HISTORIE: FAMILIE {felles_etter.upper()} ({valgt_spill}) ===\n"
            if legg_til_verden:
                fam_tekst += f"Verden / Nabolag: {verden}\n"
            fam_tekst += f"Status: {fam_status}\n"
            if budsjett:
                fam_tekst += f"Startøkonomi: {budsjett}\n"

            st.subheader(f"👨‍👩‍👧‍👦 Familie {felles_etter}")
            if legg_til_verden:
                st.write(f"**Verden / Nabolag:** 🌍 {verden}")
            if budsjett:
                st.write(f"**Startbudsjett:** {budsjett}")
            st.write(f"**Familie-status:** {fam_status}")

            mulige_karrierer = list(set(spill_database[valgt_spill]["karrierer"] + aktive_pakker_karriere))

            for i in range(antall_foreldre):
                f_er_o, f_o_type = sjekk_og_hent_okkult_status(okkult_modus, valgt_spill)
                fn, _ = hent_navn_komplett(valgt_kategori, valgt_kjonn, f_er_o, valgt_navnetype)
                foreldre_navn_kun.append(fn)
                pers, _ = generer_personlighet(valgt_spill)
                karriere = random.choice(mulige_karrierer)
                
                st.write(f"* **Forelder {i+1} [{f_o_type}]:** {fn} {felles_etter} *(Karriere/Tittel: {karriere} | {pers})*")
                foreldre_tekst_liste.append(f"- Forelder {i+1} [{f_o_type}]: {fn} {felles_etter} (Karriere/Tittel: {karriere} | {pers})")

            barn_tekst_liste = []
            for i in range(antall_barn):
                b_er_o, b_o_type = sjekk_og_hent_okkult_status(okkult_modus, valgt_spill)
                fn, _ = hent_navn_komplett(valgt_kategori, valgt_kjonn, b_er_o, valgt_navnetype)
                barn_alder = "Barn" if valgt_spill == "Sims 1 (Retro/Original)" else random.choice(barn_aldre)
                pers, mal = generer_personlighet(valgt_spill)
                
                st.write(f"* **Barn {i+1} [{b_o_type}] ({barn_alder}):** {fn} {felles_etter} *({pers} — Mål: {mal})*")
                barn_tekst_liste.append(f"- Barn {i+1} [{b_o_type}] ({barn_alder}): {fn} {felles_etter} ({pers} — Mål: {mal})")

            mote_historie = f"De voksne i husholdningen ({' og '.join(foreldre_navn_kun)}) {random.choice(hvordan_mottets)}." if antall_foreldre > 1 else f"{foreldre_navn_kun[0]} starter et nytt kapittel på egenhånd."
            fam_dynamikk = random.choice(dynamikk_liste)
            fam_sært = random.choice(rare_hendelser_fam)

            fam_tekst += f"\nBakgrunn:\n{mote_historie}\n\n"
            fam_tekst += f"Familiedynamikk:\n{fam_dynamikk}\n\n"
            fam_tekst += f"Sær hendelse i familiens fortid:\n{fam_sært}\n\n"
            fam_tekst += "Medlemmer:\n" + "\n".join(foreldre_tekst_liste)
            if barn_tekst_liste:
                fam_tekst += "\n" + "\n".join(barn_tekst_liste)

            if legg_til_husdyr:
                h_txt = hent_husdyr_tekst(valgt_spill, valgt_dyreart)
                st.write(f"**{h_txt}**")
                fam_tekst += f"\n\nHusdyr i familien: {h_txt}"

            st.markdown("### 📖 Bakgrunnshistorie & Bio")
            st.text_area("Bruk knappen øverst til høyre i boksen for å kopiere bioen:", fam_tekst, height=260)

            st.session_state.historikk.insert(0, f"[{valgt_spill} - {verden}] Familie {felles_etter}")

elif valgt_fane == "👯 Tvillinger & Slektskap":
    st.header("👯 Tvillinger & Slektskap")
    type_par = st.radio("Type:", ["Tvillinger (2)", "Trillinger (3)"])
    match_bokstav = st.checkbox("Tving samme startbokstav", value=True)

    if st.button("✨ Generer nytt!"):
        data = NAVNE_DB.get(valgt_kategori, NAVNE_DB["Norske navn"]) if valgt_kategori != "🎲 Helt tilfeldig (Bland alt)" else random.choice(list(NAVNE_DB.values()))
        alle = data.get("guttenavn_normale", []) + data.get("jentenavn_normale", [])
        er_o, o_type = sjekk_og_hent_okkult_status(okkult_modus, valgt_spill)
        _, etternavn = hent_navn_komplett(valgt_kategori, "Begge", er_o, valgt_navnetype)
        verden = hent_verden_tekst(valgt_spill, valgt_verden_valg)
        
        if match_bokstav and alle:
            bokstav = random.choice(list(set([n[0] for n in alle])))
            filtrerte = [n for n in alle if n.startswith(bokstav)]
            if len(filtrerte) < (2 if "Tvillinger" in type_par else 3):
                filtrerte = alle
        else:
            filtrerte = alle

        valgte = random.sample(filtrerte, 2 if "Tvillinger" in type_par else 3)
        st.subheader(f"👶 Familie {etternavn} [{o_type}] — 🌍 {verden}")
        for v in valgte:
            st.write(f"* **{v} {etternavn}**")

elif valgt_fane == "🐾 Kjæledyr-generator":
    st.header("🐾 Kjæledyr-generator")
    tilgjengelige_dyr_fane = list(set(spill_database[valgt_spill]["husdyr_mulige"] + aktive_pakker_husdyr))
    valgt_dyr_fane = st.selectbox("Dyreart:", ["🎲 Tilfeldig dyr"] + tilgjengelige_dyr_fane)
    if st.button("✨ Generer nytt!"):
        st.success(hent_husdyr_tekst(valgt_spill, valgt_dyr_fane))

elif valgt_fane == "🌍 Verden-generator":
    st.header("🌍 Verden- & Nabolagsgenerator")
    mulige_verdener_fane = list(set(spill_database[valgt_spill]["verdener"] + aktive_pakker_verdener)) if valgt_spill == "Sims 4 (Moderne)" else spill_database[valgt_spill]["verdener"]
    if not mulige_verdener_fane:
        mulige_verdener_fane = ["Standard nabolag"]
        
    valgt_verden_fane = st.selectbox("Velg verden:", ["🎲 Tilfeldig verden"] + sorted(mulige_verdener_fane))
    
    if st.button("✨ Generer verden info!"):
        utvalgt_v = hent_verden_tekst(valgt_spill, valgt_verden_fane)
        st.success(f"🌍 **Valgt verden/nabolag:** {utvalgt_v} ({valgt_spill})")
        st.write("Dette nabolaget er perfekt for å starte en ny historie, bygge et drømmehus eller utforske unike hemmeligheter!")

elif valgt_fane == "⭐ Favoritter":
    st.header("⭐ Favoritter")
    if not st.session_state.favoritter:
        st.info("Ingen favoritter lagret.")
    else:
        for idx, fav in enumerate(st.session_state.favoritter):
            c1, c2 = st.columns([4, 1])
            c1.write(f"**{idx+1}. {fav}**")
            if c2.button("❌", key=f"del_{idx}"):
                st.session_state.favoritter.pop(idx)
                st.rerun()

elif valgt_fane == "📜 Historikk":
    st.header("📜 Historikk")
    if not st.session_state.historikk:
        st.info("Historikken er tom.")
    else:
        for item in st.session_state.historikk[:20]:
            st.write(f"* {item}")
        if st.button("🗑️ Tøm historikk"):
            st.session_state.historikk = []
            st.rerun()
