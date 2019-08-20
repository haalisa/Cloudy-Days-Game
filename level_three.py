#lockers

import pygame
from pygame.locals import *
import transitions
from transitions import *
import random
import maze
from movement import Cat
from movement import Wall
# import level_two

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def levelthree ():

    flags = FULLSCREEN | DOUBLEBUF

    pygame.init()
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
    hideSpeech = True

    truevar = True
    clock = pygame.time.Clock()

    lockers = pygame.image.load("pics/lvl-bgs/lockers.png")

    school_door = pygame.image.load("pics/lvl-bgs/school_door.png")

    school_floor = pygame.image.load("pics/lvl-bgs/school_floor.png")
    screen.fill(white)
    player= Cat()
    while truevar:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(lockers, (0,0))

        screen.blit(school_door, (0,0))

        screen.blit(school_floor, (0,0))
        screen.blit(player.image, player.rect)

        player.update()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
        if key[pygame.K_RIGHT]:
            player.move(2)
        if key[pygame.K_UP]:
            player.jump()

        test_rect = school_door.get_rect()
        # if door is clicked then go to maze game
        if click[0] == 1 and test_rect.collidepoint(mouse):
            truevar = False
            maze.main()

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




levelthree()
