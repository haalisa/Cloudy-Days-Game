# Things to do here:
# Make scene function
# Have Kai lay on the bed
# Kit Kat is movable by wasd or arrow keys and can jump
# Collision detection works
# Interacting with the door will exit to the kitchen
# Make furniture interactive (i.e. clicking on the cat door will send Kit Kat to closet)

import pygame
from pygame.locals import *
import transitions
from transitions import *
import random

import start_menu
from movement import Player
from movement import Cat

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def levelone ():

    pygame.init() #take this out later

    flags = FULLSCREEN | DOUBLEBUF

    #define colors
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    lightBlue = (180,180,225)
    darkBlue = (141,138,186)
    darkerBlue = (114,111,161)

    #defining screen
    width, height = 1200,600
    screen = pygame.display.set_mode((width, height),flags)
    transitions.init ( screen, width, height )

    truevar = True
    runSecondTime = False
    clock = pygame.time.Clock()

    player = Cat()

    while truevar:
        bedroom = pygame.image.load("pics/lvl-bgs/bedroom.png").convert()
        bedroom = pygame.transform.scale(bedroom, (width,height))
        screen.blit(bedroom, (0,0))

        bed = pygame.image.load("pics/lvl-bgs/bed.png")
        bed = pygame.transform.scale(bed, (width,height))
        screen.blit(bed, (0,0))

        bedroom_door = pygame.image.load("pics/lvl-bgs/bedroom_door.png")
        bedroom_door = pygame.transform.scale(bedroom_door, (width,height))
        screen.blit(bedroom_door, (0,0))

        catdoor = pygame.image.load("pics/lvl-bgs/catdoor.png")
        catdoor = pygame.transform.scale(catdoor, (width,height))
        screen.blit(catdoor, (0,0))

        dresser = pygame.image.load("pics/lvl-bgs/dresser.png")
        dresser = pygame.transform.scale(dresser, (width,height))
        screen.blit(dresser, (0,0))

        # #player
        # krabsPos = [0,100] #player position
        # krabs = pygame.image.load("pics/krabs.png")
        # # krabs = pygame.Surface.get_rect
        # # krabs.transform.scale(250,350)
        # screen.blit(krabs, krabsPos) #draw screen elements

        # #speech bubble
        # speechBubble = pygame.draw.ellipse(screen, darkBlue, (width/2-300,height/2-200,300,200)) #position,size
        # transitions.run ("fadeOutUp")
        # transitions.updateScreen()
        # #the go back button
        # mouse = pygame.mouse.get_pos()
        # button2Pos = (1000,100,100,50)
        # goBackButton = pygame.draw.rect(screen, red, button2Pos)
        #
        # if goBackButton.collidepoint(mouse):
        #     goBackButton = pygame.draw.rect(screen, red,button2Pos)
        # else:
        #     startButton = pygame.draw.rect(screen, white,button2Pos)

        #if button is clicked
        click = pygame.mouse.get_pressed()

        #
        # if runSecondTime == True:
        #     if click[0] == 1 and goBackButton.collidepoint(mouse):
        #
        #         start_menu.game_intro()
        #         truevar = False

        #defining texts
        #button text
        # buttonText = pygame.font.Font('fonts/Roboto-Thin.ttf', 25)
        # TextSurf3, TextRect3 = text_objects("go back", buttonText)
        # TextRect3.center = (1050,125)
        #
        # #speech bubble text
        # speechText = pygame.font.Font('fonts/Roboto-Thin.ttf', 20)
        # TextSurf4, TextRect4 = text_objects("Hello world!", speechText)
        # TextRect4.center = (400,200)
        #
        # screen.blit(TextSurf3,TextRect3)
        # screen.blit(TextSurf4,TextRect4)

        pygame.display.flip()

        clock.tick(60)

        runSecondTime = True

        # screen.blit(player.image, player.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   exit(0)

#take this out later
levelone()
