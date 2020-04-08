
# Konstante Variablen
BREITE = 1920
HOEHE = 1080
FPS = 120
px_pro_sekunde = 250

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
            "datei": "Carved.png",
            "position": (0, 0),
            "groesse": (BREITE - 250, HOEHE),
        }
    ]
}

pfad_konfiguration = {
    "Carved.png": {
        "startposition": (777, 0),
        "pfad_segmente": [
            {"startrichtung_grad": 270, "kurve": "gerade", "distanz_px": 55},
            {"startrichtung_grad": 270, "kurve": "rechts", "distanz_px": 70},
            {"startrichtung_grad": 195, "kurve": "gerade", "distanz_px": 25 * 5.5},
            {"startrichtung_grad": 195, "kurve": "links", "distanz_px": 20.7 * 55},
            {"startrichtung_grad": 350, "kurve": "gerade", "distanz_px": 2.5 * 5.5},
            {"startrichtung_grad": 350, "kurve": "rechts", "distanz_px": 10 * 5.5},
            {"startrichtung_grad": 360 - 25.8, "kurve": "links", "distanz_px": 314 },
            {"startrichtung_grad": 25.8, "kurve": "rechts", "distanz_px": 55 },
            {"startrichtung_grad": 10, "kurve": "links", "distanz_px": 600 + 55 },
            {"startrichtung_grad": 180 - 82, "kurve": "links", "distanz_px": 20 },
            {"startrichtung_grad": 180 + 20, "kurve": "gerade", "distanz_px": 182 + 55 * 0.8 },
            {"startrichtung_grad": 180 + 20, "kurve": "links", "distanz_px": 85 },
            {"startrichtung_grad": 180 + 72, "kurve": "gerade", "distanz_px": 75 },
            {"startrichtung_grad": 180 + 72, "kurve": "rechts", "distanz_px": 72 },
            {"startrichtung_grad": 180 - 33 - 20, "kurve": "gerade", "distanz_px": 48 },
            {"startrichtung_grad": 180 - 33 - 20, "kurve": "links", "distanz_px": 120 },
            {"startrichtung_grad": 180 - 5, "kurve": "gerade", "distanz_px": 106 },
            {"startrichtung_grad": 180 -5, "kurve": "links", "distanz_px": 94 },
            {"startrichtung_grad": 180 + 51, "kurve": "gerade", "distanz_px": 64 },
            {"startrichtung_grad": 180 + 51, "kurve": "rechts", "distanz_px": 74 },
            {"startrichtung_grad": 180 - 62, "kurve": "gerade", "distanz_px": 90 },
            {"startrichtung_grad": 180 - 62, "kurve": "links", "distanz_px": 91 },
            {"startrichtung_grad": 180 - 18, "kurve": "gerade", "distanz_px": 16  },
            {"startrichtung_grad": 180 - 18, "kurve": "links", "distanz_px": 72 },
            {"startrichtung_grad": 360 - 73, "kurve": "links", "distanz_px": 326 },
            {"startrichtung_grad": 360 - 34, "kurve": "links", "distanz_px": 120 },
            {"startrichtung_grad": 47 + 20, "kurve": "gerade", "distanz_px": 63 - 55 * 0.7 },
            {"startrichtung_grad": 47 + 20, "kurve": "rechts", "distanz_px": 98 },
            {"startrichtung_grad": 360 - 79, "kurve": "gerade", "distanz_px": 64 },
            {"startrichtung_grad": 360 - 79, "kurve": "links", "distanz_px": 86 },
            {"startrichtung_grad": 72, "kurve": "gerade", "distanz_px": 63 - 55 * 0.3 },
            {"startrichtung_grad": 72, "kurve": "rechts", "distanz_px": 94 },
            {"startrichtung_grad": 360 - 49, "kurve": "gerade", "distanz_px": 69 },
            {"startrichtung_grad": 360 - 49, "kurve": "links", "distanz_px": 111 - 55 * 0.6},
            {"startrichtung_grad": 34, "kurve": "links", "distanz_px": 313 },
            {"startrichtung_grad": 180 - 86, "kurve": "rechts", "distanz_px": 100 },
            {"startrichtung_grad": 17, "kurve": "gerade", "distanz_px": 47 },
            {"startrichtung_grad": 17, "kurve": "links", "distanz_px": 117 },
            {"startrichtung_grad": 180 - 75 + 12, "kurve": "links", "distanz_px": 497 },
            {"startrichtung_grad": 180 - 11, "kurve": "rechts", "distanz_px": 151 },
            {"startrichtung_grad": 90, "kurve": "gerade", "distanz_px": 400 },
            {"startrichtung_grad": 90},

        ]
    }
}
