import pygame, sys, math

class Projectile():
    def __init__(self, speed, size =[25, 25], pos=[0,0]):

        self.image = pygame.transform.scale(pygame.image.load("Images/Player Ball/player_shoot.png"), size)
        self.rect = self.image.get_rect(center = pos)
        self.radius = (self.rect.width + self.rect.height) / 4
        self.speed = self.speedx, self.speedy = speed

        self.didBounceX = False
        self.didBounceY = False

        self.kind = "shot"
        self.living = True

        #Pew Pew by DKnight556, https://soundbible.com/1949-Pew-Pew.html
        self.sound = pygame.mixer.Sound("Sounds/Pew.ogg")
        self.sound.play()


    def update(self, size):
        self.move()

        self.didBounceX = False
        self.didBounceY = False

        self.collideWall(size)




    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)


    def collideWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.right > width or self.rect.left < 0:
            self.living = False
        if self.rect.bottom > height or self.rect.top < 0:
            self.living = False

    def collideBall(self, other):
        if self != other and other.kind != "player":
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.dist(other) < self.radius + other.radius:
                                self.living = False

                                return True
        return False

    def collideWallTile(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        self.living = False
                        return True
        return False

    def dist(self, other):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = other.rect.center[0]
        y2 = other.rect.center[1]

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)