#kitchen

import pygame
from pygame.locals import *
import random

from movement import *
#
import level_three

# import start_menu

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    white = (255,255,255)
    textSurface = font.render(text, True, white)
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
    hideSpeech = True

    truevar = True
    clock = pygame.time.Clock()
    click = pygame.mouse.get_pressed()

    player = Cat()

    bus_stop = pygame.image.load("pics/lvl-bgs/full_busstop.png").convert()
    bus_stop = pygame.transform.scale(bus_stop, (width,height))

    dialogue = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)

    TextSurf_n, TextRect_n = text_objects2("We need to get Kai to school!", dialogue)
    TextRect_n.center = (375,80)

    TextSurf_n1, TextRect_n1 = text_objects("Press enter to interact with objects.", dialogue)
    TextRect_n1.center = (900,560)

    next = 0

    text_box = pygame.image.load("pics/teal_rect.png")
    text_box.set_alpha(150)
    text_box = pygame.transform.scale(text_box, (width,150))

    player.rect.x = 1100

    while truevar:
        #draw bg
        screen.blit(bus_stop, (0,0))

        screen.blit(player.image, player.rect)

        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
            player.image = pygame.image.load("KIT_KAT/kitkat_left2.png")
        if key[pygame.K_RIGHT]:
            player.move(2)
            player.image = pygame.image.load("KIT_KAT/kitkat_right2.png")
        if key[pygame.K_UP]:
            player.jump()

        screen.blit(text_box,(0,0))
        if next == 0:
            screen.blit(TextSurf_n,TextRect_n)
            screen.blit(TextSurf_n1,TextRect_n1)

        # mouse = pygame.mouse.get_pos()
        # print(mouse)
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
