# Things to do here:
# Have Kai lay on the bed
# Collision detection on edges
# Make furniture interactive (i.e. clicking on the cat door will send Kit Kat to closet)
import pygame
from pygame.locals import *

import random
# import level_two

# import start_menu
from movement import Cat
from movement import Wall
from itertools import chain

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    white = (255,255,255)
    textSurface = font.render(text, True, white)
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

    truevar = True
    DoorOpen = False
    KaiUp= False
    clock = pygame.time.Clock()
    jumps = 0
    enter = 0
    pickedUp = False

    player = Cat()
    bedroom = pygame.image.load("pics/lvl-bgs/full_bedroom2.png").convert()
    bed = Wall((50, 420))

    bedroom_w_kai = pygame.image.load("pics/lvl-bgs/full_bedroom_kai.png").convert()
    bedroom_w_kai = pygame.transform.scale(bedroom_w_kai, (width,height))

    bed_empty = pygame.image.load("pics/lvl-bgs/full_bedroom_empty.png").convert()
    bed_empty = pygame.transform.scale(bed_empty, (width,height))

    bp= pygame.image.load("pics/backpackgif.gif").convert()

    # text boxes
    speechText = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)

    introtext= pygame.image.load("text/intro.png").convert()
    wakeup= pygame.image.load("text/wakeup.png").convert()
    fivemin= pygame.image.load("text/5min.png").convert()
    gettingup= pygame.image.load("text/gettingup.png").convert()
    readyy= pygame.image.load("text/readyy.png").convert()
    pawsitive= pygame.image.load("text/pawsitive!.png").convert()
    noenergy =pygame.image.load("text/kai speaking.png").convert()

    TextSurf4, TextRect4 = text_objects("Press enter to continue", speechText)
    TextRect4.center = (900,80)
    TextSurf3, TextRect3 = text_objects("Pick up Kai's bag using the space bar", speechText)
    TextRect3.center = (900,80)
    TextSurf1, TextRect1 = text_objects("Use left, right, and up arrows to jump on Kai's bed", speechText)
    TextRect1.center = (900,80)
    TextSurf5, TextRect5 = text_objects("Exit the room using the enter key", speechText)
    TextRect5.center = (900,80)

    dialogue = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)

    TextSurf_n1, TextRect_n1 = text_objects2("Press enter to continue", dialogue)
    TextRect_n1.center = (275,80)

    text_box = pygame.image.load("pics/teal_rect.png")
    text_box.set_alpha(200)
    text_box = pygame.transform.scale(text_box, (width,150))

    kaicon = pygame.image.load("KAI/uh2.png")
    kaicon = pygame.transform.scale(kaicon, (100,130))

    next = 0

    while truevar:

        rectangle = pygame.draw.rect(screen, (0,0,0), bed)

        # if kai is sleeping
        if DoorOpen == False:
            screen.blit(bedroom_w_kai, (0,0))
        # if kai is woken up
        if DoorOpen == True:
            screen.blit(bed_empty, (0,0))
        if not pickedUp:
            screen.blit(bp, (900,400))
        else:
            screen.blit(bp, (player.rect.x+110,player.rect.y+90))

        if enter == 0 or jumps>= 10 and jumps <15:
            screen.blit(TextSurf4,TextRect4)
        if enter ==0:
            screen.blit(introtext,(250,100))

        if enter == 1 and jumps<10:
            screen.blit(TextSurf1,TextRect1)
        # elif enter == 2:
        if jumps >=1 and jumps <5:
            screen.blit(wakeup, (250,100))
        if jumps >= 5 and jumps <10:
            screen.blit(fivemin, (250,100))
        if jumps >= 10 and jumps< 15:
            screen.blit(gettingup, (250,100))
            DoorOpen=True
            KaiUp= True

        if KaiUp:
            if enter == 2:
                jumps = 15
                screen.blit(readyy, (0,0))
                player.rect.x= -200
            elif enter == 3:
                screen.blit(noenergy, (0,0))
            elif enter == 4:
                screen.blit(pawsitive, (0,0))
            elif enter == 5:
                player.rect.x= 400
                enter =6
            elif enter == 6:
                screen.blit(TextSurf3,TextRect3)
            elif enter >= 7:
                screen.blit(TextSurf5,TextRect5)


        if player.rect.x >800 and player.rect.x< 900:
            pickedUp= True

        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
            player.image = pygame.image.load("KIT_KAT/kitkat_left2.png")
        if key[pygame.K_RIGHT]:
            player.move(2)
            player.image = pygame.image.load("KIT_KAT/kitkat_right2.png")
        if enter >= 1:
            if key[pygame.K_UP]:
                player.jump()


        # cat leaves bedroom to go to kitchen
        # TO DO: make the bed wall not work in the kitchen
        if key[pygame.K_RETURN]:
            if player.rect.x >900 and player.rect.x <1100:
                truevar = False
                level_two.leveltwo() #change to level_two later when those files have been combined

        if player.rect.x > 50 and player.rect.x<300 and player.v == 0.25:
            jumps +=1


        screen.blit(player.image, player.rect)

        clock.tick(150)

        screen.blit(text_box,(0,0))
        screen.blit(kaicon, (25,15))

        if next == 0:
            screen.blit(TextSurf_n1,TextRect_n1)

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
