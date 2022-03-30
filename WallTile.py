import pygame, sys, math

class Wall():
    def __init__(self, pos=[25,25]):
        self.image = pygame.image.load("images/WallTiles/real.png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "wall"
        
    def update(self, size):
       pass
        
