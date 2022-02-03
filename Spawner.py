import pygame, sys, math

class Spawner():
    def __init__(self, pos=[650,480]):
        self.image = pygame.image.load("Images/WallTiles/Spawner.png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "Spawner"
        
        
    def update(self, size):
       pass
        

