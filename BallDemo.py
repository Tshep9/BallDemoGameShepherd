import random
import pygame, sys, math
from Ball import *
from LevelLoader import*
from PlayerBall import *
from HUD import *
from Wall import *
from Spawner import*
from Projectile import*
pygame.init()
if not pygame.font:
    print("Warning, fonts disabled")

clock = pygame.time.Clock()
size = width, height = 900, 700
screen = pygame.display.set_mode(size)
player = PlayerBall(4, [900/2-50, 700/2-50])
balls = [player]
shots = []
score = HUD("Score: ", size,  [0,0])
timer = HUD("Time: ", size, [900-100,0])

kills = 10
time = 0

tiles = loadLevel("Levels/level.lvl")
walls = tiles[0]
spawners = tiles[1]

#Backgroundmusic.ogg by David Renda URL: https://www.fesliyanstudios.com/royalty-free-music/downloads-c/8-bit-music/6
pygame.mixer.music.load("Sounds/Background.ogg")
pygame.mixer.music.play(-1, 0.0)


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
            elif event.key == pygame.K_f or event.key == pygame.K_SPACE:
                balls += [player.spawnShot()]
                kills += -1

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
        spawner = spawners[random.randint(0, len(spawners)-1)]
        balls += [spawner.spawnBall()]
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
                if hitter.kind == "shot":
                    if hittee.kind != "shot":
                        kills += 10-hittee.radius/10
                        hittee.kill()
                elif hitter.kind == "player":
                    kills += -5
                    hittee.kill()
                    sound = pygame.mixer.Sound("Sounds/hit.ogg")
                    sound.play()


        for wall in walls:
            hitter.collideWallTile(wall)






    screen.fill([0,0,0])
    for spawner in spawners:
        screen.blit(spawner.image, spawner.rect)
    for ball in balls:
        if not ball.living:
            balls.remove(ball)
        screen.blit(ball.image, ball.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)

    screen.blit(player.image, player.rect)
    screen.blit(score.image, score.rect)
    screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    clock.tick(60)
