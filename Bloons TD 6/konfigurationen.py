
# Konstante Variablen
BREITE = 1920
HOEHE = 1080
FPS = 30

BLAU = (0, 0, 255)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)

knopf_konfiguration = {
    "startbildschirm": [
        {
            "datei": "play button.png",
            "colorkey": WEISS,
            "position": (760, 934),
            "gehe zu bildschirm": "hauptmenue"
        }
    ],
    "hauptmenue": [
        {
            "datei": "play auf hauptmenue.png",
            # "colorkey": WEISS,
            "position": (814, 791),
            "groesse": (1112 - 814, 1079 - 786),
            "gehe zu bildschirm": "maps"
        }
    ],
    "maps": [
        {
            "datei": "TownCenter.png",
            "position": (276, 223),
            "groesse": (400, 274),
            "gehe zu bildschirm": "spiel"

        }
    ]
}
bild_konfiguration = {
    "startbildschirm": [
        {
            "datei": "start.jpg",
            "position": (0, 0),
        }
    ],
    "hauptmenue": [
        {
            "datei": "AllstartBTD6.png",
            "position": (0, 0),
            "groesse": (BREITE, HOEHE),
        }
    ],

    "maps": [
        {
            "datei": "mapshintergrund.png",
            "position": (0, 0),
            "groesse": (BREITE, HOEHE),
        }
    ]
}
