from klassen import *

pygame.init()
bildschirm = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Bloons TD 6")
uhr = pygame.time.Clock()

def neuer_bildschirm(bildschirmart):
    alle_figuren.empty()
    for bild in bild_konfiguration[bildschirmart]:
        Bild(bild)
    for knopf in knopf_konfiguration[bildschirmart]:
        Knopf(knopf)

neuer_bildschirm("startbildschirm")

# Game Loop
laufend = True
while laufend:
    # Warten bis diese Schleife anfangen soll
    uhr.tick(FPS)
    # Checken ob irgendjemand eine Taste gedrückt hat

    for ereignis in pygame.event.get():
        if ereignis.type == pygame.MOUSEBUTTONDOWN:
            maus_pos = pygame.mouse.get_pos()
            print(maus_pos)
            geklickte_knoepfe = pygame.sprite.spritecollide(Punkt(maus_pos), alle_knoepfe, False)
            if geklickte_knoepfe:
                # breakpoint()
                print(geklickte_knoepfe[0].gehe_zu_bildschirm)
                neuer_bildschirm(geklickte_knoepfe[0].gehe_zu_bildschirm)
            else:
                print("Kein Knopf gedrückt")

        # für Fenster schließen checken
        if ereignis.type == pygame.QUIT:
            laufend = False

    # Für Bildschirmanzeige vorbereiten
    alle_figuren.update()

    # Malen
    bildschirm.fill(SCHWARZ)
    alle_figuren.draw(bildschirm)
    pygame.display.flip()


pygame.quit()
