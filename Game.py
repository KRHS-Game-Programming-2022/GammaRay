import pygame, sys, math, random
from LevelLoader import *
from WallTile import*
from Enemy import*
from Player import*
from Hud import*
from Spawner import *
from Laser import*
from SpriteSheet import*
from Character import*
pygame.init()

if not pygame.font:
    print("Warning, fonts disabled")

    
clock = pygame.time.Clock();

size = [1300, 960]
screen = pygame.display.set_mode(size)




counter = 0;


level = 1
room = 1

tiles = loadLevel("Levels/Level"+str(level)+"-Room"+str(room)+".lvl")
walls = tiles [0]
spawners = tiles[1]

player = PlayerChar(15, spawners[0].rect.center)
chars = [player]

 
 
kills = 0
time = 0
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#Player movement
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_z:
                chars += [player.shoot()]
                print(len(chars))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
    time += 1
    counter += 1
    
    if counter >= 1:
        counter = 0;
        chars += [Char([random.randint(-7,7), random.randint(-7,7)],
                [random.randint(100, 700),random.randint(100, 500)])
        ]
        for char in chars:
            if chars[-1].charCollide(char):
             chars.remove(chars[-1])
             break   
            


        
        
        
    for char in chars:
        updateResult = char.update(size)
        if updateResult != None:
            if updateResult == "right":
                room += 1
                tiles = loadLevel("Levels/Level"+str(level)+"-Room"+str(room)+".lvl")
                walls = tiles [0]
                spawners = tiles[1]
                enemyspawners = tiles[2]
            elif updateResult == "left":
                room -= 1
                tiles = loadLevel("Levels/Level"+str(level)+"-Room"+str(room)+".lvl")
                walls = tiles [0]
                spawners = tiles[1]
                enemyspawners = tiles[2]

        
        
    for hittingChar in chars:
        for hitChar in chars:
            if hittingChar.charCollide(hitChar):
                if hitChar.charCollide(hittingChar):
                    kills += 1
                
                """
                if hitChar.kind != "Player":
                    if hittingChar.kind == "Laser":
                        hitChar.living = False
                        kills += 1
                """
        for wall in walls:
            hittingChar.wallTileCollide(wall)
                
    
    for char in chars:
        if not char.living:
            chars.remove(char)
            
        
        
        
        
        
    screen.fill((64, 128, 255))
    for spawner in spawners:
        screen.blit(spawner.image, spawner.rect)
    for char in chars:
        screen.blit(char.image, char.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60)
    #print(clock.get_fps())



