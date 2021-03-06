import pygame
import math
from os import path
from konfigurationen import *

alle_figuren = pygame.sprite.Group()
alle_knoepfe = pygame.sprite.Group()
alle_bilder = pygame.sprite.Group()
alle_bloons = pygame.sprite.Group()

spiel_ordner = path.dirname(__file__)
bilder_ordner = path.join(spiel_ordner, "Bilder")
extras_ordner = path.join(bilder_ordner, "Extras")
bloons_ordner = path.join(bilder_ordner, "Bloons")

px_pro_frame = px_pro_sekunde / FPS

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


class Bloon(pygame.sprite.Sprite):
    def __init__(self, pfad):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(bloons_ordner, "bloon_rot.png")).convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(SCHWARZ)
        self.pfad = pfad
        self.rect.center = self.pfad["startposition"]
        self.x_float = self.rect.x
        self.y_float = self.rect.y
        self.pfad_segment = 0
        self.richtung = self.pfad["pfad_segmente"][0]["startrichtung_grad"]
        self.distanz_px = self.pfad["pfad_segmente"][0]["distanz_px"]
        self.zurueckgelegte_distanz = 0
        alle_figuren.add(self)
        alle_bloons.add(self)                                                                                                                                                   

    def update(self):
        self.x_float += px_pro_frame * math.cos((self.richtung / 360) * 2 * math.pi)
        self.y_float += - px_pro_frame * math.sin((self.richtung / 360) * 2 * math.pi)
        self.rect.x = int(self.x_float)
        self.rect.y = int(self.y_float)
        self.zurueckgelegte_distanz += px_pro_frame
        if self.zurueckgelegte_distanz >= self.pfad["pfad_segmente"][self.pfad_segment]["distanz_px"]:
            self.pfad_segment += 1
            if self.pfad_segment == len(self.pfad["pfad_segmente"])-1:
                self.kill()
            else:
                self.richtung = self.pfad["pfad_segmente"][self.pfad_segment]["startrichtung_grad"]
                self.zurueckgelegte_distanz = 0
                self.distanz_px = self.pfad["pfad_segmente"][self.pfad_segment]["distanz_px"]
                if self.pfad["pfad_segmente"][self.pfad_segment]["kurve"] == "rechts":
                    winkelunterschied = self.pfad["pfad_segmente"][self.pfad_segment]["startrichtung_grad"] -self.pfad["pfad_segmente"][self.pfad_segment+1]["startrichtung_grad"]
                    winkelunterschied = winkelunterschied % 360
                    self.kreis_umfang_px = 360 * self.distanz_px / winkelunterschied
                elif self.pfad["pfad_segmente"][self.pfad_segment]["kurve"] == "links":
                    winkelunterschied = self.pfad["pfad_segmente"][self.pfad_segment+1]["startrichtung_grad"] -self.pfad["pfad_segmente"][self.pfad_segment]["startrichtung_grad"]
                    winkelunterschied = winkelunterschied % 360
                    self.kreis_umfang_px =  self.distanz_px * 360 / winkelunterschied
        else:
            if self.pfad["pfad_segmente"][self.pfad_segment]["kurve"] == "gerade":
                pass
            elif self.pfad["pfad_segmente"][self.pfad_segment]["kurve"] == "rechts":
                self.richtung -= (360 * px_pro_frame / self.kreis_umfang_px) % 360
            elif self.pfad["pfad_segmente"][self.pfad_segment]["kurve"] == "links":
                self.richtung += (360 * px_pro_frame / self.kreis_umfang_px) % 360
        print(self.richtung)


class Charakter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Pfeil(pygame.sprite.Sprite):
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
