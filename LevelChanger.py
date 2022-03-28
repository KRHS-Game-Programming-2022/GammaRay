import pygame, sys, math

class LevelChanger():
    def __init__(self, pos=[0,0], direction=1):
        self.direction = direction
        if self.direction > 0:
            self.image = pygame.image.load("Images/WallTiles/LevelUp.png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "LevelChanger"
        
        
    def update(self, size):
       pass
        
