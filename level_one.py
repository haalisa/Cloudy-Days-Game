# Things to do here:
# Have Kai lay on the bed
# Collision detection on edges
# Interacting with the door will exit to the kitchen
# Make furniture interactive (i.e. clicking on the cat door will send Kit Kat to closet)
import pygame
from pygame.locals import *
import transitions
from transitions import *
import random
# import level_two2

# import start_menu
from movement import Cat
from movement import Wall
from itertools import chain

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
    DoorOpen = False
    KaiUp= False
    clock = pygame.time.Clock()
    jumps = 0
    enter = 0

    player = Cat()
    bedroom = pygame.image.load("pics/lvl-bgs/full_bedroom2.png").convert()
    bed = Wall((50, 400))

    bedroom_sleeping = pygame.image.load("pics/lvl-bgs/full_bedroom_sleeping.png").convert()
    bedroom_sleeping = pygame.transform.scale(bedroom_sleeping, (width,height))

    introtext= pygame.image.load("pics/bird1.png").convert()
    instruct= pygame.image.load("pics/bird2.png").convert()
TextSurf4, TextRect4 = text_objects("Press enter to continue", speechText)
TextRect4.center = (900,80)
screen.blit(TextSurf4,TextRect4)
TextSurf1, TextRect1 = text_objects("Hit the up arrow to jump on Kai's bed", speechText)
TextRect4.center = (900,80)
    while truevar:
        rectangle = pygame.draw.rect(screen, (0,0,0), bed)

        # if kai is sleeping
        if DoorOpen == False:
            screen.blit(bedroom_sleeping, (0,0))
        # if kai is woken up
        if DoorOpen == True:
            screen.blit(bedroom, (0,0))
        if enter == 0:
            screen.blit(introtext,(500,100))
        elif enter == 1:
            screen.blit(instruct, (500,100))
        elif enter == 2

        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
        if key[pygame.K_RIGHT]:
            player.move(2)
        if enter == 1:
            if key[pygame.K_UP]:
                player.jump()

        # cat leaves bedroom to go to kitchen
        # TO DO: make the bed wall not work in the kitchen
        if key[pygame.K_RETURN]:
            if player.rect.x >900 and player.rect.x <1100:
                truevar = False
                level_two2.leveltwo() #change to level_two later when those files have been combined

        if player.rect.x > 50 and player.rect.x<300 and player.v == 0.25:
            jumps +=1

        if jumps >= 10:
            DoorOpen = True

        if jumps >= 5:
            KaiUp= True

        speechText = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)


        screen.blit(TextSurf1,TextRect1)

        screen.blit(player.image, player.rect)

        clock.tick(150)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key==K_RETURN:
                    enter += 1
#take this out later
levelone()
