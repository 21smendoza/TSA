import sys
import random
import pygame
import math

#initializes the program
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode( (800, 600) )
#internal clock creates a slight delay to prevent program from speeding
clock = pygame.time.Clock()

pygame.display.flip()

run = True

#begin the game bois!
while run:
    clock.tick(60)

    for event in pygame.event.get():
        #exits the game when called to exit
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
