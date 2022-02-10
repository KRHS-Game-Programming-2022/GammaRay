import pygame, sys, math 
from Character import*
from Laser import*

class PlayerChar(Char):
    def __init__(self, maxSpeed=20, startPos=[0,0]):
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
        self.kind = "Player"
        self.dir = "up"
        
        self.gravity = 3
        self.jumping = False
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#Player Movement
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
            if not self.jumping:
                self.speedy = -50
                self.move()
                self.images = self.imagesUp
                print("--------Jump---------")
                self.jumping = True
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
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#Player Health
    def health(self):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                
                                return True
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#Player Laser
    def shoot(self):
        if self.dir == "up":
            return Laser([0,-10], self.rect.center)
        if self.dir == "down":
            return Laser([0,10], self.rect.center)
        if self.dir == "right":
            return Laser([10,0], self.rect.center)
        if self.dir == "left":
            return Laser([-10,0], self.rect.center)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    
    def move(self):
        self.speedy += self.gravity
        Char.move(self)

    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.bottom > size[1]:
            self.rect.bottom = size[1]
            self.speedy = 0
            print("hit botto")
            self.jumping = False
        
        if self.rect.top < 0:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
    
        if self.rect.right > size[0]:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
        if self.rect.left < 0:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
#Player Collision
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        print("thit block")
                        xdiff = self.rect.centerx - other.rect.centerx
                        ydiff = self.rect.centery - other.rect.centery
                        print(xdiff,ydiff)
                        if abs(xdiff) > abs(ydiff):    #Left/Right collsion
                            if xdiff < 0:
                                self.rect.right = other.rect.left-1
                                print("\t==============hit left")
                            elif xdiff > 0:
                                self.rect.left = other.rect.right+1
                                print("\t==============hit right")
                        else:                           #Up/Down collsions
                            if ydiff <0:
                                print(self.rect.bottom, other.rect.top)
                                self.rect.bottom = other.rect.top-1
                                self.speedy = 0
                                self.jumping = False
                                print("\thit top")
                            elif ydiff>0:
                                self.rect.top = other.rect.bottom + 1
                                self.speedy = 0
                                print("\t============hit bottom")
                        
                        return True
        return False
            

    # ~ def EnemyCollide(self, other):
        # ~ if self != other:
            # ~ if self.rect.right > other.rect.left:
                # ~ if self.rect.left < other.rect.right:
                    # ~ if self.rect.bottom > other.rect.top:
                        # ~ if self.rect.top < other.rect.bottom:
                            # ~ if self.getDist(other) < self.rad + other.rad:
                                
                                # ~ return True
        # ~ return False
