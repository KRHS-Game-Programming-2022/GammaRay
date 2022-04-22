import pygame, sys, math

class Char():
    def __init__(self, speed = [0,0], startPos=[0,0]):
        self.images = [pygame.image.load("Images/Characters/Enemies/Enemy1/ball1.png"),
                       pygame.image.load("Images/Characters/Enemies/Enemy1/ball2.png"),
                       pygame.image.load("Images/Characters/Enemies/Enemy1/ball3.png"),
                       pygame.image.load("Images/Characters/Enemies/Enemy1/ball2.png")]
                       
                       
        self.frame = 0
        self.frameMax = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx,self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        
        self.rect = self.rect.move(startPos)
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.kind = "Char"
        self.animationTimer = 0
        self.animationTimerMax = 60/10
        self.living = True
        
    def update(self, size):
        self.move()
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.wallCollide(size)
        self.animationTimer += 1
        self.animate()
        
    
    def move(self):
        
        self.speed = [self.speedx,self.speedy]
        self.rect = self.rect.move(self.speed)

        
    def animate(self):
        if self.animationTimer >= self.animationTimerMax:
            self.animationTimer = 0
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            #print(self.frame, self.frameMax, len(self.images))
            self.image = self.images[self.frame]
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > size[1]:
                self.speedy = -self.speedy
                self.didBounceY = True
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.didBounceY = True
        if not self.didBounceX:
            if self.rect.right > size[0]:
                self.speedx = -self.speedx
                self.didBounceX = True
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.didBounceX = True
            
            
            
            
            
    def charCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                if not self.didBounceX:
                                    self.speedx = -self.speedx
                                    self.didBounceX = True
                                if not self.didBounceY:
                                    self.speedy = -self.speedy
                                    self.didBounceY = True
                                if other.kind == "Laser" and self.kind != "Player":
                                    self.living = False
                                    return True
        return False
    
    def wallTileCollide(self, other):
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                            if not self.didBounceX:
                                self.speedx = -self.speedx
                                self.didBounceX = True
                            if not self.didBounceY:
                                self.speedy = -self.speedy
                                self.didBounceY = True
                            return True
        return False
        
        
        
        
    def getDist(self, other):
        x1 = self.rect.centerx 
        x2 = other.rect.centerx  
        y1 = self.rect.centery 
        y2 = other.rect.centery 
        return math.sqrt ((x2-x1)**2 + (y2-y1)**2)
