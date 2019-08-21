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
import level_two2

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
    clock = pygame.time.Clock()
    jumps = 0

    player = Cat()
    bedroom = pygame.image.load("pics/lvl-bgs/full_bedroom2.png").convert()
    bed = Wall((50, 400))

    bedroom_sleeping = pygame.image.load("pics/lvl-bgs/full_bedroom_sleeping.png").convert()
    bedroom_sleeping = pygame.transform.scale(bedroom_sleeping, (width,height))

    while truevar:
        rectangle = pygame.draw.rect(screen, (0,0,0), bed)

        # if kai is sleeping
        if DoorOpen == False:
            screen.blit(bedroom_sleeping, (0,0))

        # if kai is woken up
        if DoorOpen == True:
            screen.blit(bedroom, (0,0))

        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
        if key[pygame.K_RIGHT]:
            player.move(2)
        if key[pygame.K_UP]:
            player.jump()

        # cat leaves bedroom to go to kitchen
        # TO DO: make the bed wall not work in the kitchen
        if key[pygame.K_RETURN]:
            if player.rect.x >900 and player.rect.x <1100:
                truevar = False
                level_two2.leveltwo() #change to level_two later when those files have been combined

        print (player.jumpdone)
        if player.jumpdone == 10:
            DoorOpen = True
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
        #speech bubble text
        speechText = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)

        TextSurf4, TextRect4 = text_objects("Jump on Kai to wake them up!", speechText)
        TextRect4.center = (900,80)
        screen.blit(TextSurf4,TextRect4)

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

#take this out later
levelone()
