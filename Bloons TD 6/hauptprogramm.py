import pygame
from os import path
import pdb

# Konstante Variablen
BREITE = 1920
HOEHE = 1080
FPS = 30

BLAU = (0, 0, 255)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)

# breakpoint()

class Knopf(pygame.sprite.Sprite):
    def __init__(self, konfiguration):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(extras_ordner, konfiguration["datei"])).convert()
        self.image.set_colorkey(konfiguration["colorkey"])
        self.rect = self.image.get_rect()
        self.rect.topleft = konfiguration["position"]
        self.aktion = konfiguration["aktion"]
        alle_figuren.add(self)
        alle_knoepfe.add(self)


class Charakter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Pfeil(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Bloons(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Pop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Punkt(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, x + 1, y + 1)


knopf_konfiguration = {
    "startbildschirm": [
        {
            "datei": "play button.png",
            "colorkey": WEISS,
            "position": (760, 934),
            "aktion": "Gehe zu Hauptmenue"
        }
    ],
    "hauptmenue": [
        {
            "datei": "play auf hauptmenue.png",
            "colorkey": WEISS,
            "position": (760, 910),
            "aktion": "zeige map an"
        }
    ]
}


pygame.init()
bildschirm = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Bloons TD 6")
uhr = pygame.time.Clock()

alle_figuren = pygame.sprite.Group()
alle_knoepfe = pygame.sprite.Group()

spiel_ordner = path.dirname(__file__)
bilder_ordner = path.join(spiel_ordner, "Bilder")
extras_ordner = path.join(bilder_ordner, "Extras")

startbildschirm = pygame.image.load(path.join(extras_ordner, "start.jpg")).convert()
hintergrund = startbildschirm

for knopf in knopf_konfiguration["startbildschirm"]:
    Knopf(knopf)


allstart = pygame.image.load(path.join(extras_ordner, "AllstartBTD6.png")).convert()


# Game Loop
laufend = True
while laufend:
    # Warten bis diese Schleife anfangen soll
    uhr.tick(FPS)
    # Checken ob irgendjemand eine Taste gedrückt hat

    for ereignis in pygame.event.get():
        if ereignis.type == pygame.MOUSEBUTTONDOWN:
            # breakpoint()
            maus_pos = pygame.mouse.get_pos()
            print(maus_pos)
            geklickte_knoepfe = pygame.sprite.spritecollide(
                Punkt(maus_pos[0], maus_pos[1]), alle_knoepfe, False
            )
            print(geklickte_knoepfe[0].aktion)
            if geklickte_knoepfe[0].aktion == "Gehe zu Hauptmenue":
                hintergrund = allstart

        # für Fenster schließen checken
        if ereignis.type == pygame.QUIT:
            laufend = False
    # Für Bildschirmanzeige vorbereiten
    alle_figuren.update()
    # Malen
    bildschirm.fill(SCHWARZ)
    bildschirm.blit(hintergrund, (0, 0))
    alle_figuren.draw(bildschirm)
    # Bildschirm umdrehen
    pygame.display.flip()


pygame.quit()
