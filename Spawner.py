import pygame, sys, math
from LevelLoader import *


class Spawner():
    def __init__(self, pos=[25, 25]):
        self.image = pygame.image.load("Images/Tiles/spawner.png")
        self.rect = self.image.get_rect(center=pos)
        self.kind = "spawner"

    def update(self, size):
        pass

        