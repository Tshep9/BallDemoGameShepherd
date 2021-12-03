import random
import pygame, sys, math
from LevelLoader import *
from Ball import*



class Spawner():
    def __init__(self, pos=[25, 25]):
        self.image = pygame.image.load("Images/Tiles/spawner.png")
        self.rect = self.image.get_rect(center=pos)
        self.kind = "spawner"

    def update(self, size):
        pass

    def spawnBall(self):
        speed = [random.randint(-5, 5), random.randint(-5, 5)]
        size = random.randint(10, 75)
        pos = [self.rect.center]

        while speed == [0,0]:
            speed = [random.randint(-5,5), random.randint(-5,5)]

        return Ball(speed, [size, size], self.rect.center)
