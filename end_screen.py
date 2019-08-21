# add a composition book screen

import pygame
from pygame.locals import *
import transitions
from transitions import *
import random

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def endscreen():

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
    # transitions.init ( screen, width, height )

    clock = pygame.time.Clock()
    cloud1_xPos = 200
    cloud1_yPos = random.randint(300,400)
    cloud2_xPos = -100
    cloud2_yPos = random.randint(50,150)
    cloud3_xPos = 100
    cloud3_yPos = random.randint(400,500)
    clock.tick(180)

    while True:
        #background is blue
        screen.fill(lightBlue)

        #cloud animation
        cloud1 = pygame.image.load("pics/cloud1.png")
        # cloud1 = load_image()
        # pixels = PixelArray(cloud1)
        # pixels.replace(Color(black, Color(red))
        cloud1 = pygame.transform.scale(cloud1,(400,250))
        cloud2 = pygame.image.load("pics/cloud2.png")
        cloud2 = pygame.transform.scale(cloud2,(200,100))
        cloud3 = pygame.image.load("pics/cloud2.png")
        cloud3 = pygame.transform.scale(cloud2,(75,50))
        screen.blit(cloud1, (cloud1_xPos,cloud1_yPos))
        i = 0
        for i in range(200):
            cloud1_xPos = cloud1_xPos + 0.01
        screen.blit(cloud2, (cloud2_xPos,cloud2_yPos))
        screen.blit(cloud3,(cloud2_xPos,cloud3_yPos))
        for i in range(200):
            cloud2_xPos = cloud2_xPos + 0.015
        if cloud1_xPos > 1250:
            i = 0
            cloud1_xPos = random.randint(-50,-100)
        if cloud2_xPos > 1250:
            i = 0
            cloud1_xPos = random.randint(-50,-100)
        if cloud2_xPos > 1250:
            i = 0
            cloud1_xPos = random.randint(-50,-100)

        #define texts
        largeText = pygame.font.Font('fonts/Roboto-Thin.ttf', 100)
        TextSurf, TextRect = text_objects("to be continued...", largeText)
        TextRect.center = ((width/2),(height/2)-100)

        descriptionText = pygame.font.Font('fonts/Roboto-Thin.ttf', 50)
        TextSurf1, TextRect1 = text_objects("thank you for playing!!!", descriptionText)
        TextRect1.center = ((width/2),(height/2))

        creator_names = pygame.font.Font('fonts/Roboto-Thin.ttf', 30)
        TextSurf2, TextRect2 = text_objects("~ Iris Li, Divaa Leathers, Lisa Ha", creator_names)
        TextRect2.center = ((width/2),(height/2)+100)

        #draw texts
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf1, TextRect1)
        screen.blit(TextSurf2, TextRect2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   exit(0)
