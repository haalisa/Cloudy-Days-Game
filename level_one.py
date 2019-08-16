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

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# def game_intro():
#
#     flags = FULLSCREEN | DOUBLEBUF
#
#     #define colors
#     black = (0,0,0)
#     white = (255,255,255)
#     red = (255,0,0)
#     lightBlue = (180,180,225)
#     darkBlue = (141,138,186)
#     darkerBlue = (114,111,161)
#
#     #defining screen
#     width, height = 1200,600
#     screen = pygame.display.set_mode((width, height),flags)
#     # transitions.init ( screen, width, height )
#
#     clock = pygame.time.Clock()
#     cloud1_xPos = 200
#     cloud1_yPos = random.randint(300,400)
#     cloud2_xPos = -100
#     cloud2_yPos = random.randint(50,150)
#     cloud3_xPos = 100
#     cloud3_yPos = random.randint(400,550)
#     clock.tick(180)
#     while True:
#         #background is blue
#         screen.fill(lightBlue)
#
#         #cloud animation
#         cloud1 = pygame.image.load("pics/cloud1.png")
#         cloud1 = pygame.transform.scale(cloud1,(400,250))
#         cloud2 = pygame.image.load("pics/cloud2.png")
#         cloud2 = pygame.transform.scale(cloud2,(200,100))
#         cloud3 = pygame.image.load("pics/cloud2.png")
#         cloud3 = pygame.transform.scale(cloud2,(75,50))
#         screen.blit(cloud1, (cloud1_xPos,cloud1_yPos))
#         for i in range(200):
#             cloud1_xPos = cloud1_xPos + 0.01
#         screen.blit(cloud2, (cloud2_xPos,cloud2_yPos))
#         for i in range(200):
#             cloud2_xPos = cloud2_xPos + 0.015
#         screen.blit(cloud3,(cloud2_xPos,cloud3_yPos))
#
#         #buttons
#         mouse = pygame.mouse.get_pos()
#         buttonPos = ((width/2)-50,450,100,50)
#         startButton = pygame.draw.rect(screen, darkBlue, buttonPos)
#
#         if startButton.collidepoint(mouse):
#             startButton = pygame.draw.rect(screen, darkerBlue,buttonPos)
#         else:
#             startButton = pygame.draw.rect(screen, darkBlue,buttonPos)
#
#         #if button is clicked
#         click = pygame.mouse.get_pressed()
#         if click[0] == 1 and startButton.collidepoint(mouse):
#             levelone()
#
#
#         #define texts
#         largeText = pygame.font.Font('fonts/Roboto-Thin.ttf', 100)
#         TextSurf, TextRect = text_objects("Cloudy Days", largeText)
#         TextRect.center = ((width/2),(height/2)-100)
#
#         descriptionText = pygame.font.Font('fonts/Roboto-Thin.ttf', 30)
#         TextSurf1, TextRect1 = text_objects("a game about mental health", descriptionText)
#         TextRect1.center = ((width/2),(height/2))
#
#         buttonText = pygame.font.Font('fonts/Roboto-Thin.ttf', 35)
#         TextSurf2, TextRect2 = text_objects("start", buttonText)
#         TextRect2.center = ((width/2),470)
#
#         #draw texts
#         screen.blit(TextSurf, TextRect)
#         screen.blit(TextSurf1, TextRect1)
#         screen.blit(TextSurf2, TextRect2)
#
#         pygame.display.flip()
#
#         clock.tick(60)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit(0)
#             elif event.type == KEYDOWN:
#                if event.key == K_ESCAPE:
#                    pygame.quit()
#                    exit(0)
#

def levelone ():

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
    while truevar:
        bg = pygame.image.load("pics/lvl-bgs/bedroom.png").convert()
        bg = pygame.transform.scale(bg, (width,height))
        screen.blit(bg, (0,0))

        #player
        krabsPos = [0,100] #player position
        krabs = pygame.image.load("pics/krabs.png")
        # krabs = pygame.Surface.get_rect
        # krabs.transform.scale(250,350)
        screen.blit(krabs, krabsPos) #draw screen elements

        #speech bubble
        speechBubble = pygame.draw.ellipse(screen, darkBlue, (width/2-300,height/2-200,300,200)) #position,size
        transitions.run ("fadeOutUp")
        transitions.updateScreen()
        #the go back button
        mouse = pygame.mouse.get_pos()
        button2Pos = (1000,100,100,50)
        goBackButton = pygame.draw.rect(screen, red, button2Pos)

        if goBackButton.collidepoint(mouse):
            goBackButton = pygame.draw.rect(screen, red,button2Pos)
        else:
            startButton = pygame.draw.rect(screen, white,button2Pos)

        #if button is clicked
        click = pygame.mouse.get_pressed()


        if runSecondTime == True:
            if click[0] == 1 and goBackButton.collidepoint(mouse):

                start_menu.game_intro()
                truevar = False

        #defining texts
        #button text
        buttonText = pygame.font.Font('fonts/Roboto-Thin.ttf', 25)
        TextSurf3, TextRect3 = text_objects("go back", buttonText)
        TextRect3.center = (1050,125)

        #speech bubble text
        speechText = pygame.font.Font('fonts/Roboto-Thin.ttf', 20)
        TextSurf4, TextRect4 = text_objects("Hello world!", speechText)
        TextRect4.center = (400,200)

        screen.blit(TextSurf3,TextRect3)
        screen.blit(TextSurf4,TextRect4)

        pygame.display.flip()

        clock.tick(60)

        runSecondTime = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   exit(0)
