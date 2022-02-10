import pygame, sys, math
from WallTile import *
from Spawner import *
def loadLevel (lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = size/1
    tiles = []
    newLines = []
    walls = []
    spawners = []
    
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
    tiles = [walls,
            spawners]
    return tiles
    
    


#loadLevel("Levels/example.lvl")
