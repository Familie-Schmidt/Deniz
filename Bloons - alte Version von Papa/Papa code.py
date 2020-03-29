import pygame, sys, os

def initialise():
    global screen, landschaft, affe
    pygame.init()
    screen_dim = (1000, 600)
    screen = pygame.display.set_mode(screen_dim)
    pygame.display.set_caption("Bloons TD 6")

    BASE = os.path.dirname(__file__) # Pfad zum Verzeichnis dieses Skriptes.
#    IMAGE = os.path.join(BASE, "mein-super-bild.png")
    landschaft = pygame.image.load(os.path.join(BASE, 'Bilder/Park_Path.PNG'))
    landschaft = pygame.transform.scale(landschaft, (800, 600))

    affe = pygame.image.load(os.path.join(BASE, 'Bilder/affe1.png'))
    affe = pygame.transform.scale(affe, (100, 100))

initialise()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(landschaft, (0, 0))
    screen.blit(affe, (700, 50))
    pygame.display.flip()
