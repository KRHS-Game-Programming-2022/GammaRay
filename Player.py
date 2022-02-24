import pygame, sys, math 
from Character import*
from Laser import*
from SpriteSheet import*

class PlayerChar(Char):
    def __init__(self, maxSpeed=20, startPos=[0,0]):
        Char.__init__(self, [0,0], startPos)
        spriteSheet = SpriteSheet("Vision Board/soldier.png")
        self.imagesLeft = [pygame.image.load ("Images/Characters/Ray/Ray-left.png")]
        self.imagesRight = spriteSheet.load_strip(pygame.Rect(7,456,51,50), 8, (0,0,0))
        self.imagesUp = [pygame.image.load ("Images/Characters/Ray/Ray-up.png")]
        self.imagesDown = [pygame.image.load ("Images/Characters/Ray/Ray-down.png")]
        self.images = self.imagesUp
        self.frame = 0
        self.frameMax = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.maxSpeed = maxSpeed
        self.kind = "Player"
        self.diry = "up"
        self.dirx = "right"
        self.lastdir = "up"
        
        self.gravity = 3
        self.jumping = False
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#Player Movement
    def goKey(self, direction):
        if direction == "left":
            self.dirx = direction
            self.lastdir = direction
            self.speedx = -self.maxSpeed
            self.images = self.imagesLeft
            self.frame = 0
            self.frameMax = len(self.images) - 1
        elif direction == "right":
            self.dirx = direction
            self.lastdir = direction
            self.speedx = self.maxSpeed
            self.images = self.imagesRight
            self.frame = 0
            self.frameMax = len(self.images) - 1
        elif direction == "up":
            self.diry = direction
            self.lastdir = direction
            if not self.jumping:
                self.speedy = -50
                self.move()
                self.images = self.imagesUp
                self.frame = 0
                self.frameMax = len(self.images) - 1
                print("--------Jump---------")
                self.jumping = True
        elif direction == "down":
            self.diry = direction
            self.lastdir = direction
            self.speedy = self.maxSpeed
            self.images = self.imagesDown
            self.frame = 0
            self.frameMax = len(self.images) - 1
        elif direction == "sleft":
            if self.dirx == "left":
                self.speedx = 0
        elif direction == "sright":
            if self.dirx == "right":
                self.speedx = 0
        elif direction == "sup":
            if self.diry == "up":
                self.speedy = 0
        elif direction == "sdown":
            if self.diry == "down":
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
        if self.lastdir == "up":
            return Laser([0,-10+self.speedy], self.rect.center)
        if self.lastdir == "down":
            return Laser([0,10+self.speedy], self.rect.center)
        if self.lastdir == "right":
            return Laser([25+self.speedx,0], self.rect.center)
        if self.lastdir == "left":
            return Laser([-25+self.speedx,0], self.rect.center)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    
    def update(self, size):
        self.move()
        
        
        self.animationTimer += 1
        self.animate()
        
        return self.wallCollide(size)
    
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
            self.rect.left = 0
            return "right"
                
        if self.rect.left < 0:
            self.rect.right = size[0]
            return "left"
            
#Player Collision
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        #print("thit block")
                        xdiff = self.rect.centerx - other.rect.centerx
                        ydiff = self.rect.centery - other.rect.centery
                        #print(xdiff,ydiff)
                        if abs(xdiff) > abs(ydiff):    #Left/Right collsion
                            if xdiff < 0:
                                self.rect.right = other.rect.left-1
                                #print("\t==============hit left")
                            elif xdiff > 0:
                                self.rect.left = other.rect.right+1
                                #print("\t==============hit right")
                        else:                           #Up/Down collsions
                            if ydiff <0:
                                #print(self.rect.bottom, other.rect.top)
                                self.rect.bottom = other.rect.top-1
                                self.speedy = 0
                                self.jumping = False
                                #print("\thit top")
                            elif ydiff>0:
                                self.rect.top = other.rect.bottom + 1
                                self.speedy = 0
                                #print("\t============hit bottom")
                        
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
