import pygame, sys, math

class HUD():
    def __init__(self, startPos=[0,0]):
        self.font = pygame.font.Font(None, 40)
        self.image = self.font.render("Score: 0", True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft = startPos)

    def update(self, score):
        text = "Score: " + str(score)
        self.image = self.font.render("Score: "+str(int(score)), True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)



