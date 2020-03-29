# Art from Kenney.nl:)
# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under
# CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>

import pygame
import random
import os

img_ordner = os.path.join(os.path.dirname(__file__), "img")
snd_ordner = os.path.join(os.path.dirname(__file__), "snd")
# Konstante Variablen
BREITE = 480
HÖHE = 600
FPS = 60

BLAU = (0, 0, 255)
SCHWARZ = (0, 0, 0)
WEIß = (255, 255, 255)
ROT = (255, 0, 0)
GRÜN = (0, 255, 0)
GELB = (255, 255, 0)

spiel_ordner = os.path.dirname(__file__)
img_ordner = os.path.join(spiel_ordner, "img")

schriftart_name = pygame.font.match_font("cooper black")


def male_text(oberflaeche, text, groesse, x, y):
    schriftart = pygame.font.Font(schriftart_name, groesse)
    text_oberflaeche = schriftart.render(text, True, WEIß)
    text_rect = text_oberflaeche.get_rect()
    text_rect.midtop = (x, y)
    oberflaeche.blit(text_oberflaeche, text_rect)


def male_schild_bar(oberflaeche, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LÄNGE = 100
    BAR_HÖHE = 10
    fill = (pct / 100) * BAR_LÄNGE
    umrandung_rect = pygame.Rect(x, y, BAR_LÄNGE, BAR_HÖHE)
    fill_rect = pygame.Rect(x, y, fill, BAR_HÖHE)
    pygame.draw.rect(oberflaeche, GRÜN, fill_rect)
    pygame.draw.rect(oberflaeche, WEIß, umrandung_rect, 2)


class Spieler(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(spieler_img, (50, 38))
        self.image.set_colorkey(SCHWARZ)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, GELB,  self.rect.center, self.radius)
        self.rect.centerx = BREITE / 2
        self.rect.bottom = HÖHE - 10
        self.geschwindigkeit_x = 0
        self.schild = 100

    def update(self):
        self.geschwindigkeit_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] == True:
            self.geschwindigkeit_x = -5
        if keystate[pygame.K_RIGHT] == True:
            self.geschwindigkeit_x = 5
        self.rect.x += self.geschwindigkeit_x
        if self.rect.right > BREITE:
            self.rect.right = BREITE
        if self.rect.left < 0:
            self.rect.left = 0

    def schiessen(self):
        laser_sound.play()
        Kugel(self.rect.centerx, self.rect.top)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(SCHWARZ)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, GELB,  self.rect.center, self.radius)
        self.rect.x = random.randrange(BREITE - self.rect.width)
        self.rect.y = random.randrange(-300, -150)
        self.geschwindigkeit_y = random.randrange(1, 7)
        self.geschwindigkeit_x = random.randrange(-3, 3)
        self.rot = 0
        self.rot_geschwindigkeit = random.randrange(-8, 8)
        self.letztes_update = pygame.time.get_ticks()
        mobs.add(self)
        alle_figuren.add(self)

    def rotieren(self):
        jetzt = pygame.time.get_ticks()
        if jetzt - self.letztes_update > 50:
            self.letztes_update = jetzt
            self.rot += self.rot_geschwindigkeit
            zentrum = self.rect.center
            self.image = pygame.transform.rotate(self.image_orig, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = zentrum

    def update(self):
        self.rotieren()
        self.rect.y += self.geschwindigkeit_y
        self.rect.x += self.geschwindigkeit_x
        if self.rect.top > HÖHE or self.rect.right < 0 or self.rect.left > BREITE:
            self.rect.x = random.randrange(BREITE - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            # 1 + int(pygame.time.get_ticks() / 2000))
            self.geschwindigkeit_y = random.randrange(1, 7) + int(score / 1000)
            self.geschwindigkeit_x = random.randrange(-3, 3)


class Kugel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(laser_img, (10, 30))
        self.image.set_colorkey(SCHWARZ)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.geschwindigkeit_y = -10
        kugeln.add(self)
        alle_figuren.add(self)

    def update(self):
        self.rect.y += self.geschwindigkeit_y
        # Kill es wenn die Kugel on the top ist
        if self.rect.bottom < 0:
            self.kill()


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(["schild", "gun"])
        self.image = powerup_bilder[self.type]
        self.image.set_colorkey(SCHWARZ)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.geschwindigkeit_y = 3
        powerups.add(self)
        alle_figuren.add(self)

    def update(self):
        self.rect.y += self.geschwindigkeit_y
        # Kill es wenn die Kugel on the top ist
        if self.rect.top > HÖHE:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, mitte, größe):
        pygame.sprite.Sprite.__init__(self)
        self.size = größe
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = mitte
        self.frame = 0
        self.letztes_update = pygame.time.get_ticks()
        self.frame_rate = 75
        alle_figuren.add(self)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.letztes_update > self.frame_rate:
            self.letztes_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                mitte = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = mitte


# initialisierung
pygame.init()
pygame.mixer.init()
bildschirm = pygame.display.set_mode((BREITE, HÖHE))
pygame.display.set_caption("Space Invader")
uhr = pygame.time.Clock()

# Alle grafiken laden
hintergrund = pygame.image.load(os.path.join(img_ordner, "starfield.png")).convert()
hintergrund_rect = hintergrund.get_rect()
spieler_img = pygame.image.load(os.path.join(img_ordner, "playerShip1_green.png")).convert()
laser_img = pygame.image.load(os.path.join(img_ordner, "laserGreen10.png")).convert()
# meteor_img = pygame.image.load(os.path.join(img_ordner, "meteorBrown_med1.png")).convert()
meteor_images = []
meteor_liste = ["meteorBrown_big1.png", "meteorBrown_big2.png", "meteorBrown_small1.png",
                "meteorBrown_med1.png", "meteorBrown_med1.png", "meteorBrown_small2.png",
                "meteorBrown_tiny1.png"]

for img in meteor_liste:
    meteor_images.append(pygame.image.load(os.path.join(img_ordner, img)).convert())
explosion_anim = {}
explosion_anim["gr"] = []
explosion_anim["kl"] = []
explosion_anim["player"] = []
for i in range(9):
    datei_name = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(os.path.join(img_ordner, datei_name)).convert()
    img.set_colorkey(SCHWARZ)
    img_gr = pygame.transform.scale(img, (75, 75))
    explosion_anim["gr"].append(img_gr)
    img_kl = pygame.transform.scale(img, (32, 32))
    explosion_anim["kl"].append(img_kl)
    datei_name = "sonicExplosion0{}.png".format(i)
    img_spieler = pygame.image.load(os.path.join(img_ordner, datei_name)).convert()
    img_spieler.set_colorkey(SCHWARZ)
    explosion_anim["player"].append(img_spieler)

powerup_bilder = {}
powerup_bilder["schild"] = pygame.image.load(os.path.join(img_ordner, "shield_gold.png")).convert()
powerup_bilder["gun"] = pygame.image.load(os.path.join(img_ordner, "bolt_gold.png")).convert()

laser_sound = pygame.mixer.Sound(os.path.join(snd_ordner, "laser.wav"))
pygame.mixer.music.set_volume(2.0)

explosion_sound = pygame.mixer.Sound(os.path.join(snd_ordner, "explosion.wav"))
pygame.mixer.music.load(os.path.join(snd_ordner, "space invader hintergrundmusic.ogg"))

alle_figuren = pygame.sprite.Group()
mobs = pygame.sprite.Group()
kugeln = pygame.sprite.Group()
powerups = pygame.sprite.Group()
spieler = Spieler()
alle_figuren.add(spieler)
for i in range(8):
    Mob()

score = 0
pygame.mixer.music.play(loops=-1)
# Game Loop
laufend = True
while laufend == True:
    # Warten bis diese Schleife anfangen soll
    uhr.tick(FPS)
    # Checken ob irgendjemand eine Taste gedrückt hat

    for ereignis in pygame.event.get():
        # für Fenster schließen checken
        if ereignis.type == pygame.QUIT:
            laufend = False
        elif ereignis.type == pygame.KEYDOWN:
            if ereignis.key == pygame.K_SPACE:
                spieler.schiessen()
                pygame.time.set_timer(pygame.USEREVENT, 250)
        elif ereignis.type == pygame.USEREVENT:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE] == True:
                spieler.schiessen()

    # Für Bildschirmanzeige vorbereiten
    alle_figuren.update()

    # Prüfen ob eine Kugel einen mob berührt
    kollisionen = pygame.sprite.groupcollide(mobs, kugeln, True, True)
    for i in kollisionen:
        explosion_sound.play()
        alter_score = score
        score += 61 - i.radius + 10 * i.geschwindigkeit_y
        Explosion(i.rect.center, "gr")
        Mob()
        if random.random() < 0.1:
            Pow(i.rect.center)

        grenze = 2000
        if alter_score % grenze >= int(0.75*grenze) and score % grenze < int(0.25*grenze):
            Mob()

    #Prüfen ob spieler mit powerups kollidiert
    kollisionen = pygame.sprite.spritecollide(spieler, powerups, True)
    for kollision in kollisionen:
        if kollision.type == "schild":
            spieler.schild += random.randrange(10, 35)
        if kollision.type == "gun":
            pass

    # prüfen ob eine Kollision passiert
    kollisionen = pygame.sprite.spritecollide(spieler, mobs, True, pygame.sprite.collide_circle)
    for kollision in kollisionen:
        Explosion(kollision.rect.center, "kl")
        Mob()
        spieler.schild -= kollision.radius
        if spieler.schild <= 0:
            todes_explosion = Explosion(spieler.rect.center, "player")
            spieler.kill()

    if not spieler.alive() and not todes_explosion.alive():
        laufend = False

    # Malen
    bildschirm.fill(SCHWARZ)
    bildschirm.blit(hintergrund, hintergrund_rect)
    # bildschirm.blit(spaceshooter, hintergrund_rect)
    alle_figuren.draw(bildschirm)
    male_text(bildschirm, str(score), 18, BREITE / 2, 10)
    male_schild_bar(bildschirm, 5, 5, spieler.schild)
    # Bildschirm umdrehen
    pygame.display.flip()


pygame.quit()
