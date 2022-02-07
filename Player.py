import pygame, sys, math 
from Character import*
from Laser import*

class PlayerChar(Char):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Char.__init__(self, [0,0], startPos)
        self.imagesLeft = [pygame.image.load ("Images/Characters/Ray/Ray-left.png")]
        self.imagesRight = [pygame.image.load ("Images/Characters/Ray/Ray-right.png")]
        self.imagesUp = [pygame.image.load ("Images/Characters/Ray/Ray-up.png")]
        self.imagesDown = [pygame.image.load ("Images/Characters/Ray/Ray-down.png")]
        self.images = self.imagesUp
        self.frame = 0
        self.frameMax = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.maxSpeed = maxSpeed
        self.kind = "player"
        self.dir = "up"
        
    def goKey(self, direction):
        if direction == "left":
            self.dir = direction
            self.speedx = -self.maxSpeed
            self.images = self.imagesLeft
        elif direction == "right":
            self.dir = direction
            self.speedx = self.maxSpeed
            self.images = self.imagesRight
        elif direction == "up":
            self.dir = direction
            self.speedy = -self.maxSpeed
            self.images = self.imagesUp
        elif direction == "down":
            self.dir = direction
            self.speedy = self.maxSpeed
            self.images = self.imagesDown
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            self.speedy = 0
        elif direction == "sdown":
            self.speedy = 0
            

    def health(self):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                
                                return True
    def shoot(self):
        if self.dir == "up":
            return Laser([0,-10], self.rect.center)
        if self.dir == "down":
            return Laser([0,10], self.rect.center)
        if self.dir == "right":
            return Laser([10,0], self.rect.center)
        if self.dir == "left":
            return Laser([-10,0], self.rect.center)

    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > size[1]:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
        
        if not self.didBounceX:
            if self.rect.right > size[0]:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
            

    def EnemyCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                
                                return True
        return False
