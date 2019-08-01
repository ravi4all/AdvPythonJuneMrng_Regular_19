import pygame
from pygame.locals import *
from os import path

WIDTH = 1200
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

class Spritesheet():

    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name

    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(BLACK)

        return image

class Player_1(pygame.sprite.Sprite):

    walking_frames = []
    punch_frames = []
    kick_frames = []
    super_kick_frames = []

    isAttack = False

    health = 450
    strength = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet(player_sprite)
        self.image = spritesheet.getImage(42,247,116,243)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(44,731,118,243)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(256,731,118,243)
        self.walking_frames.append(self.image)

        self.image = spritesheet.getImage(42,490,118,240)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(260,489,166,240)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(472,487,122,245)
        self.punch_frames.append(self.image)

        self.image = spritesheet.getImage(250,1451,118,250)
        self.kick_frames.append(self.image)
        self.image = spritesheet.getImage(428,1457,208,248)
        self.kick_frames.append(self.image)
        self.image = spritesheet.getImage(676,1461,120,244)
        self.kick_frames.append(self.image)

        self.image = spritesheet.getImage(18,1701,116,248)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(212,1705,172,240)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(426,1707,216,238)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(658,1737,188,210)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(898,1727,118,218)
        self.super_kick_frames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2-250, HEIGHT/2+70)

        self.punchActive = 0
        self.kickActive = 0
        self.superKickActive = 0
        self.moving = False

    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.hit = pygame.sprite.groupcollide(ken, ryo, False, False)
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_d]:
            self.speedx = 8
            self.moving = True
            if self.rect.x > WIDTH or self.hit:
                self.moving = False
                self.speedx = 0
        elif keypressed[pygame.K_a]:
            self.speedx = -8
            self.moving = True
            if self.rect.x < 0:
                self.moving = False
                self.speedx = 0
        elif keypressed[pygame.K_s]:
            self.punch = True
        elif keypressed[pygame.K_w]:
            self.kick = True
        elif keypressed[pygame.K_f]:
            self.superKick = True
        else:
            self.superKick = False
            self.punch = False
            self.kick = False

        #self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.moving:
            self.rect.x += self.speedx
#        print(self.rect.x)

        pos = self.rect.x
        print("Pos",pos)
        pun = self.punchActive
        kickFrames = self.kickActive
        superKickFrames = self.superKickActive

        frame = (pos // 30) % len(self.walking_frames)
        # print("Position",pos//30)
        # print("Frame",frame)
        self.image = self.walking_frames[frame]

        if self.punch:
            frame = (pun // 30) % len(self.punch_frames)
            self.image = self.punch_frames[frame]
            if self.hit:
                player_2.strength -= 1
                player_2.isAttack = True
                punchSound.play()

        elif self.kick:
            frame = (kickFrames // 30) % len(self.kick_frames)
            self.image = self.kick_frames[frame]
            if self.hit:
                player_2.strength -= 4
                player_2.isAttack = True
                punchSound.play()

        elif self.superKick:
            frame = (superKickFrames // 30) % len(self.super_kick_frames)
            self.image = self.super_kick_frames[frame]
            if self.hit:
                player_2.strength -= 8
                player_2.isAttack = True
                attackSound.play()
        else:
            player_2.isAttack = False


class Player_2(pygame.sprite.Sprite):

    walking_frames = []
    punch_frames = []
    kick_frames = []
    super_kick_frames = []
    hit_frames = []

    cpu_moves = []

    isAttack = False

    health = 450
    strength = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet(player_sprite_2)
        self.image = spritesheet.getImage(2750,41,102,226)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(2756,317,110,224)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(2394,315,94,226)
        self.walking_frames.append(self.image)

        self.image = spritesheet.getImage(2737,1219,130,238)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2492,1213,184,240)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2492,1213,184,240)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2300,1219,130,236)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2108,1225,112,232)
        self.punch_frames.append(self.image)

        self.image = spritesheet.getImage(1012,905,94,228)
        self.kick_frames.append(self.image)
        self.image = spritesheet.getImage(811,878,135,252)
        self.kick_frames.append(self.image)

        self.image = spritesheet.getImage(58,217,96,267)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(216,260,136,219)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(394,332,212,118)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(646,282,92,200)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(806,365,180,111)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(1026,300,98,258)
        self.super_kick_frames.append(self.image)

        self.image = spritesheet.getImage(1174,1571,144,242)
        self.hit_frames.append(self.image)
        self.image = spritesheet.getImage(1375,1583,123,226)
        self.hit_frames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2+250, HEIGHT/2+90)

        self.punchActive = 0
        self.kickActive = 0
        self.superKickActive = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_j]:
            self.speedx = -8
        elif keypressed[pygame.K_l]:
            self.speedx = 8
        elif keypressed[pygame.K_k]:
            self.punch = True
        elif keypressed[pygame.K_i]:
            self.kick = True
        elif keypressed[pygame.K_h]:
            self.superKick = True
        else:
            self.superKick = False
            self.punch = False
            self.kick = False

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        pos = self.rect.x
        pun = self.punchActive
        kickFrames = self.kickActive
        superKickFrames = self.superKickActive

        frame = (pos // 30) % len(self.walking_frames)
        self.image = self.walking_frames[frame]

        self.hit = pygame.sprite.groupcollide(ken, ryo, False, False)

        if self.punch:
            frame = (pun // 30) % len(self.punch_frames)
            self.image = self.punch_frames[frame]
            self.isAttack = False
            if self.hit:
                player.strength -= 1
                player.isAttack = True
                punchSound.play()

        if self.kick:
            frame = (kickFrames // 30) % len(self.kick_frames)
            self.image = self.kick_frames[frame]
            self.isAttack = False
            if self.hit:
                player.strength -= 4
                player.isAttack = True
                punchSound.play()

        if self.superKick:
            frame = (superKickFrames // 30) % len(self.super_kick_frames)
            self.image = self.super_kick_frames[frame]
            self.isAttack = False
            if self.hit:
                player.strength -= 8
                player.isAttack = True
                attackSound.play()

        if self.isAttack:
            frame = (kickFrames // 30) % len(self.hit_frames)
            self.image = self.hit_frames[frame]


pygame.time.set_timer(USEREVENT + 1, 1000)
def timer(seconds):
    font = pygame.font.Font('font_1.ttf', 50)
    seconds_display = font.render("Time Left: " + str(seconds), 1, WHITE)
    screen.blit(seconds_display, (WIDTH/2-130, 10))


def healthBarPlayer_1():
    health = 450+player.strength

    if health > 300:
        col = GREEN
    elif health > 150:
        col = YELLOW
    else:
        col = RED

    if health < 0:
        health = 0
        player.strength = 0

    pygame.draw.rect(screen, col, (10,10,health,40))

def healthBarPlayer_2():
    health = 450+player_2.strength

    if health > 300:
        col = GREEN
    elif health > 150:
        col = YELLOW
    else:
        col = RED

    if health < 0:
        health = 0
        player_2.strength = 0

    pygame.draw.rect(screen, col, (740,10,health,40))

pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street Fighter")
clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir,'background.png')).convert()
splash_bg = pygame.image.load(path.join(img_dir,'splash-bg.jpg')).convert()
player_sprite = pygame.image.load(path.join(img_dir, "ken_.png")).convert_alpha()
player_sprite_2 = pygame.image.load(path.join(img_dir, "ryu_.png")).convert_alpha()

attackSound = pygame.mixer.Sound(path.join(snd_dir, 'attack.wav'))
punchSound = pygame.mixer.Sound(path.join(snd_dir, 'punch2.wav'))

backgroundSound = pygame.mixer.Sound(path.join(snd_dir, 'StreetFighter.ogg'))
themeSound = pygame.mixer.Sound(path.join(snd_dir, 've_music.wav'))

all_sprites = pygame.sprite.Group()
player = Player_1()
player_2 = Player_2()

ken = pygame.sprite.Group()
ken.add(player)

ryo = pygame.sprite.Group()
ryo.add(player_2)

all_sprites.add(player)
all_sprites.add(player_2)


def gameOverScreen():
    font = pygame.font.Font('font_1.ttf',100)
    text_1 = font.render("Game Over", True, RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(text_1, (WIDTH/2-150,HEIGHT/2-150))
        pygame.display.update()

def main():
    seconds = 45
    # Game loop
    running = True
    backgroundSound.play(-1)
    # backgroundSound.set_volume(0.2)
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == USEREVENT + 1:
                seconds -= 1

        if seconds == -1:
            gameOverScreen()

        player.punchActive += 7
        player.kickActive += 7
        player.superKickActive += 7

        player_2.punchActive += 10
        player_2.kickActive += 5
        player_2.superKickActive += 7

        all_sprites.update()

        screen.fill(BLACK)
        screen.blit(background, (0,0))
        all_sprites.draw(screen)
        timer(seconds)
        healthBarPlayer_1()
        healthBarPlayer_2()
        pygame.display.flip()

    pygame.quit()


def startScreen():
    font = pygame.font.Font('font_1.ttf',70)
    text_1 = font.render("Hit SPACE to ", True, RED)
    text_2 = font.render("Start Game", True, RED)
    screen.blit(text_1, (50,300))
    screen.blit(text_2, (80, 400))

def splashScreen():

    running = True
    themeSound.play(-1)
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    themeSound.stop()
                    main()

        screen.blit(splash_bg, (0,0))
        startScreen()
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    splashScreen()
