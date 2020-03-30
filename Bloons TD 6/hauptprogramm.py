from klassen import *

pygame.init()
bildschirm = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Bloons TD 6")
uhr = pygame.time.Clock()

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
