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
    yellow = (218, 165, 32)
    blue = (0, 64, 255)
    red = (153, 0, 0) #for the 2 up 2 right
    pink = (204, 0, 255) # for the 2 up 2 left
    purple = (102, 0, 255) # for the 1 up 1 right
    dark_blue = (0, 51, 204) # for the 1 up 1 left
    light_blue = (0, 255, 255) #for the 2 down 2 right
    light_green = (0, 204, 102) #for the 2 down 2 left
    dark_green = (0, 102, 0) #for the 1 down 1 right
    dark_yellow = (204, 204, 0) #for the 1 down 1 left
    orange = (255, 153, 0) #for the 2 right
    burnt = (153, 51, 0) #for the 2 left
    light_purple = (204, 204, 255) #for the 2 up
    light_pink = (255, 204, 255) #for the 2 down
    width = 1125
    height = 1000
    player_score = 0
    enemy_score = 0
    font_small = pygame.font.SysFont("comicsansms", 15)
    font_medium = pygame.font.SysFont("comicsansms", 25)
    title = font_medium.render("Volleyball Name Pending", True, black)
    play = font_small.render("Play", True, black)
    end_game = font_small.render("Quit", True, black)
    proceed = font_small.render("Continue", True, black)
    select = font_small.render("Pick three players to use. High attack makes the opposing receiver more likely to drop the ball. High defense makes the player less likely to drop the ball.", True, black)
    selecting = font_small.render("Pick a card, and pick the tile that you would like to place them in. After placement, you will be unable to switch positions.", True, black)
    server = font_small.render("Pick a character to serve the ball.", True, black)
    screen = pygame.display.set_mode( (width, height) )
    pygame.mouse.set_visible(False)
    #internal clock creates a slight delay to prevent program from speeding
    clock = pygame.time.Clock()
    run = True
    menu = True
    selection = True
    selection_2 = True
    selected = []
    menu_buttons = pygame.sprite.Group()
    timer = 0
    moving = False
    occupied = False
    move_count = 0
    
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
        #if touching cursor, changes color
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
        #if touching cursor, changes color
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
        self.movable = False
        self.color = lightest_brown
    def toss_options(self, x, y):
        x_location = self.x_pos + x
        y_location = self.y_pos + y
        return (x_location, y_location)
    def move_options(self, x, y):
        global moving
        moving = True
        if self.x_pos == x:
            if self.y_pos == y + 1 or self.y_pos == y - 1:
                self.image.fill(blue)
                self.movable = True
        elif self.x_pos == x + 1 or self.x_pos == x - 1:
            if self.y_pos == y:
                self.image.fill(blue)
                self.movable = True
    def resolve(self, x, y):
        global moving
        moving = False
        if self.x_pos == x:
            if self.y_pos == y + 1 or self.y_pos == y - 1:
                self.image.fill(self.color)
                self.moveable = False
        elif self.x_pos == x + 1 or self.x_pos == x - 1:
            if self.y_pos == y:
                self.image.fill(self.color)
                self.moveable = False
    def update(self):
        #if touching cursor, changes color
        global moving
        if not moving:
            click = pygame.sprite.spritecollide(self, cursor_group, False)
            if click:
                self.image.fill(grey)
            else:
                self.image.fill(self.color)

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
        #place holder (this class is not interactable with cursor)
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
        self.hp = 100
        self.picked = False
    def move(self, x_in, y_in):
        global move_count
        move_count += 1
        if self.picked:
            self.x_pos += x_in
            self.y_pos += y_in
            self.rect.x = self.x_pos * 125 - 52.5
            self.rect.y = self.y_pos * 125 + 25
        
    def update(self):
        #placeholder code after
        click = pygame.sprite.spritecollide(self,cursor_group, False)

class Movement_card(pygame.sprite.Sprite):
    """Class for the cards that choose movement"""
    def __init__(self, x, y, x_mov, y_mov, color, order):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 150))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_mov = x_mov
        self.y_mov = y_mov
        self.order = order
    def update(self):
        global selected
        if self.order in selected:
            self.rect.y = 800
        else:
            self.rect.y = 775
        click = pygame.sprite.spritecollide(self, cursor_group, False)
        if click:
            self.image.fill(grey)
        else:
            self.image.fill(self.color)

class Ball(pygame.sprite.Sprite):
    """Class for the volleyball that will move back and forth"""
    def __init__(self, x, y, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_pos = x_pos
        self.y_pos = y_pos
    def wait(self, x, y):
        self.rect.x = x
        self.rect.y = y
    def toss(self, x_in, y_in):
        self.x_pos = x_in
        self.y_pos = y_in
        self.rect.x = x_in * 125
        self.rect.y = y_in * 125 + 15
    def update(self):
        #placeholder code after
        click = 1

#these variables set up the sprites found in the menu portion of the game
mouse = pygame.mouse.get_pos()
play_button, quit_button = Menu_button(500, 270), Menu_button(500, 400)
cursor_group = pygame.sprite.Group()
cursor = Cursor()
menu_buttons.add(play_button)
menu_buttons.add(quit_button)
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
    menu_buttons.update()
    cursor.update()
    screen.fill(light_brown)
    menu_buttons.draw(screen)
    cursor_group.draw(screen)
    screen.blit(title, (400, 100))
    screen.blit(play, (550, 290))
    screen.blit(end_game, (550, 420))
    pygame.display.update()


#these variables set up the sprites for the player selection portion of the game
menu_buttons.remove(play_button, quit_button)
Player_cards = pygame.sprite.Group()
card_1 = Player_card(45, 100, 30, 70)
card_2 = Player_card(230, 100, 40, 60)
card_3 = Player_card(415, 100, 50, 50)
card_4 = Player_card(600, 100, 60, 40)
card_5 = Player_card(765, 100, 70, 30)
card_6 = Player_card(950, 100, 80, 20)
Player_cards.add(card_1, card_2, card_3, card_4, card_5, card_6)
proceed_button = Menu_button(475, 500)
menu_buttons.add(proceed_button)


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
    #updates and draws all sprites onto the screen
    cursor.update()
    Player_cards.update()
    screen.fill(light_brown)
    Player_cards.draw(screen)
    menu_buttons.draw(screen)
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

#creates the location for each tile

for x in range(0, 500, 125):
    for y in range(0, 500, 125):
        tile = Enemy_field(575+x, 175+y, x / 125 + 1, y / 125 + 1)
        Enemy_fields.add(tile)

for x in range(0, 500, 125):
    for y in range(0, 500, 125):
        tile = Player_field(50+x, 175+y, x / 125 + 1, y / 125 + 1)
        Player_fields.add(tile)


#set up for selectable cards
card_1 = Player_card(45, 700, 30, 70)
card_2 = Player_card(230, 700, 40, 60)
card_3 = Player_card(415, 700, 50, 50)
card_4 = Player_card(600, 700, 60, 40)
card_5 = Player_card(765, 700, 70, 30)
card_6 = Player_card(950, 700, 80, 20)

#adds cards to second phase of selection based on if they were selected before
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
            #if no other card is already selected, selects the clicked card
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
                if len(selected) == 1:
                    if 1 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125 + 25, n.x_pos, n.y_pos, 30, 70)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_1)
                            tiles_selected.append(n)
                    if 2 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125 + 25, n.x_pos, n.y_pos, 40, 60)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_2)
                            tiles_selected.append(n)
                    if 3 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125 + 25, n.x_pos, n.y_pos, 50, 50)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_3)
                            tiles_selected.append(n)
                    if 4 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125 + 25, n.x_pos, n.y_pos, 60, 40)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_4)
                            tiles_selected.append(n)
                    if 5 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125 + 25, n.x_pos, n.y_pos, 70, 30)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_5)
                            tiles_selected.append(n)
                    if 6 in selected:
                        if n not in tiles_selected:
                            Player = Character(n.x_pos * 125 - 52.5, n.y_pos * 125 + 25, n.x_pos, n.y_pos, 80, 20)
                            user_players.add(Player)
                            selected = []
                            Player_cards.remove(card_6)
                            tiles_selected.append(n)


    #determines position based on if the card was selected, could be optimized by a lot
    if 1 in selected:
        card_1.rect.y = 775
    else:
        card_1.rect.y = 750
    if 2 in selected:
        card_2.rect.y = 775
    else:
        card_2.rect.y = 750
    if 3 in selected:
        card_3.rect.y = 775
    else:
        card_3.rect.y = 750
    if 4 in selected:
        card_4.rect.y = 775
    else:
        card_4.rect.y = 750
    if 5 in selected:
        card_5.rect.y = 775
    else:
        card_5.rect.y = 750
    if 6 in selected:
        card_6.rect.y = 775
    else:
        card_6.rect.y = 750
    
    mouse = pygame.mouse.get_pos()
    #more drawing code for the sprites
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
    screen.blit(selecting, (10, 10))
    cursor.update()
    cursor_group.draw(screen)
    #stops loop if all cards have been placed
    if len(Player_cards) == 0:
        selection_2 = False

    pygame.display.update()

#setting up variables for game
selected = []
Movement_cards = pygame.sprite.Group()
serving = True
ball_group = pygame.sprite.Group()
#always starting with player
enemy_turn = False
enemy_move = False
player_turn = True
player_turn_2 = False
player_move = False
#creates an enemy player for every enemy tile, just here to test for position detection without actually programming the enemy AI yet!
Enemy_players = pygame.sprite.Group()
for x in range (0, 500, 125):
    for y in range (0, 500, 125):
        enemy = Character(600 + x, 150 + y, x / 125 + 5, y / 125 + 1, 50, 50)
        Enemy_players.add(enemy)
# sets up the first run of the movement card deck
for x in range(85, 1085, 200):
    random_card = random.randint(1, 12)
    if random_card == 1:
        move_card = Movement_card(x, 775, 2, -2, red, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 2:
        move_card = Movement_card(x, 775, -2, -2, pink, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 3:
        move_card = Movement_card(x, 775, 1, -1, purple, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 4:
        move_card = Movement_card(x, 775, -1, -1, dark_blue, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 5:
        move_card = Movement_card(x, 775, 2, 2, light_blue, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 6:
        move_card = Movement_card(x, 775, -2, 2, light_green, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 7:
        move_card = Movement_card(x, 775, 1, 1, dark_green, (x - 85) / 200+ 1)
        Movement_cards.add(move_card)
    if random_card == 8:
        move_card = Movement_card(x, 775, -1, 1, dark_yellow, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 9:
        move_card = Movement_card(x, 775, 2, 0, orange, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 10:
        move_card = Movement_card(x, 775, -2, 0, burnt, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 11:
        move_card = Movement_card(x, 775, 0, -2, light_purple, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)
    if random_card == 12:
        move_card = Movement_card(x, 775, 0, 2, light_pink, (x - 85) / 200 + 1)
        Movement_cards.add(move_card)

#begin the game bois!
while run:
    clock.tick(120)

    for event in pygame.event.get():
        #exits the game when called to exit
        if event.type == pygame.QUIT:
            sys.exit()
    
    #starts each player round by selecting a player to serve the ball
    while serving:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if the tiles are clicked, it checks if a character is on it; if there is, then they are selected to serve
                click = pygame.sprite.spritecollide(cursor, Player_fields, False)
                for n in click:
                    for characters in user_players:
                        if characters.x_pos == n.x_pos and characters.y_pos == n.y_pos:
                            ball = Ball(characters.x_pos * 125 - 25, characters.y_pos * 125 + 15, characters.x_pos, characters.y_pos)
                            ball_group.add(ball)
                            enemy_turn = True
                            serving = False
        #updates the sprites and draws them
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
        screen.blit(server, (10,10))
        Enemy_players.draw(screen)
        ball_group.update()
        ball_group.draw(screen)
        cursor.update()
        cursor_group.draw(screen)
        pygame.display.update()
        if not serving:
            #time delay is a placeholder until we have the physics working
            pygame.time.delay(500)
            ball.wait(width/ 2.049, ball.y_pos * 125)
    #like player serving, except randomly chosen and for the computer instead
    #while returning:
    timer = 0

    while enemy_turn:
        clock.tick(120)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        for all in Player_fields:
            all.color = lightest_brown

        ball_group.update()
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
        Enemy_players.update()
        Enemy_players.draw(screen)
        ball_group.draw(screen)
        cursor_group.draw(screen)
        pygame.display.update()
        timer += 1
        if timer > 250:
            for enemies in Enemy_players:
                if enemies.x_pos == ball.x_pos + 4:
                    if enemies.y_pos == ball.y_pos:
                        ball.toss(enemies.x_pos, enemies.y_pos)
                        player_turn = True
                        enemy_turn = False
    
    timer = 0
    move_count = 0
    
    #starts the player movement section of the player turn
    while player_turn:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = pygame.sprite.spritecollide(cursor, Player_fields, False)
                if move_count < 3:
                    if not moving:
                        if 1 not in selected:
                            for tile in clicked:
                                for characters in user_players:
                                    if characters.x_pos == tile.x_pos and characters.y_pos == tile.y_pos:
                                        for tiles in Player_fields:
                                            tiles.move_options(characters.x_pos, characters.y_pos)
                                            characters.picked = True
                            selected.append(1)
                        else:
                            selected.remove(1)
                            for tile in Player_fields:
                                for characters in user_players:
                                    if characters.x_pos == tile.x_pos and characters.y_pos == tile.y_pos:
                                        for tiles in Player_fields:
                                            tiles.resolve(characters.x_pos, characters.y_pos)
                                            characters.picked = False
                                            occupied = False
                                            moving = False
                    else:
                        for tile in clicked:
                            for characters in user_players:
                                if characters.x_pos == tile.x_pos:
                                    if characters.y_pos == tile.y_pos + 1 or characters.y_pos == tile.y_pos - 1:
                                        for everyone in user_players:
                                            if everyone.x_pos == tile.x_pos and everyone.y_pos == tile.y_pos:
                                                occupied = True
                                        if characters.picked and not occupied:
                                            characters.move(tile.x_pos - characters.x_pos, tile.y_pos - characters.y_pos)
                                            tile.movable = False
                                            moving = False
                                            occupied = False
                                if characters.y_pos == tile.y_pos:
                                    if characters.x_pos == tile.x_pos + 1 or characters.x_pos == tile.x_pos - 1:
                                        for everyone in user_players:
                                            if everyone.x_pos == tile.x_pos and everyone.y_pos == tile.y_pos:
                                                occupied = True
                                        if characters.picked and not occupied:
                                            characters.move(tile.x_pos - characters.x_pos, tile.y_pos - characters.y_pos)
                                            tile.movable = False
                                            moving = False
                                            occupied = False
                        occupied = False

        if move_count == 2:
            player_turn = False
            player_turn_2 = True
        ball_group.update()
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
        Enemy_players.update()
        Enemy_players.draw(screen)
        ball_group.draw(screen)
        cursor_group.draw(screen)
        pygame.display.update()
    #starts the movement card section of the player turn
    selected = []
    first_done = False
    second_done = False

    while player_turn_2:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = pygame.sprite.spritecollide(cursor, Movement_cards, False)
                for n in clicked:
                    if not selected:
                        if n.order == 1:
                            selected.append(1)
                        if n.order == 2:
                            selected.append(2)
                        if n.order == 3:
                            selected.append(3)
                        if n.order == 4:
                            selected.append(4)
                        if n.order == 5:
                            selected.append(5)
                    else:
                        selected.clear()
                print(selected)
                click = pygame.sprite.spritecollide(cursor, Player_fields, False)
                if selected:
                    for tiles in click:
                        if tiles.color != red:
                            for all in Player_fields:
                                all.color = lightest_brown
                            for characters in user_players:
                                if characters.x_pos == tiles.x_pos and characters.y_pos == tiles.y_pos:
                                    location = tiles.toss_options(n.x_mov, n.y_mov)
                                    for tile in Player_fields:
                                        if tile.x_pos == location[0] and tile.y_pos == location[1]:
                                            tile.color = red
                                            tile.image.fill(red)
                                            first_throw = (tile.x_pos, tile.y_pos)
                        else:
                            for all in Player_fields:
                                if all.color != red:
                                    all.color = lightest_brown
                                for characters in user_players:
                                    if characters.x_pos == tiles.x_pos and characters.y_pos == tiles.y_pos:
                                        location = tiles.toss_options(n.x_mov, n.y_mov)
                                        for tile in Player_fields:
                                            if tile.x_pos == location[0] and tile.y_pos == location[1]:
                                                tile.color =  burnt
                                                tile.image.fill(burnt)
                                                for characters in user_players:
                                                    if characters.x_pos == tile.x_pos and characters.y_pos == tile.y_pos:
                                                        second_throw = (tile.x_pos, tile.y_pos)
                                                        player_move = True
                                                        player_turn_2 = False

        ball_group.update()
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
        Enemy_players.update()
        Enemy_players.draw(screen)
        ball_group.draw(screen)
        Movement_cards.update()
        Movement_cards.draw(screen)
        cursor_group.draw(screen)
        pygame.display.update()

    timer = 0

    while player_move:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        timer += 1
        if timer < 150:
            ball.toss(first_throw[0], first_throw[1])
        if timer >= 150 and timer < 300:
            ball.toss(second_throw[0], second_throw[1])
        if timer >= 300:
            ball.wait(width/ 2.049, ball.y_pos * 125)
            player_move = False
            enemy_turn = True
        ball_group.update()
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
        Enemy_players.update()
        Enemy_players.draw(screen)
        ball_group.draw(screen)
        cursor_group.draw(screen)
        pygame.display.update()

        
        
    #updates and draws the sprites
    ball_group.update()
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
    Enemy_players.update()
    Enemy_players.draw(screen)
    ball_group.draw(screen)
    cursor_group.draw(screen)

    pygame.display.update()