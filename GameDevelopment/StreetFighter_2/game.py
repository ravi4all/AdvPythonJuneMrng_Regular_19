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


    def update(self):
        self.speedx = 0
        self.speedy = 0

class Player_2(pygame.sprite.Sprite):

    walking_frames = []
    punch_frames = []
    kick_frames = []
    super_kick_frames = []
    hit_frames = []

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

    def update(self):
        self.speedx = 0
        self.speedy = 0


pygame.time.set_timer(USEREVENT + 1, 1000)
def timer(seconds):
    font = pygame.font.SysFont(None, 50)
    seconds_display = font.render("Time Left: " + str(seconds), 1, WHITE)
    screen.blit(seconds_display, (WIDTH/2-130, 10))

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street Fighter")
clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir,'background.png')).convert()
player_sprite = pygame.image.load(path.join(img_dir, "ken_.png")).convert_alpha()
player_sprite_2 = pygame.image.load(path.join(img_dir, "ryu_.png")).convert_alpha()

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
    font = pygame.font.SysFont(None,100)
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

        all_sprites.update()

        screen.fill(BLACK)
        screen.blit(background, (0,0))
        all_sprites.draw(screen)
        timer(seconds)
        pygame.display.flip()

    pygame.quit()

main()