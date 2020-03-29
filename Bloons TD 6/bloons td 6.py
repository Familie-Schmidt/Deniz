# Fängt an einen Screen zu erstellen.
import pygame, time
pygame.init()
bildschirm=pygame.display.set_mode((1200,800))

start=pygame.image.load("Bilder/Extras/start.jpg")
start=pygame.transform.scale(start,(1200,800))
bildschirm.blit(start,(0,0))

play_button=pygame.image.load("Bilder/Extras/play button.png")
play_button=pygame.transform.scale(play_button,(200,90))
bildschirm.blit(play_button,(500,640))

Allstart=pygame.image.load("Bilder/Extras/AllstartBTD6.png")
Allstart=pygame.transform.scale(Allstart,(1200,800))

pygame.display.flip()
#time.sleep(30)
#In den Befehlen hier hat er den startbildschirm projeziert.

while 1>0:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            bildschirm.blit(Allstart,(0,0))

    pygame.display.flip()
    time.sleep(0.1)
