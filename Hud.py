import pygame, sys, math
from SpriteSheet import*

class Hud():
    def __init__(self, baseText ,startPos=[0,0]):
        spriteSheet = SpriteSheet("Images\Characters\Ray\Hud\HealthBar.png")
        self.images = spriteSheet.images_at (100,100),(0,0,0)
        self.rect = self.image.get_rect(topleft = startPos)
        
    count = 19
    for i in range(count):
        print(i)

    
    def update(self, score):
        self.rect = self.image.get_rect(topleft = self.rect.topleft) 

