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

    lockers = pygame.image.load("pics/lvl-bgs/full_lockers.png").convert()
    school_door = pygame.image.load("pics/lvl-bgs/kitchen_door.png")
    block_rect = pygame.Rect(950, 200, 200, 335)
    player= Cat()
    while truevar:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        screen.blit(lockers, (0,0))
        # block = pygame.draw.rect(screen, (0,0,0), block_rect)

        screen.blit(player.image, player.rect)
        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
        if key[pygame.K_RIGHT]:
            player.move(2)
        if key[pygame.K_UP]:
            player.jump()

        if key[pygame.K_RETURN]:
            if player.rect.x >900 and player.rect.x <1100:
                truevar = False
                maze.main()

        clock.tick(200)
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
