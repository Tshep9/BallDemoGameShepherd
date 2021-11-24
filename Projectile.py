import random
import pygame, sys, math
from LevelLoader import *
from Ball import*



class Shoot():
    def __init__(self, pos=[25, 25]):
        self.image = pygame.image.load("Images/Player Ball/player_shoot.png")
        self.rect = self.image.get_rect(center=pos)
        self.kind = "shot"

    def update(self, size):
        pass

    def spawnShot(self):
        speed = [random.randint(-5, 5), random.randint(-5, 5)]
        size = random.randint(10, 100)
        pos = [self.rect.center]

        while speed == [0,0]:
            speed = [random.randint(-5,5), random.randint(-5,5)]

        return Ball(speed, [size, size], self.rect.center)