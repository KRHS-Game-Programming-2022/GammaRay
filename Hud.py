import pygame, sys, math
from SpriteSheet import*

class Hud():
    def __init__(self ,startPos=[0,0]):
        self.sheet = SpriteSheet("Images\Characters\Ray\Hud\HealthBar.png")
        self.rects = []
        for y in range(0,600,200):
            for x in range(0, 1800, 200):
                self.rects += [pygame.Rect(x,y,200,200)]
        self.rects = self.rects[0:19]
        self.images = self.sheet.images_at(self.rects,(0,0,50))
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = startPos)
        #self.image.blit(self.sheet, (0, 0), self.rect)
        self.counter = 0;
        self.frame = 0
        
        
    

    
    def update(self):
        #self.rect = self.image.get_rect(topleft = self.rect.topleft) 
        self.counter += 1
        if self.counter > 15:
            self.counter = 0
            self.frame += 1
            if self.frame >= len(self.images):
                self.frame = 0
            self.image = self.images[self.frame]
            #print(self.frame)
            

        

