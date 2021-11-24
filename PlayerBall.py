import pygame, sys, math
from Ball import*
class PlayerBall(Ball):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], [100,100], startPos)
        self.imagesUp = [pygame.image.load("Images/Player Ball/player_up.png")]
        self.imagesDown = [pygame.image.load("Images/Player Ball/player_down.png")]
        self.imagesLeft = [pygame.image.load("Images/Player Ball/player_left.png")]
        self.imagesRight = [pygame.image.load("Images/Player Ball/player_right.png")]
        self.maxSpeed = maxSpeed
        self.images = self.imagesUp
        self.frame = 0
        self.frameMax = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(topleft=startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2) / 2
        self.kind = "player"


    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.images = self.imagesLeft
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.images = self.imagesRight
        if direction == "up":
            self.speedy = -self.maxSpeed
            self.images = self.imagesUp
        elif direction == "down":
            self.speedy = self.maxSpeed
            self.images = self.imagesDown


        if direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        if direction == "sup":
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
                                return True
        return False

    def collideWallTile(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.speedx = -self.speedx
                        self.speedy = -self.speedy
                        self.move()
                        self.speedx = 0
                        self.speedy = 0
                        self.didBounceX = True
                        self.didBounceY = True
        return False




