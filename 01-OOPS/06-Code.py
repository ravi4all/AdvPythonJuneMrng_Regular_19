import pygame
import random
pygame.init()
width = 1000
height = 500
screen = pygame.display.set_mode((1000,500))
red = 255,0,0
white = 255,255,255
black = 0,0,0
green = 0,255,0
color_1 = 100,120,126

class Ball():

    def __init__(self):
        self.x =0
        self.y = 0
        self.moveX = random.randint(1,3)
        self.moveY = random.randint(1,3)
        self.radius = random.randint(30,60)
        self.color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - self.radius:
            self.moveX = random.randint(-3, -1)
        elif self.x < self.radius:
            self.moveX = random.randint(1, 3)
        elif self.y > height - self.radius:
            self.moveY = random.randint(-3, -1)
        elif self.y < self.radius:
            self.moveY = random.randint(1, 3)

# ball_1 = Ball()
# ball_2 = Ball()
# ball_3 = Ball()

ballList = []

for i in range(5):
    ball = Ball()
    ballList.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # pygame.draw.circle(screen,black,[ball_1.x, ball_1.y],ball_1.radius)
    # ball_1.update()
    #
    # pygame.draw.circle(screen, black, [ball_2.x, ball_2.y], ball_2.radius)
    # ball_2.update()
    #
    # pygame.draw.circle(screen, black, [ball_3.x, ball_3.y], ball_3.radius)
    # ball_3.update()
    for i in range(len(ballList)):
        pygame.draw.circle(screen, ballList[i].color, [ballList[i].x, ballList[i].y], ballList[i].radius)
        ballList[i].update()

    pygame.display.update()