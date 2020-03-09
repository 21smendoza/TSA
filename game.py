import sys
import random
import pygame
import math

#initializes the program
pygame.init()
pygame.mixer.init()

#if statement will contain many of the variables for the code to run later on
if True:
    dark_brown = (102, 51, 0)
    brown = (120, 60, 30)
    light_brown = (153, 76, 0)
    lightest_brown = (255, 229, 204)
    black = (0, 0, 0)
    grey = (96, 96, 96)
    width = 1125
    height = 1000
    font_small = pygame.font.SysFont("comicsansms", 15)
    font_medium = pygame.font.SysFont("comicsansms", 25)
    title = font_medium.render("Volleyball Name Pending", True, black)
    play = font_small.render("Play", True, black)
    end_game = font_small.render("Quit", True, black)
    proceed = font_small.render("Continue", True, black)
    select = font_small.render("Pick three players to use. High attack makes the opposing receiver more likely to drop the ball. High defense makes the player less likely to drop the ball.", True, black)
    screen = pygame.display.set_mode( (width, height) )
    pygame.mouse.set_visible(False)
    #internal clock creates a slight delay to prevent program from speeding
    clock = pygame.time.Clock()
    run = True
    menu = True
    selection = True
    selection_2 = True
    selected = []
    all_sprites = pygame.sprite.Group()
    
pygame.display.flip()
class Cursor(pygame.sprite.Sprite):
    """Class for the sprite that follows and replaces the cursor"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((5, 5))
        self.rect = self.image.get_rect()
        self.rect.x = mouse[0]
        self.rect.y = mouse[1]
    def update(self):
        self.rect.x = mouse[0]
        self.rect.y = mouse[1]

class Menu_button(pygame.sprite.Sprite):
    """Class for the buttons on the menu screen"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)   
        self.image = pygame.Surface((150, 50))
        self.image.fill(dark_brown)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        click = pygame.sprite.spritecollide(self, cursor_group, False)
        if click:
            self.image.fill(grey)
        else:
            self.image.fill(dark_brown)

class Player_card(pygame.sprite.Sprite):
    """Class for the sprites of the cards that allows the user to choose characters"""
    def __init__(self, x, y, attack, defense):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((125, 175))
        self.image.fill(dark_brown)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.attack = attack
        self.defense = defense
    def update(self):
        click = pygame.sprite.spritecollide(self, cursor_group, False)
        if click:
            self.image.fill(grey)
        else:
            self.image.fill(dark_brown)

class Player_field(pygame.sprite.Sprite):
    """Class for the tiles on the player side"""
    def __init__(self, x, y, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((120, 120))
        self.image.fill(lightest_brown)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_pos = x_pos
        self.y_pos = y_pos
    def update(self):
        click = pygame.sprite.spritecollide(self, cursor_group, False)
        if click:
            self.image.fill(grey)
        else:
            self.image.fill(lightest_brown)

class Enemy_field(pygame.sprite.Sprite):
    """Class for the tiles on the enemy side"""
    def __init__(self, x, y, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((120, 120))
        self.image.fill(lightest_brown)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_pos = x_pos
        self.y_pos = y_pos
    def update(self):
        click = pygame.sprite.spritecollide(self, cursor_group, False)

class Character(pygame.sprite.Sprite):
    """Class for every character on the field"""
    def __init__(self, x, y, x_pos, y_pos, attack, defense):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((75, 100))
        self.image.fill(dark_brown)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_pos = x_pos
        self.y_pos = y_pos
    def update(self):
        click = pygame.sprite.spritecollide(self,cursor_group, False)
#these variables set up the sprites found in the menu portion of the game
mouse = pygame.mouse.get_pos()
play_button = Menu_button(500, 270)
quit_button = Menu_button(500, 400)
cursor_group = pygame.sprite.Group()
cursor = Cursor()
all_sprites.add(play_button)
all_sprites.add(quit_button)
all_sprites.add(cursor)
cursor_group.add(cursor)

#programs the menu portion of the game
while menu:
    clock.tick(120)
    
    for event in pygame.event.get():
        #exits the game when called to exit
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.sprite.spritecollide(play_button, cursor_group, False)
            for n in click:
                menu = False
            click = pygame.sprite.spritecollide(quit_button, cursor_group, False)
            for n in click:
                sys.exit()


    mouse = pygame.mouse.get_pos()
    play_button.update()
    quit_button.update()
    cursor.update()
    screen.fill(light_brown)
    all_sprites.draw(screen)
    screen.blit(title, (400, 100))
    screen.blit(play, (550, 290))
    screen.blit(end_game, (550, 420))
    pygame.display.update()


#these variables set up the sprites for the player selection portion of the game
all_sprites.remove(play_button, quit_button)
Player_cards = pygame.sprite.Group()
card_1 = Player_card(40, 100, 30, 70)
card_2 = Player_card(220, 100, 40, 60)
card_3 = Player_card(400, 100, 50, 50)
card_4 = Player_card(580, 100, 60, 40)
card_5 = Player_card(740, 100, 70, 30)
card_6 = Player_card(920, 100, 80, 20)
Player_cards.add(card_1, card_2, card_3, card_4, card_5, card_6)
proceed_button = Menu_button(475, 500)
all_sprites.add(proceed_button)


#programs the character selection portion of the game
while selection:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #checks to see what card is pressed, if 3 cards have already been pressed, and if the card itself had been pressed before
            click = pygame.sprite.spritecollide(card_1, cursor_group, False)
            for n in click:
                if 1 not in selected:
                    if len(selected) < 3:
                        selected.append(1)
                else:
                    selected.remove(1)
            click = pygame.sprite.spritecollide(card_2, cursor_group, False)
            for n in click:
                if 2 not in selected:
                    if len(selected) < 3:
                        selected.append(2)
                else:
                    selected.remove(2)
            click = pygame.sprite.spritecollide(card_3, cursor_group, False)
            for n in click:
                if 3 not in selected:
                    if len(selected) < 3:
                        selected.append(3)
                else:
                    selected.remove(3)
            click = pygame.sprite.spritecollide(card_4, cursor_group, False)
            for n in click:
                if 4 not in selected:
                    if len(selected) < 3:
                        selected.append(4)
                else:
                    selected.remove(4)
            click = pygame.sprite.spritecollide(card_5, cursor_group, False)
            for n in click:
                if 5 not in selected:
                    if len(selected) < 3:
                        selected.append(5)
                else:
                    selected.remove(5)
            click = pygame.sprite.spritecollide(card_6, cursor_group, False)
            for n in click:
                if 6 not in selected:
                    if len(selected) < 3:
                        selected.append(6)
                else:
                    selected.remove(6)
            click = pygame.sprite.spritecollide(proceed_button, cursor_group, False)
            for n in click:
                if len(selected) == 3:
                    selection = False
    #determines position based on if the card was selected, could be optimized by a lot
    if 1 in selected:
        card_1.rect.y = 300
    else:
        card_1.rect.y = 100
    if 2 in selected:
        card_2.rect.y = 300
    else:
        card_2.rect.y = 100
    if 3 in selected:
        card_3.rect.y = 300
    else:
        card_3.rect.y = 100
    if 4 in selected:
        card_4.rect.y = 300
    else:
        card_4.rect.y = 100
    if 5 in selected:
        card_5.rect.y = 300
    else:
        card_5.rect.y = 100
    if 6 in selected:
        card_6.rect.y = 300
    else:
        card_6.rect.y = 100
    mouse = pygame.mouse.get_pos()
    cursor.update()
    Player_cards.update()
    screen.fill(light_brown)
    Player_cards.draw(screen)
    all_sprites.draw(screen)
    cursor_group.draw(screen)
    screen.blit(select, (10, 10))
    #if the 3 cards are selected, then the option to continue becomes available
    if len(selected) == 3:
        screen.blit(proceed, (490, 510))
        proceed_button.update()
    pygame.display.update()

#removes all of the cards from the sprite group
Player_cards.empty()
Player_fields = pygame.sprite.Group()
Enemy_fields = pygame.sprite.Group()
all_sprites.remove(proceed_button)

#creates the location for each tile, which will allow position to determine the coordinates later

for x in range(0, 500, 125):
    for y in range(0, 500, 125):
        tile = Enemy_field(575+x, 175+y, x / 125 + 1, y / 125 + 1)
        Enemy_fields.add(tile)
        print(tile.x_pos, tile.y_pos)

for x in range(0, 500, 125):
    for y in range(0, 500, 125):
        tile = Player_field(50+x, 175+y, x / 125 + 1, y / 125 + 1)
        Player_fields.add(tile)
        print(tile.x_pos, tile.y_pos)



card_1 = Player_card(40, 700, 30, 70)
card_2 = Player_card(220, 700, 40, 60)
card_3 = Player_card(400, 700, 50, 50)
card_4 = Player_card(580, 700, 60, 40)
card_5 = Player_card(740, 700, 70, 30)
card_6 = Player_card(920, 700, 80, 20)

for card in selected:
    if card == 1:
        Player_cards.add(card_1)
    if card == 2:
        Player_cards.add(card_2)
    if card == 3:
        Player_cards.add(card_3)
    if card == 4:
        Player_cards.add(card_4)
    if card == 5:
        Player_cards.add(card_5)
    if card == 6:
        Player_cards.add(card_6)

selected = []
user_players = pygame.sprite.Group()
tiles_selected = []

#allows the player to select where to place their units on the field
while selection_2:
    clock.tick(120)

    for event in pygame.event.get():
        #exits the game when called to exit
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.sprite.spritecollide(card_1, cursor_group, False)
            for n in click:
                if 1 not in selected:
                    if len(selected) < 1:
                        selected.append(1)
                else:
                    selected.remove(1)
            click = pygame.sprite.spritecollide(card_2, cursor_group, False)
            for n in click:
                if 2 not in selected:
                    if len(selected) < 1:
                        selected.append(2)
                else:
                    selected.remove(2)
            click = pygame.sprite.spritecollide(card_3, cursor_group, False)
            for n in click:
                if 3 not in selected:
                    if len(selected) < 1:
                        selected.append(3)
                else:
                    selected.remove(3)
            click = pygame.sprite.spritecollide(card_4, cursor_group, False)
            for n in click:
                if 4 not in selected:
                    if len(selected) < 1:
                        selected.append(4)
                else:
                    selected.remove(4)
            click = pygame.sprite.spritecollide(card_5, cursor_group, False)
            for n in click:
                if 5 not in selected:
                    if len(selected) < 1:
                        selected.append(5)
                else:
                    selected.remove(5)
            click = pygame.sprite.spritecollide(card_6, cursor_group, False)
            for n in click:
                if 6 not in selected:
                    if len(selected) < 1:
                        selected.append(6)
                else:
                    selected.remove(6)
            #allows the placement of characters on new, unselected tiles based on what card is currently chosen
            click = pygame.sprite.spritecollide(cursor, Player_fields, False)
            for n in click:
                print(tiles_selected)
                if len(selected) == 1:
                    if 1 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125, n.x_pos, n.y_pos, 30, 70)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_1)
                            tiles_selected.append(n)
                    if 2 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125, n.x_pos, n.y_pos, 40, 60)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_2)
                            tiles_selected.append(n)
                    if 3 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125, n.x_pos, n.y_pos, 50, 50)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_3)
                            tiles_selected.append(n)
                    if 4 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125, n.x_pos, n.y_pos, 60, 40)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_4)
                            tiles_selected.append(n)
                    if 5 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125, n.x_pos, n.y_pos, 70, 30)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_5)
                            tiles_selected.append(n)
                    if 6 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125, n.x_pos, n.y_pos, 80, 20)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_6)
                            tiles_selected.append(n)


    #determines position based on if the card was selected, could be optimized by a lot
    if 1 in selected:
        card_1.rect.y = 800
    else:
        card_1.rect.y = 725
    if 2 in selected:
        card_2.rect.y = 800
    else:
        card_2.rect.y = 725
    if 3 in selected:
        card_3.rect.y = 800
    else:
        card_3.rect.y = 725
    if 4 in selected:
        card_4.rect.y = 800
    else:
        card_4.rect.y = 725
    if 5 in selected:
        card_5.rect.y = 800
    else:
        card_5.rect.y = 725
    if 6 in selected:
        card_6.rect.y = 800
    else:
        card_6.rect.y = 725
    
    mouse = pygame.mouse.get_pos()
    
    pygame.draw.rect(screen, light_brown, (0, 0, width, height / 1.3))
    pygame.draw.rect(screen, brown, (0, height / 1.4, width, height / 1.8))
    Player_fields.update()
    Enemy_fields.update()
    Enemy_fields.draw(screen)
    Player_fields.draw(screen)
    Player_cards.update()
    Player_cards.draw(screen)
    user_players.update()
    user_players.draw(screen)
    cursor.update()
    cursor_group.draw(screen)

    if len(Player_cards) == 0:
        selection_2 = False

    pygame.display.update()

#begin the game bois!
while run:
    clock.tick(120)

    for event in pygame.event.get():
        #exits the game when called to exit
        if event.type == pygame.QUIT:
            sys.exit()
    
    mouse = pygame.mouse.get_pos()
    
    
    pygame.draw.rect(screen, light_brown, (0, 0, width, height / 1.3))
    pygame.draw.rect(screen, brown, (0, height / 1.4, width, height / 1.8))
    Player_fields.update()
    Enemy_fields.update()
    Enemy_fields.draw(screen)
    Player_fields.draw(screen)
    Player_cards.update()
    Player_cards.draw(screen)
    user_players.update()
    user_players.draw(screen)
    cursor.update()
    cursor_group.draw(screen)

    pygame.display.update()