import pygame
from os import path
from konfigurationen import *

alle_figuren = pygame.sprite.Group()
alle_knoepfe = pygame.sprite.Group()

spiel_ordner = path.dirname(__file__)
bilder_ordner = path.join(spiel_ordner, "Bilder")
extras_ordner = path.join(bilder_ordner, "Extras")

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
