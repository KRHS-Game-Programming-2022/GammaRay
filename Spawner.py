import pygame, sys, math

class Spawner():
    def __init__(self, pos=[0,0]):
        self.image = pygame.image.load("Images/WallTiles/Spawner.png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "Spawner"
        
        
    def update(self, size):
       pass
        
class EnemySpawner():
    def __init__(self, pos=[0,0]):
        self.image = pygame.image.load("Images/WallTiles/EnemySpawner.png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "EnemySpawner"
        print ("WORK NOW", pos)
    def update(self, size):
        pass
