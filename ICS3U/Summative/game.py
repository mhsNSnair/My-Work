"""
course: ICS3U
filename: Nicholas_ICS3U_Final
date: 07/19/20
name: Nicholas Snair
description: This program is a pong game where you can play against the computer or aginst someone else.
"""

import pygame, sys, random, math #Imports the modules needed to make the game run

clock = pygame.time.Clock()#Creates a clock so that the game can have frames per second

from pygame.locals import *
pygame.init() # initiates pygame

pygame.display.set_caption('Pong Game') #Name for the window

WINDOW_SIZE = (1024,768)#Size of the window

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

font = pygame.font.SysFont(None, 40)

pygame.mixer.music.load('Sounds/onedreamerpong.mp3') # I do NOT take credit for the music used. One Dreamer: Prologue.
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1)

def draw_text(text, font, color, surface, x, y):
    """
    A function for drawing text on screen
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Button:
    """
    Class to get rectangles to use as buttons
    """
    def __init__(self, x, y):#Defines postion variables
        self.x = x
        self.y = y
    def update(self):#Draws the object on to the screen to update its postion and shape
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, 200,75))

class Player:
    def __init__(self, x, y):#Defines postion variables, score, and movement
        self.x = x
        self.y = y
        self.yvel = 10
        self.moving_up = False
        self.moving_down = False
        self.moving_up = False
        self.moving_down = False
        self.score = 0
    def update(self):#Draws the object on to the screen to update its postion and shape
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, 20,100))
        if self.moving_down == True:
            self.y += self.yvel
        if self.moving_up == True:
            self.y -= self.yvel

class Ball:
    def __init__(self, x, y):#Defines postion variables and velocity
        self.x = x
        self.y = y
        self.yvel = 7
        self.xvel = 7
    def update(self):#Draws the object on to the screen to update its postion and shape. It also allows it to bounce off the wall.
        #pygame.draw.rect(screen, (255,255,255), (self.x,self.y, 20,20))
        Ball = pygame.image.load('Images\sball.png').convert()
        Ball = pygame.transform.scale(Ball, (20,20))#Scales the image
        rect = Ball.get_rect()
        rect.center = (self.x+9,self.y+9)
        screen.blit(Ball, rect)
        self.x += self.xvel
        self.y += self.yvel/2
        if self.x >= WINDOW_SIZE[0] or self.x <= 0:
            self.xvel *= -1
        if self.y > WINDOW_SIZE[1] or self.y <= 0:
            self.yvel *= -1

def win_screen():
    """
    Shows when the player scores 10
    """
    if player.score >= 10:
        screen.fill((0,0,0))
        draw_text('You Win!',font, (255,255,255), screen, WINDOW_SIZE[0]/2.50,WINDOW_SIZE[1]/8)
        ball.yvel = 0
        ball.xvel = 0

def lose_screen():
    """
    Shows when the Computer scores 10
    """
    if comp.score >= 10:
        screen.fill((0,0,0))
        draw_text('You Lose!',font, (255,255,255), screen, WINDOW_SIZE[0]/2.50,WINDOW_SIZE[1]/8)
        ball.yvel = 0
        ball.xvel = 0

def win_screen2_1():
    """
    Shows when the player scores 10
    """
    if player.score >= 10:
        screen.fill((0,0,0))
        draw_text('Player 1 Wins!',font, (255,255,255), screen, WINDOW_SIZE[0]/2.50,WINDOW_SIZE[1]/8)
        ball.yvel = 0
        ball.xvel = 0

def win_screen2_2():
    """
    Shows when the second player scores 10
    """
    if player_2.score >= 10:
        screen.fill((0,0,0))
        draw_text('Player 2 Wins!',font, (255,255,255), screen, WINDOW_SIZE[0]/2.50,WINDOW_SIZE[1]/8)
        ball.yvel = 0
        ball.xvel = 0

"""
Used to set the class objects postions
"""
player = Player(100, 100)
comp = Player(900, 100)
ball = Ball(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2)
Start = Button(190,436)
s_player = Button(630,436)
player_2 = Player(900,100)
hard = Button(410,600)


def game_screen():
    """
    Main game loop
    """
    while True:
        screen.fill((0,0,0))
        draw_text('PONG', font, (255,255,255), screen, WINDOW_SIZE[0]/2.25,WINDOW_SIZE[1]/8)#
        draw_text(str(player.score) + " - " + str(comp.score), font, (255,255,255), screen, WINDOW_SIZE[0]/2.20,WINDOW_SIZE[1]/6)# Scoreboard
        player.update()
        comp.update()
        ball.update()



        # Computer following ball
        if comp.y < ball.y:
            comp.y += 9
        if comp.y > ball.y:
            comp.y -= 9

        # Scoring area and point system for the computer
        if ball.x <= 0:
            ball.x = WINDOW_SIZE[0]/2
            ball.y = WINDOW_SIZE[1]/2
            comp.score += 1
            Concede = pygame.mixer.Sound("Sounds/Concede.wav")
            Concede.play()
            ball.xvel = 0
            ball.xvel += -7
            ball.yvel = 0
            ball.yvel += -7

        # Sends to the lose screen if the player is scored on 10 times and plays a sound
        if comp.score >= 10:
            lose_screen()
            Lose = pygame.mixer.Sound("Sounds/Lose.wav")
            Lose.play()
            pygame.time.delay(30)
            pygame.mixer.pause()

        # Scoring area and point system for the player
        if ball.x >= WINDOW_SIZE[0]:
            ball.x = WINDOW_SIZE[0]/2
            ball.y = WINDOW_SIZE[1]/2
            player.score += 1
            Goal = pygame.mixer.Sound("Sounds/Goal.wav")
            Goal.play()
            ball.xvel = 0
            ball.xvel += 7
            ball.yvel = 0
            ball.yvel += 7

        # Sends to the win screen if player score is 10 and plays a sound
        if player.score >= 10:
            win_screen()
            Win = pygame.mixer.Sound("Sounds/Win.wav")
            Win.play()
            pygame.time.delay(120)
            pygame.mixer.pause()

        # Player collision
        if ball.x <= player.x + 20 and ball.x >= player.x and ball.y >= player.y and ball.y <= player.y + 100:
            ball.xvel *= -1
            Hit = pygame.mixer.Sound("Sounds/Hit.wav")
            Hit.play()
            if player.moving_down == True:
                ball.yvel = abs(ball.yvel) * 1.5
            elif player.moving_up == True:
                ball.yvel = abs(ball.yvel)* - 1.5
            else:
                ball.yvel *= 0.6

        # Makes so that the player can't go off the screen
        if player.y >= WINDOW_SIZE[1] - 110:
            player.y = WINDOW_SIZE[1] - 110
        if player.y <= 10:
            player.y = 10

        # Bot collision
        if ball.x >= comp.x - 10 and ball.x <= comp.x + 10 and ball.y >= comp.y -10 and ball.y <= comp.y + 100:
            ball.xvel *= -1
            ball.yvel = ball.yvel * 1.5
            Hit = pygame.mixer.Sound("Sounds/Hit.wav")
            Hit.play()

        # Makes so that the computer can't go off the screen
        if comp.y >= WINDOW_SIZE[1] - 100:
            comp.y = WINDOW_SIZE[1] - 100
        if comp.y <= 10:
            comp.y = 10

        # Avoids yvel going under 1
        if ball.yvel < 0 and abs(ball.yvel) < 1:
            ball.yvel = -1
        if ball.yvel < 1 and ball.yvel > 0:
            ball.yvel = 1

        # Avoids yvel going over 15
        if ball.yvel < 0 and abs(ball.yvel) > 20:
            ball.yvel = -20
        if ball.yvel > 20:
            ball.yvel = 20

        # Moves the player and finds wether or not they have the button down or not
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == ord('s'):
                    player.moving_down = True
                if event.key == ord('w'):
                    player.moving_up = True
            if event.type == KEYUP:
                if event.key == ord('s'):
                    player.moving_down = False
                if event.key == ord('w'):
                    player.moving_up = False

            if event.type == QUIT:#Allows the exit button to exit out of the program
                pygame.quit()
                sys.exit()

        pygame.display.update()#Updates display
        clock.tick(60)#Sets frame rate to 60 FPS

def game_screen_2():
    """
    2 player game loop
    """
    while True:
        screen.fill((0,0,0))
        draw_text('PONG', font, (255,255,255), screen, WINDOW_SIZE[0]/2.25,WINDOW_SIZE[1]/8)
        draw_text(str(player.score) + " - " + str(player_2.score), font, (255,255,255), screen, WINDOW_SIZE[0]/2.20,WINDOW_SIZE[1]/6)
        player.update()
        ball.update()
        player_2.update()

        # Scoring area and point system for player 2
        if ball.x <= 0:
            ball.x = WINDOW_SIZE[0]/2
            ball.y = WINDOW_SIZE[1]/2
            player_2.score += 1
            Goal = pygame.mixer.Sound("Sounds/Goal.wav")
            Goal.play()
            ball.xvel = 0
            ball.xvel += -7
            ball.yvel = 0
            ball.yvel += -7

        # Scoring area and point system for player 1
        if ball.x >= WINDOW_SIZE[0]:
            ball.x = WINDOW_SIZE[0]/2
            ball.y = WINDOW_SIZE[1]/2
            player.score += 1
            Goal = pygame.mixer.Sound("Sounds/Goal.wav")
            Goal.play()
            ball.xvel = 0
            ball.xvel += 7
            ball.yvel = 0
            ball.yvel += 7

        # Sends to the win screen if player 1 score is 10 and plays a sound
        if player.score >= 10:
            win_screen2_1()
            Win = pygame.mixer.Sound("Sounds/Win.wav")
            Win.play()
            pygame.time.delay(120)
            pygame.mixer.pause()

        # Sends to the win screen if player 2 score is 10 and plays a sound
        if player_2.score >= 10:
            win_screen2_2()
            Win = pygame.mixer.Sound("Sounds/Win.wav")
            Win.play()
            pygame.time.delay(120)
            pygame.mixer.pause()

        # Player collision
        if ball.x <= player.x + 20 and ball.x >= player.x and ball.y >= player.y and ball.y <= player.y + 100:
            ball.xvel *= -1
            Hit = pygame.mixer.Sound("Sounds/Hit.wav")
            Hit.play()
            if player.moving_down == True:
                ball.yvel = abs(ball.yvel) * 1.5
            elif player.moving_up == True:
                ball.yvel = abs(ball.yvel)* - 1.5
            else:
                ball.yvel *= 0.6

        # Makes so that the player 1 can't go off the screen
        if player.y >= WINDOW_SIZE[1] - 110:
            player.y = WINDOW_SIZE[1] - 110
        if player.y <= 10:
            player.y = 10

        # Player collision
        if ball.x <= player_2.x + 20 and ball.x >= player_2.x and ball.y >= player_2.y and ball.y <= player_2.y + 100:
            ball.xvel *= -1
            Hit = pygame.mixer.Sound("Sounds/Hit.wav")
            Hit.play()
            if player_2.moving_down == True:
                ball.yvel = abs(ball.yvel) * 1.5
            elif player_2.moving_up == True:
                ball.yvel = abs(ball.yvel)* - 1.5
            else:
                ball.yvel *= 0.6

        # Makes so that the player 2 can't go off the screen
        if player_2.y >= WINDOW_SIZE[1] - 110:
            player_2.y = WINDOW_SIZE[1] - 110
        if player_2.y <= 10:
            player_2.y = 10

        # Avoids yvel going under 1
        if ball.yvel < 0 and abs(ball.yvel) < 1:
            ball.yvel = -1
        if ball.yvel < 1 and ball.yvel > 0:
            ball.yvel = 1

        # Avoids yvel going over 15
        if ball.yvel < 0 and abs(ball.yvel) > 20:
            ball.yvel = -20
        if ball.yvel > 20:
            ball.yvel = 20

        # Moves the player and finds wether or not they have the button down or not
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    player_2.moving_down = True
                if event.key == K_UP:
                    player_2.moving_up = True
            if event.type == KEYUP:
                if event.key == K_DOWN:
                    player_2.moving_down = False
                if event.key == K_UP:
                    player_2.moving_up = False

            # Moves the player and finds wether or not they have the button down or not
            if event.type == KEYDOWN:
                if event.key == ord('s'):
                    player.moving_down = True
                if event.key == ord('w'):
                    player.moving_up = True
            if event.type == KEYUP:
                if event.key == ord('s'):
                    player.moving_down = False
                if event.key == ord('w'):
                    player.moving_up = False

            if event.type == QUIT:#Allows the exit button to exit out of the program
                pygame.quit()
                sys.exit()

        pygame.display.update()#Updates display
        clock.tick(60)#Sets frame rate to 60 FPS

def game_screen_3():
    """
    Main game loop
    """
    while True:
        screen.fill((0,0,0))
        draw_text('PONG', font, (255,255,255), screen, WINDOW_SIZE[0]/2.25,WINDOW_SIZE[1]/8)#
        draw_text(str(player.score) + " - " + str(comp.score), font, (255,255,255), screen, WINDOW_SIZE[0]/2.20,WINDOW_SIZE[1]/6)# Scoreboard
        player.update()
        comp.update()
        ball.update()

        # Computer following ball
        if comp.y < ball.y:
            comp.y += 14
        if comp.y > ball.y:
            comp.y -= 14

        # Scoring area and point system for the computer
        if ball.x <= 0:
            ball.x = WINDOW_SIZE[0]/2
            ball.y = WINDOW_SIZE[1]/2
            comp.score += 1
            Concede = pygame.mixer.Sound("Sounds/Concede.wav")
            Concede.play()
            ball.xvel = 0
            ball.xvel += 9
            ball.yvel = 0
            ball.yvel += 9

        # Sends to the lose screen if the player is scored on 10 times and plays a sound
        if comp.score >= 10:
            lose_screen()
            Lose = pygame.mixer.Sound("Sounds/Lose.wav")
            Lose.play()
            pygame.time.delay(30)
            pygame.mixer.pause()

        # Scoring area and point system for the player
        if ball.x >= WINDOW_SIZE[0]:
            ball.x = WINDOW_SIZE[0]/2
            ball.y = WINDOW_SIZE[1]/2
            player.score += 1
            Goal = pygame.mixer.Sound("Sounds/Goal.wav")
            Goal.play()
            ball.xvel = 0
            ball.xvel += 9
            ball.yvel = 0
            ball.yvel += 9

        # Sends to the win screen if player score is 10 and plays a sound
        if player.score >= 10:
            win_screen()
            Win = pygame.mixer.Sound("Sounds/Win.wav")
            Win.play()
            pygame.time.delay(120)
            pygame.mixer.pause()

        # Player collision
        if ball.x <= player.x + 20 and ball.x >= player.x and ball.y >= player.y and ball.y <= player.y + 100:
            ball.xvel *= -1
            Hit = pygame.mixer.Sound("Sounds/Hit.wav")
            Hit.play()
            if player.moving_down == True:
                ball.yvel = abs(ball.yvel) * 1.3
                ball.xvel = abs(ball.xvel) * 1.4
            elif player.moving_up == True:
                ball.yvel = abs(ball.yvel)* - 1.3
            else:
                ball.yvel *= 1
                ball.xvel *= 1.1

        # Makes so that the player can't go off the screen
        if player.y >= WINDOW_SIZE[1] - 110:
            player.y = WINDOW_SIZE[1] - 110
        if player.y <= 10:
            player.y = 10

        # Bot collision
        if ball.x >= comp.x - 10 and ball.x <= comp.x + 10 and ball.y >= comp.y -10 and ball.y <= comp.y + 100:
            ball.xvel *= -1
            ball.yvel = ball.yvel * 1.5
            ball.xvel = ball.xvel * 1.1
            Hit = pygame.mixer.Sound("Sounds/Hit.wav")
            Hit.play()

        # Makes so that the computer can't go off the screen
        if comp.y >= WINDOW_SIZE[1] - 100:
            comp.y = WINDOW_SIZE[1] - 100
        if comp.y <= 10:
            comp.y = 10

        # Avoids yvel going under 1
        if ball.yvel < 0 and abs(ball.yvel) < 1:
            ball.yvel = -1
        if ball.yvel < 1 and ball.yvel > 0:
            ball.yvel = 1

        # Avoids yvel going over 15
        if ball.yvel < 0 and abs(ball.yvel) > 30:
            ball.yvel = -30
        if ball.yvel > 30:
            ball.yvel = 30

        # Moves the player and finds wether or not they have the button down or not
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == ord('s'):
                    player.moving_down = True
                if event.key == ord('w'):
                    player.moving_up = True
            if event.type == KEYUP:
                if event.key == ord('s'):
                    player.moving_down = False
                if event.key == ord('w'):
                    player.moving_up = False

            if event.type == QUIT:#Allows the exit button to exit out of the program
                pygame.quit()
                sys.exit()

        pygame.display.update()#Updates display
        clock.tick(60)#Sets frame rate to 60 FPS

def main_Menu():
    """
    Main menu loop
    """
    while True:
        screen.fill((0,0,0))#Makes the screen black to update the page properly and so images dont stack
        picture = pygame.image.load('Images\Title.png')#Loads the title screen image
        picture = pygame.transform.scale(picture, (1024,768))#Scales the image
        rect = picture.get_rect()
        rect = rect.move((0,0))
        screen.blit(picture, rect)
        Start.update()#Updates the start button on to the page
        s_player.update()#Updates the second player button on to the page
        hard.update()
        draw_text('Start', font, (20,20,20), screen, 250,460)#Text for the first button
        draw_text('2 Players', font, (0,0,0), screen, 670,460)#Text for the second button
        draw_text('HARD MODE', font, (0,0,0), screen, 425,625)#Text for the third button
        x = 0
        y = 0

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:#Defines the area that you need to press the left mouse button in to start the game
                x , y = event.pos
                if event.button == 1 and x >= 189 and x <= 388 and y >= 435 and y <= 511:
                    game_screen()

            if event.type == MOUSEBUTTONDOWN:#Defines the area that you need to press the left mouse button in to activate Two palyer mode
                x , y = event.pos
                if event.button == 1 and x >= 629 and x <= 829 and y >= 435 and y <= 511:
                    game_screen_2()

            if event.type == MOUSEBUTTONDOWN:#Defines the area that you need to press the left mouse button in to activate Two palyer mode
                x , y = event.pos
                print(x,y)
                if event.button == 1 and x >= 410 and x <= 607 and y >= 599 and y <= 673:
                    game_screen_3()

            if event.type == QUIT: #Allows the exit button to exit out of the program
                pygame.quit()
                sys.exit()

        pygame.display.update()#Updates display
        clock.tick(60)#Sets frame rate to 60 FPS
main_Menu()
