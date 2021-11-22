import random
import pygame, sys, math
from Ball import *
from LevelLoader import*
"""
from PlayerBall import *
from HUD import *
from Wall import *
pygame.init()
if not pygame.font:
    print("Warning, fonts disabled")

clock = pygame.time.Clock()
size = width, height = 900, 700
screen = pygame.display.set_mode(size)
player = PlayerBall(4, [900/2-50, 700/2-50])
balls = [player]
score = HUD("Score: ", size,  [0,0])
timer = HUD("Time: ", size, [900-100,0])

kills = 0
time = 0

walls = loadLevel("Levels/level.lvl")


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


    time += 1
    spawnTimer += 1

    if spawnTimer >= spawnTimerMax:
        spawnTimer = 0
        ballSpeed = [random.randint(-5,5), random.randint(-5,5)]
        balllPos = [random.randint(0, width-100), random.randint(0, height-100)]
        ballSize = random.randint(10, 100)
        balls += [Ball(ballSpeed, [ballSize, ballSize], balllPos)]
        for ball in balls:
            if balls [-1].collideBall(ball):
                balls.remove(balls[-1])
                break


    for ball in balls:
        ball.update(size)

    timer.update(int(time/60))
    score.update(kills)

    for hitter in balls:
        for hittee in balls:
            if hitter.collideBall(hittee):
                if hitter.kind == "player":
                    kills += 10-hittee.radius/10
                    balls.remove(hittee)
        for wall in walls:
            hitter.collideWallTile(wall)


    screen.fill([0,0,0])
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(player.image, player.rect)
    screen.blit(score.image, score.rect)
    screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    clock.tick(60)
"""