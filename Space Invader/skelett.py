import pygame
import random

#Konstante Variablen
BREITE=360
HÖHE=400
FPS=30

BLAU=(0,0,255)
SCHWARZ=(0,0,0)
WEIß=(255,255,255)
ROT=(255,0,0)
GRÜN=(0,255,0)

#initialisierung
pygame.init()
pygame.mixer.init()
bildschirm= pygame.display.set_mode((BREITE, HÖHE))
pygame.display.set_caption("Space Invader")
uhr=pygame.time.Clock()

alle_figuren=pygame.sprite.Group()

#Game Loop
laufend=True
while laufend==True:
    #Warten bis diese Schleife anfangen soll
    uhr.tick(FPS)
    #Checken ob irgendjemand eine Taste gedrückt hat

    for ereignis in pygame.event.get():
        #für Fenster schließen checken
        if ereignis.type==pygame.QUIT:
            laufend=False
    #Für Bildschirmanzeige vorbereiten
    alle_figuren.update()
    #Malen
    bildschirm.fill(SCHWARZ)
    alle_figuren.draw(bildschirm)
    #Bildschirm umdrehen
    pygame.display.flip()


pygame.quit()
