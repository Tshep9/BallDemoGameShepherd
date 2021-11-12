import pygame, sys, math
from Ball import *
pygame.init()

clock = pygame.time.Clock()
size = width, height = 900, 700
screen = pygame.display.set_mode(size)

ball1 = Ball("Ball.png", [2,6])
ball2 = Ball("Ball.png", [7,1], [250,10])
ball3 = Ball("Ball.png", [2,1], [100,10])
ball4 = Ball("Ball.png", [3,5], [400,10])
ball5 = Ball("Ball.png", [1,6], [550,30])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    ball1.move()
    ball1.collideWall(size)

    ball2.move()
    ball2.collideWall(size)

    ball3.move()
    ball3.collideWall(size)

    ball4.move()
    ball4.collideWall(size)

    ball5.move()
    ball5.collideWall(size)

    ball1.collideBall(ball2)
    ball1.collideBall(ball3)
    ball1.collideBall(ball4)
    ball1.collideBall(ball5)

    ball2.collideBall(ball1)
    ball2.collideBall(ball3)
    ball2.collideBall(ball4)
    ball2.collideBall(ball5)

    ball3.collideBall(ball1)
    ball3.collideBall(ball2)
    ball3.collideBall(ball4)
    ball3.collideBall(ball5)

    ball4.collideBall(ball1)
    ball4.collideBall(ball2)
    ball4.collideBall(ball3)
    ball4.collideBall(ball5)

    ball5.collideBall(ball1)
    ball5.collideBall(ball2)
    ball5.collideBall(ball3)
    ball5.collideBall(ball4)

    screen.fill([0,0,0])
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    screen.blit(ball3.image, ball3.rect)
    screen.blit(ball4.image, ball4.rect)
    screen.blit(ball5.image, ball5.rect)
    pygame.display.flip()
    clock.tick(60)
