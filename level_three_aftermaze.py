#lockers

import pygame
from pygame.locals import *
import random
import maze
from movement import Cat
from movement import Wall
# import level_two
import end_screen

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    white = (255,255,255)
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def levelthreeaftermaze ():

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
    hideSpeech = True

    truevar = True
    clock = pygame.time.Clock()

    lockers = pygame.image.load("pics/lvl-bgs/full_lockers.png").convert()
    school_door = pygame.image.load("pics/lvl-bgs/kitchen_door.png")
    block_rect = pygame.Rect(950, 200, 200, 335)
    player= Cat()
    player.rect.x = 975

    dialogue = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)

    TextSurf_n, TextRect_n = text_objects2("We finished the school day!", dialogue)
    TextRect_n.center = (375,80)

    TextSurf_n1, TextRect_n1 = text_objects("Walk left to leave the school.", dialogue)
    TextRect_n1.center = (900,560)

    next = 0

    text_box = pygame.image.load("pics/teal_rect.png")
    text_box.set_alpha(200)
    text_box = pygame.transform.scale(text_box, (width,150))


    while truevar:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        screen.blit(lockers, (0,0))
        # block = pygame.draw.rect(screen, (0,0,0), block_rect)

        screen.blit(player.image, player.rect)
        player.update()

        screen.blit(text_box,(0,0))
        if next == 0:
            screen.blit(TextSurf_n,TextRect_n)
            screen.blit(TextSurf_n1,TextRect_n1)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
            player.image = pygame.image.load("KIT_KAT/kitkat_left2.png")
        if key[pygame.K_RIGHT]:
            player.move(2)
            player.image = pygame.image.load("KIT_KAT/kitkat_right2.png")
        if key[pygame.K_UP]:
            player.jump()

        if player.rect.x < -150:
            end_screen.endscreen()

        # if key[pygame.K_RETURN]:
        #     if player.rect.x >900 and player.rect.x <1100:
        #         truevar = False
        #         maze.main()

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


#levelthreeaftermaze()
