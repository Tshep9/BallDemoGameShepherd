import pygame, sys, math

class Ball():
    def __init__(self, image, speed, size, pos=[0,0]):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft = pos)
        self.radius = (self.rect.width + self.rect.height) / 4
        self.speed = self.speedx, self.speedy = speed

        self.didBounceX = False
        self.didBounceY = False

    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def collideWall(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceX:
            if self.rect.right > width or self.rect.left < 0:
                self.speedx = -self.speedx
                self.didBounceX = True
        if not self.didBounceY:
            if self.rect.bottom > height or self.rect.top < 0:
                self.speedy = -self.speedy
                self.didBounceY = True

    def collideBall(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.dist(other) < self.radius + other.radius:
                                if not self.didBounceX:
                                    self.speedx = -self.speedx
                                    self.didBounceX = True
                                if not self.didBounceY:
                                    self.speedy = -self.speedy
                                    self.didBounceY = True
                                return True
        return False

    def dist(self, other):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = other.rect.center[0]
        y2 = other.rect.center[1]

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)