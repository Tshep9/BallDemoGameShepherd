import pygame, sys, math
from Ball import *
pygame.init()

clock = pygame.time.Clock()
size = width, height = 900, 700
screen = pygame.display.set_mode(size)

ball1 = Ball("Ball.png", [2,6])
ball2 = Ball("Ball.png", [7,1], [200,10])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    ball1.move()
    ball1.collideWall(size)

    ball2.move()
    ball2.collideWall(size)

    ball1.collideBall(ball2)
    ball2.collideBall(ball1)

    screen.fill([0,0,0])
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    pygame.display.flip()
    clock.tick(60)
