#kitchen

import pygame
from pygame.locals import *
import transitions
from transitions import *
import random

from movement import *

import level_three

# import start_menu

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def leveltwooutside ():

    # flags = FULLSCREEN | DOUBLEBUF
    pygame.init() #take out later

    #define colors
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    lightBlue = (180,180,225)
    darkBlue = (141,138,186)
    darkerBlue = (114,111,161)

    #defining screen
    width, height = 1200,600
    screen = pygame.display.set_mode((width, height))
    transitions.init ( screen, width, height )
    hideSpeech = True

    truevar = True
    clock = pygame.time.Clock()
    click = pygame.mouse.get_pressed()

    player = Cat()

    bus_stop = pygame.image.load("pics/lvl-bgs/full_busstop.png").convert()
    bus_stop = pygame.transform.scale(bus_stop, (width,height))

    player.rect.x = 1100

    while truevar:
        #draw bg
        screen.blit(bus_stop, (0,0))

        screen.blit(player.image, player.rect)
        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
        if key[pygame.K_RIGHT]:
            player.move(2)
        if key[pygame.K_UP]:
            player.jump()

        mouse = pygame.mouse.get_pos()
        print(mouse)
        if key[pygame.K_RETURN]:
            if player.rect.x > 130 and player.rect.x < 250:
                truevar = False
                level_three.levelthree()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit(0)
                elif event.key == K_KP_ENTER:
                    pygame.quit()
                    exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_img = event.pos

leveltwooutside()
