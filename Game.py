import pygame, sys, math, random
from LevelLoader import *
from WallTile import*
from Enemy import*
from Player import*
from Hud import*
from Spawner import *
from Laser import*
from SpriteSheet import*
pygame.init()

if not pygame.font:
    print("Warning, fonts disabled")

    
clock = pygame.time.Clock();

size = [1300, 960]
screen = pygame.display.set_mode(size)




counter = 0;




tiles = loadLevel("levels/1.lvl")
walls = tiles [0]
spawners = tiles[1]

player = Player(4, spawners[0].rect.center)
player = [player]
 
 
kills = 0
time = 0

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
                balls += [player.shoot()]
                print(len(balls))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")

    time += 1
    counter += 1
    if counter >= 10:
        counter = 0;
        balls += [Ball([random.randint(-7,7), random.randint(-7,7)],
                [random.randint(100, 700),random.randint(100, 500)])
        ]
        for ball in balls:
            if balls[-1].ballCollide(ball):
             balls.remove(balls[-1])
             break   
            
        
    for ball in balls:
        ball.update(size)
      
    timer.update(int(time/60))
    score.update(kills)
        
        
    for hittingBall in balls:
        for hitBall in balls:
            if hittingBall.ballCollide(hitBall):
                if hitBall.kind != "player":
                    if hittingBall.kind == "laser":
                        hitBall.living = False
                        kills += 1
        for wall in walls:
            hittingBall.wallTileCollide(wall)
                
    
    for ball in balls:
        if not ball.living:
            balls.remove(ball)
            
        
        
        
        
        
    screen.fill((64, 128, 255))
    for spawner in spawners:
        screen.blit(spawner.image, spawner.rect)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(score.image, score.rect)
    screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    clock.tick(60)
    #print(clock.get_fps())



