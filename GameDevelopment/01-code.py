import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
red = 255,0,0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = width/2, height/2
        self.rect.y = height - 60
        self.moveX = 0

    def update(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.moveX = 1
        elif keypressed[pygame.K_LEFT]:
            self.moveX = -1
        else:
            self.moveX = 0

        self.rect.x += self.moveX

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()