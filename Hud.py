import pygame, sys, math

class Hud():
    def __init__(self, baseText ,startPos=[0,0]):
        self.baseText= baseText
        self.font = pygame.font.Font(None, 36)
        self.images = [pygame.image.load ("images/Hud/TempHealth1", 1, (250, 50, 150))]
        self.rect = self.image.get_rect(topleft = startPos)
    
    def update(self, score):
        text = self.baseText + str(score)
        self.image = self.font.render(text, 1, (250, 50, 150))
        self.rect = self.image.get_rect(topleft = self.rect.topleft) 

