import pygame, sys, math
from Ball import*
class PlayerBall(Ball):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self,"player.png", [0,0], [100,100], startPos)
        self.maxSpeed = maxSpeed

    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "up":
            self.speedy = -self.maxSpeed
        elif direction == "down":
            self.speedy = self.maxSpeed

        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            self.speedy = 0
        elif direction == "sdown":
            self.speedy = 0

        self.speed = [self.speedx, self.speedy]
        print(self.maxSpeed, direction, self.speed)

    def collideWall(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceX:
            if self.rect.right > width or self.rect.left < 0:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
        if not self.didBounceY:
            if self.rect.bottom > height or self.rect.top < 0:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
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
                                    self.move()
                                    self.speedx = 0
                                    self.didBounceX = True
                                if not self.didBounceY:
                                    self.speedy = -self.speedy
                                    self.move()
                                    self.speedy = 0
                                    self.didBounceY = True
                                return True
        return False
