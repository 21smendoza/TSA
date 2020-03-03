import sys
import random
import pygame
import math

#initializes the program
pygame.init()
pygame.mixer.init()
dark_brown = (102, 51, 0)
light_brown = (153, 76, 0)
lightest_brown = (255, 229, 204)
black = (0, 0, 0)
grey = (96, 96, 96)

width = 1100
height = 650
screen = pygame.display.set_mode( (width, height) )
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
    
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    
    pygame.draw.rect(screen, light_brown, (0, 0, width, height / 1.3))
    pygame.draw.rect(screen, dark_brown, (0, height / 1.3, width, height / 1.8))
    pygame.draw.polygon(screen, lightest_brown, ((width / 9, 150), (width / 9 * 8, 150), (width / 22 * 21, 450), (width / 22, 450)))
    pygame.draw.line(screen, black, (int(round(width / 2)), 150), (int(round(width / 2)), 450), 3)
    pygame.draw.line(screen, black, (int(round(width / 4.8)), 150), (int(round(width / 6.2)), 450), 3)
    pygame.draw.line(screen, black, (int(round(width / 3.3)), 150), (int(round(width / 3.7)), 450), 3)
    pygame.draw.line(screen, black, (int(round(width / 2.5)), 150), (int(round(width / 2.6)), 450), 3)
    pygame.draw.line(screen, black, (int(round(width / 1.655)), 150), (int(round(width / 1.63)), 450), 3)
    pygame.draw.line(screen, black, (int(round(width / 1.261)), 150), (int(round(width / 1.19)), 450), 3)
    pygame.draw.line(screen, black, (int(round(width / 1.43)), 150), (int(round(width / 1.385)), 450), 3)
    pygame.draw.line(screen, black, (int(round(width / 10.6)), 225), (int(round(width / 1.105)), 225), 3)
    pygame.draw.line(screen, black, (int(round(width / 12.8)), 300), (int(round(width / 1.085)), 300), 3)
    pygame.draw.line(screen, black, (int(round(width / 16.2)), 375), (int(round(width / 1.067)), 375), 3)
    pygame.draw.rect(screen, grey, (width / 2 - 10, 130, 20, 350))

    pygame.display.update()
