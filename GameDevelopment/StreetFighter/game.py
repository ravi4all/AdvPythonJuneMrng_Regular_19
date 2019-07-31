import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0
black = 0,0,0
blue = 0,0,255
green = 0,255,0

class Spritesheet():

    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name

    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(black)

        return image


class Player(pygame.sprite.Sprite):
    standingFrames = []
    def __init__(self):
        super().__init__()
        sprite = Spritesheet(ken)
        self.image = sprite.getImage(48,247,106,239)
        self.standingFrames.append(self.image)
        self.image = sprite.getImage(264,240,113,249)
        self.standingFrames.append(self.image)
        self.image = sprite.getImage(482,248,106,237)
        self.standingFrames.append(self.image)
        self.image = sprite.getImage(687,247,112,241)
        self.standingFrames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = width/2, height/2
        self.moveX = 0
        self.pos = 0

    def update(self):
        self.pos += 2
        keypressed = pygame.key.get_pressed()

        frame = (self.pos // 30) % len(self.standingFrames)
        # print(self.pos, self.pos//30, (self.pos // 30) % len(self.standingFrames))
        self.image = self.standingFrames[frame]

        if keypressed[pygame.K_RIGHT]:
            self.moveX = 1
        elif keypressed[pygame.K_LEFT]:
            self.moveX = -1
        else:
            self.moveX = 0

        self.rect.x += self.moveX

ken = pygame.image.load("ken_.png")

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

FPS = 100
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()
    clock.tick(FPS)