import pygame, sys, math

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

sounds = {"laser": pygame.mixer.Sound("Sounds/PlayerSounds/laser.ogg")}
