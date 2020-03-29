import pygame
from os import path
from sprite_arten import *

# Konstante Variablen
BREITE = 1920
HOEHE = 1080
FPS = 30

BLAU = (0, 0, 255)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)


pygame.init()
bildschirm = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Bloons TD 6")
uhr = pygame.time.Clock()

alle_figuren = pygame.sprite.Group()
spiel_ordner = path.dirname(__file__)
bilder_ordner = path.join(spiel_ordner, "Bilder")
extras_ordner = path.join(bilder_ordner, "Extras")
startbildschirm = pygame.image.load(path.join(extras_ordner, "start.jpg")).convert()
play_button = pygame.image.load(path.join(extras_ordner, "play button.png")).convert()
play_button.get_rect()
allstart = pygame.image.load(path.join(extras_ordner, "AllstartBTD6.png")).convert()
play_button.set_colorkey(WEISS)
hintergrund = startbildschirm

# Game Loop
laufend = True
while laufend:
    # Warten bis diese Schleife anfangen soll
    uhr.tick(FPS)
    # Checken ob irgendjemand eine Taste gedrückt hat

    for ereignis in pygame.event.get():
        if ereignis.type == pygame.MOUSEBUTTONDOWN:
            maus_pos = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(maus_pos):
                hintergrund = allstart

        # für Fenster schließen checken
        if ereignis.type == pygame.QUIT:
            laufend = False
    # Für Bildschirmanzeige vorbereiten
    alle_figuren.update()
    # Malen
    bildschirm.fill(SCHWARZ)
    bildschirm.blit(hintergrund, (0, 0))
    bildschirm.blit(play_button, (760, 934))
    alle_figuren.draw(bildschirm)
    # Bildschirm umdrehen
    pygame.display.flip()


pygame.quit()
