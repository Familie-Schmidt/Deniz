
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
            "position": (157, 223),
            "groesse": (400, 274),
            "gehe zu bildschirm": "spiel"

        },
        {
            "datei": "TreeStump.png",
            "position": (757, 223),
            "groesse": (400, 274),
            "gehe zu bildschirm": "spiel"

        },
        {
            "datei": "Monkey_Meadow_Halloween_2018.png",
            "position": (1357, 223),
            "groesse": (400, 274),
            "gehe zu bildschirm": "spiel"

        },
        {
            "datei": "Carved.png",
            "position": (157, 623),
            "groesse": (400, 274),
            "gehe zu bildschirm": "spiel"

        },
        {
            "datei": "Winter_Park.png",
            "position": (757, 623),
            "groesse": (400, 274),
            "gehe zu bildschirm": "spiel"

        },
        {
            "datei": "Frozen_Over.png",
            "position": (1357, 623),
            "groesse": (400, 274),
            "gehe zu bildschirm": "spiel"

        }
    ],
    "spiel": []
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
    ],
    "spiel": [
        {
            "datei": "Frozen_Over.png",
            "position": (0, 0),
            "groesse": (BREITE, HOEHE),
        }
    ]
}
