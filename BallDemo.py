import random
import pygame, sys, math
from Ball import *
from PlayerBall import *
pygame.init()

clock = pygame.time.Clock()
size = width, height = 900, 700
screen = pygame.display.set_mode(size)
player = PlayerBall(4, [900/2-50, 700/2-50])
balls = [player]

spawnTimer = 0
spawnTimerMax = 60*1;

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")


    spawnTimer += 1
    if spawnTimer >= spawnTimerMax:
        spawnTimer = 0;
        ballSpeed = [random.randint(-5,5), random.randint(-5,5)]
        balllPos = [random.randint(0, width-100), random.randint(0, height-100)]
        ballSize = random.randint(10, 100)
        balls += [Ball(ballSpeed, [ballSize, ballSize], balllPos)]
        print(len(balls))
        for ball in balls:
            if balls [-1].collideBall(ball):
                balls.remove(balls[-1])
                break






    for ball in balls:
        ball.update(size)

    for hitter in balls:
        for hittee in balls:
            if hitter.collideBall(hittee):
                if hitter.kind == "player":
                    balls.remove(hittee)

    screen.fill([0,0,0])
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)
