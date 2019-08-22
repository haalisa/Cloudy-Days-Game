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

    # flags = FULLSCREEN | DOUBLEBUF

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
    #
    # introtext= pygame.image.load("text/intro.png").convert()
    # wakeup= pygame.image.load("text/wakeup.png").convert()
    # fivemin= pygame.image.load("text/5min.png").convert()
    # gettingup= pygame.image.load("text/gettingup.png").convert()
    # readyy= pygame.image.load("text/readyy.png").convert()
    # pawsitive= pygame.image.load("text/pawsitive!.png").convert()
    # noenergy =pygame.image.load("text/kai speaking.png").convert()
    #
    # TextSurf4, TextRect4 = text_objects("Press enter to continue", speechText)
    # TextRect4.center = (900,80)
    # TextSurf3, TextRect3 = text_objects("Pick up Kai's bag using the space bar", speechText)
    # TextRect3.center = (900,80)
    # TextSurf1, TextRect1 = text_objects("Use left, right, and up arrows to jump on Kai's bed", speechText)
    # TextRect1.center = (900,80)
    # TextSurf5, TextRect5 = text_objects("Exit the room using the enter key", speechText)
    # TextRect5.center = (900,80)

    dialogue = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)

    TextSurf_n, TextRect_n = text_objects2("Press enter to continue.", dialogue)
    TextRect_n.center = (275,80)

    TextSurf_n1, TextRect_n1 = text_objects2("Hi, I'm Kit Kat. That's Kai who's my best friend.", dialogue)
    TextRect_n1.center = (375,80)

    TextSurf_n2, TextRect_n2 = text_objects2("Sometimes, Kai has trouble getting out of bed. Help me wake him up.", dialogue)
    TextRect_n2.center = (480,80)

    TextSurf_n3, TextRect_n3 = text_objects2("Wake up... Kai...", dialogue)
    TextRect_n3.center = (270,80)

    TextSurf_n4, TextRect_n4 = text_objects2("Five more minutes...", dialogue)
    TextRect_n4.center = (275,80)

    TextSurf_n5, TextRect_n5 = text_objects2("Kai, you need to wake up.", dialogue)
    TextRect_n5.center = (280,80)

    TextSurf_n6, TextRect_n6 = text_objects2("Okay, I'm getting up!", dialogue)
    TextRect_n6.center = (278,80)

    TextSurf_n7, TextRect_n7 = text_objects2("Press enter to continue.", dialogue)
    TextRect_n7.center = (280,80)

    TextSurf_n8, TextRect_n8 = text_objects2("Are you ready for school?", dialogue)
    TextRect_n8.center = (width/2,height/2)

    TextSurf_n9, TextRect_n9 = text_objects2("I don't have the energy to deal with school today.", dialogue)
    TextRect_n9.center = (width/2,height/2)

    TextSurf_n10, TextRect_n10 = text_objects2("Stay pawsitive, Kai!", dialogue)
    TextRect_n10.center = (width/2,height/2)

    TextSurf_n11, TextRect_n11 = text_objects2("I'll be by your side; it'll be a good day!", dialogue)
    TextRect_n11.center = (width/2,height/2)

    text_box = pygame.image.load("pics/teal_rect.png")
    text_box.set_alpha(200)
    text_box = pygame.transform.scale(text_box, (width,150))

    text_box_big = pygame.image.load("pics/teal_rect.png")
    text_box_big.set_alpha(200)
    text_box_big = pygame.transform.scale(text_box, (width,height))

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
        #for the backpack
        if not pickedUp:
            screen.blit(bp, (900,400))
        else:
            screen.blit(bp, (player.rect.x+110,player.rect.y+90))

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
        if enter >= 2:
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

        screen.blit(text_box_big,(0,0))

        if jumps < 20:
            screen.blit(text_box,(0,0))
        if jumps > 20 and enter >= 4:
            screen.blit(text_box_big,(0,0))

        if enter == 1 and jumps<10:
            next = 1
        if enter == 2:
            next = 2
        if jumps >=1 and jumps < 5:
            next = 3
        if jumps >= 5 and jumps <10:
            next = 4
        if jumps >= 10 and jumps< 15:
            next = 5
        if jumps >= 17 < 20:
            next = 6
            DoorOpen = True
            KaiUp= True
            if enter >= 2:
                enter = 3
        if jumps > 20 and enter == 3:
            next = 7
        if jumps > 20 and enter == 4:
            next = 8
        if jumps > 20 and enter == 5:
            next = 9
        if jumps > 20 and enter == 6:
            next = 10
        if jumps > 20 and enter == 7:
            next = 11

        if next == 0:
            screen.blit(TextSurf_n,TextRect_n)
        if next == 1:
            screen.blit(TextSurf_n1,TextRect_n1)
        if next == 2:
            screen.blit(TextSurf_n2,TextRect_n2)
        if next == 3:
            screen.blit(TextSurf_n3,TextRect_n3)
        if next == 4:
            screen.blit(TextSurf_n4,TextRect_n4)
            screen.blit(kaicon, (25,15))
        if next == 5:
            screen.blit(TextSurf_n5,TextRect_n5)
        if next == 6:
            screen.blit(TextSurf_n6,TextRect_n6)
            screen.blit(kaicon, (25,15))
        if next == 7:
            screen.blit(TextSurf_n7,TextRect_n7)
        if next == 8:
            screen.blit(TextSurf_n8,TextRect_n8)
        if next == 9:
            screen.blit(TextSurf_n9,TextRect_n9)
        if next == 10:
            screen.blit(TextSurf_n10,TextRect_n10)
        if next == 11:
            screen.blit(TextSurf_n11,TextRect_n11)


        # if KaiUp:
        #     if enter == 2:
        #         jumps = 15
        #         screen.blit(readyy, (0,0))
        #         player.rect.x= -200
        #     elif enter == 3:
        #         screen.blit(noenergy, (0,0))
        #     elif enter == 4:
        #         screen.blit(pawsitive, (0,0))
        #     elif enter == 5:
        #         player.rect.x= 400
        #         enter =6
        #     elif enter == 6:
        #         screen.blit(TextSurf3,TextRect3)
        #     elif enter >= 7:
        #         screen.blit(TextSurf5,TextRect5)


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
