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
from Background import*
from Sounds import*
from LevelChanger import*

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()


if not pygame.font:
    print("Warning, fonts disabled")

    
clock = pygame.time.Clock();

size = [1300, 960]
screen = pygame.display.set_mode(size)



counter = 0;


level = 3 
room = 1

tiles = loadLevel("Levels/Level"+str(level)+"-Room"+str(room)+".lvl")
walls = tiles [0]
spawners = tiles[1]
interactables = tiles[2]

player = PlayerChar(15, spawners[0].rect.center)
chars = [player]

sounds = {"laser": pygame.mixer.Sound("Sounds/PlayerSounds/laser.ogg")}

bg=pygame.image.load("Images/Background/fake.png")
bgrect=bg.get_rect()

hud = Hud([0,0])

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
                sounds["laser"].play()
                chars += [player.shoot()]
            elif event.key == pygame.K_SPACE:
                player.goKey("jump")
                #print(len(chars))
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
    
    if counter >= 50:
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
                enemyspawners = tiles[0]
                interactables = tiles[2]
            elif updateResult == "left":
                room -= 1
                tiles = loadLevel("Levels/Level"+str(level)+"-Room"+str(room)+".lvl")
                walls = tiles [0]
                spawners = tiles[1]
                interactables = tiles[2]
                enemyspawners = tiles[0]

        
        
    for hittingChar in chars:
        for hitChar in chars:
            if hittingChar.kind == "Player":
                hittingChar.enemyCollide(hitChar)
            elif hittingChar.charCollide(hitChar):
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
            
        for interactable in interactables:
            if hittingChar.kind == "Player" and hittingChar.wallTileCollide(interactable):
                if interactable.kind == "LevelChanger":
                    level += interactable.direction
                    room = 1
                    tiles = loadLevel("Levels/Level"+str(level)+"-Room"+str(room)+".lvl")
                    walls = tiles [0]
                    spawners = tiles[1]
                    interactables = tiles[2]
                    enemyspawners = tiles[0]
                    player.rect.center = spawners[0].rect.center
                
                
    
    for char in chars:
        if not char.living:
            chars.remove(char)
            
        
    hud.update(player.HP)
        
        
        
    screen.fill((12,255,60))
    screen.blit(bg,bgrect)
    # ~ for bg in bgs:
        # ~ screen.blit(bg.image, bg.rect)
    for spawner in spawners:
        screen.blit(spawner.image, spawner.rect)
    for char in chars:
        screen.blit(char.image, char.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    for interactable in interactables:
        screen.blit(interactable.image, interactable.rect)
    screen.blit(hud.image,hud.rect)

    pygame.display.flip()
    clock.tick(60)
    #print(clock.get_fps())



