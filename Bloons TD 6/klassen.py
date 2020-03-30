import pygame
from os import path
from konfigurationen import *

alle_figuren = pygame.sprite.Group()
alle_knoepfe = pygame.sprite.Group()
alle_bilder = pygame.sprite.Group()

spiel_ordner = path.dirname(__file__)
bilder_ordner = path.join(spiel_ordner, "Bilder")
extras_ordner = path.join(bilder_ordner, "Extras")

class Knopf(pygame.sprite.Sprite):
    def __init__(self, konfiguration):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(extras_ordner, konfiguration["datei"])).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = konfiguration["position"]
        if "groesse" in konfiguration.keys():
            self.image = pygame.transform.scale(self.image, konfiguration["groesse"])
        if "colorkey" in konfiguration.keys():
            self.image.set_colorkey(konfiguration["colorkey"])
        # self.aktion = konfiguration["aktion"]
        self.gehe_zu_bildschirm = konfiguration["gehe zu bildschirm"]
        alle_figuren.add(self)
        alle_knoepfe.add(self)


class Bild(pygame.sprite.Sprite):
    def __init__(self, konfiguration):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(extras_ordner, konfiguration["datei"])).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = konfiguration["position"]
        if "groesse" in konfiguration.keys():
            self.image = pygame.transform.scale(self.image, konfiguration["groesse"])
        if "colorkey" in konfiguration.keys():
            self.image.set_colorkey(konfiguration["colorkey"])
        alle_figuren.add(self)
        alle_bilder.add(self)


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
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(position, (1, 1))
