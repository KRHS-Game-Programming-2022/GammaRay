import pygame, sys, math
from WallTile import *
from Spawner import *
from LevelChanger import *
def loadLevel (lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = size/6
    tiles = []
    newLines = []
    walls = []
    spawners = []
    enemyspawners = []
    interactables = []
    
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":   
                newLine += c
        newLines += [newLine]
        
    lines = newLines
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls += [Wall([x*size+offset, y*size+offset])]
            if c == "X":
                spawners += [Spawner([x*size+offset, y*size+offset])]
            if c == "E":
                spawners += [EnemySpawner([x*size+offset, y*size+offset])]
            if c == "+":
                interactables += [LevelChanger([x*size+offset, y*size+offset], 1)]
    tiles = [walls,
            spawners,
            interactables]
    return tiles
    
    


#loadLevel("Levels/example.lvl")
