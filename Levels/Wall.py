import pygame, sys, math

class Wall():
    def __init__(self, pos=[25,25]):
        self.image = pygame.image.load("Images/Tiles/wall.png")
        self.rect = self.image.get_rect(center = pos)
        self.speed = self.speedx, self.speedy = speed

        self.kind = "wall"
      


    def update(self, size):
       pass


   
