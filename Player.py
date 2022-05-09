import pygame, sys, math 
from Character import*
from Laser import*
from SpriteSheet import*

class PlayerChar(Char):
    def __init__(self, maxSpeed=20, startPos=[0,0]):
        Char.__init__(self, [0,0], startPos)
        spriteSheet = SpriteSheet("Images/Characters/Ray/test.png")
        self.normalImageList = {
            "left":spriteSheet.load_strip(pygame.Rect(0,300,100,150), 8, (0,0,0)),
            "right":spriteSheet.load_strip(pygame.Rect(0,150,100,150), 8, (0,0,0)),
            "down":spriteSheet.load_strip(pygame.Rect(207,0,100,150), 1, (0,0,0)),
            "up":spriteSheet.load_strip(pygame.Rect(0,300,100,150), 1, (0,0,0)),
            "left down":spriteSheet.load_strip(pygame.Rect(100,300,100,150), 1, (0,0,0)),
            "jump":spriteSheet.load_strip(pygame.Rect(400,0,100,150), 1, (0,0,0)),
            "left idle":spriteSheet.load_strip(pygame.Rect(101,0,100,150),1,(0,0,0)),
            "right idle":spriteSheet.load_strip(pygame.Rect(0,0,100,150), 1, (0,0,0)),
        }
        
        spriteSheet = SpriteSheet("Images/Characters/Ray/iFrames.png")
        self.invicibleImageList = {
            "left":spriteSheet.load_strip(pygame.Rect(0,300,100,150), 8, (0,0,0)),
            "right":spriteSheet.load_strip(pygame.Rect(0,150,100,150), 8, (0,0,0)),
            "down":spriteSheet.load_strip(pygame.Rect(207,0,100,150), 1, (0,0,0)),
            "up":spriteSheet.load_strip(pygame.Rect(0,300,100,150), 1, (0,0,0)),
            "left down":spriteSheet.load_strip(pygame.Rect(100,300,100,150), 1, (0,0,0)),
            "jump":spriteSheet.load_strip(pygame.Rect(400,0,100,150), 1, (0,0,0)),
            "left idle":spriteSheet.load_strip(pygame.Rect(101,0,100,150),1,(0,0,0)),
            "right idle":spriteSheet.load_strip(pygame.Rect(0,0,100,150), 1, (0,0,0)),
        }
        
        self.imageList = self.normalImageList
        self.imageKey = "right idle"
        self.images = self.imageList[self.imageKey]
        
        self.frame = 0
        self.frameMax = len(self.images) - 1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.imagesIdle = spriteSheet.image_at((0,0,100,150),(0,0,0))
       
        self.maxSpeed = maxSpeed
        self.kind = "Player"
        self.diry = "up"
        self.dirx = "right"
        self.lastdir = "up"
        
        self.gravity = 3
        self.jumping = False
        
        self.HP = 20
        self.living = True
        
              
        self.invincible = False
        self.iFrame = 0
        self.iFrameMax = 1*60;
        
        
        
        print (self.HP)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#Player Movement
    def goKey(self, direction):
        if direction == "left":
            self.dirx = direction
            self.lastdir = direction
            self.speedx = -self.maxSpeed
            self.imageKey = "left"
            self.frame = 0
        elif direction == "right":
            self.dirx = direction
            self.lastdir = direction
            self.speedx = self.maxSpeed
            self.imageKey = "right"
            self.frame = 0
        elif direction == "up":
            self.diry = direction
            self.lastdir = direction
            self.speedy = self.maxSpeed
            self.imageKey = "up"
            self.frame = 0
        elif direction == "down":
            self.diry = direction
            self.lastdir = direction
            self.speedy = self.maxSpeed
            self.imageKey = "down"
            self.frame = 0
        elif direction =="jump":
            self.diry = direction
            self.lastdir = direction
            if not self.jumping:
                self.speedy = -50
                self.move()
                self.imageKey = "jump"
                self.frame = 0
                # ~ print("--------Jump---------")
                self.jumping = True
        elif direction == "sleft":
            self.imageKey = "left idle"
            self.frame=0
            if self.dirx == "left":
                self.speedx = 0
        elif direction == "sright":
            self.imageKey = "right idle"
            self.frame=0
            if self.dirx == "right":
                self.speedx = 0
        elif direction == "sup":
            if self.diry == "up":
                self.speedy = 0
        elif direction == "sdown":
            if self.diry == "down":
                self.speedy = 0
        elif direction == "sjump":
            if self.diry == "jump":
                self.speedy = 0

    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#Player Laser
    def shoot(self):
        if self.lastdir == "up":
            return Laser(self.lastdir, [0,-25], [self.rect.centerx,self.rect.centery-50])
        if self.lastdir == "down":
            return Laser(self.lastdir, [0,25], [self.rect.centerx,self.rect.centery+50])
        if self.lastdir == "jump":
            return Laser(self.lastdir, [0,-25], [self.rect.centerx,self.rect.centery-50])
        if self.lastdir == "right":
            return Laser(self.lastdir, [25,0], [self.rect.centerx+50,self.rect.centery])
        if self.lastdir == "left":
            return Laser(self.lastdir, [-25,0], [self.rect.centerx-50,self.rect.centery])
        else: 
            print("BAD DIRECTION")
            return Laser(self.lastdir, [-25,0], [self.rect.centerx-50,self.rect.centery])
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    
    def update(self, size):
        self.move()
        
        
        self.animationTimer += 1
        self.animate()
        
        if self.HP <= 0:
            self.living = False
        if self.invincible:
            self.iFrame += 1
            if self.iFrame > self.iFrameMax:
                self.iFrame = 0
                self.invincible = False
                self.imageList = self.normalImageList
               
        
        return self.wallCollide(size)
        
    def animate(self):
        if self.animationTimer >= self.animationTimerMax:
            print(self.imageKey)
            self.images = self.imageList[self.imageKey]
            self.frameMax= len(self.images) - 1
            self.animationTimer = 0
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            print(self.frame, self.frameMax, len(self.images))
            self.image = self.images[self.frame]
    
    def move(self):
        self.speedy += self.gravity
        Char.move(self)

    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        
        if self.rect.bottom > size[1]:
            self.rect.bottom = size[1]
            self.speedy = 0
            # ~ print("hit botto")
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
            
    

    def enemyCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                if not self.invincible and other.kind != "Laser":
                                    self.HP -= 1
                                    print("HP is now: " + str(self.HP))
                                    self.invincible = True
                                    self.imageList = self.invicibleImageList
                                return True
        return False
