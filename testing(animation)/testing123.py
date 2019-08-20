# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))

# 3 - Load images

player = pygame.image.load("bird1.png")
playermovement = pygame.image.load("bird2.png")
background = pygame.image.load("house.jpg")
keys = [False, False, False, False]
playerpos = [100,100]
movement = 0
pressed = pygame.key.get_pressed()

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(background,(0,0))

#when the keys are not pressed, then do a "default" frame/animation to show character is not moving

#WE GOT THE MOVEMENT FOR TWO FRAMES \(O w O)/-----------------------------------
    if movement < 23:
        screen.blit(player, playerpos)
    else:
        screen.blit(playermovement, playerpos)
    if movement > 46:
        movement = 0

#-------------------------------------------------------------------------------
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

#this connects the keys with the numbers down below
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

    # 9 - Move player
    if keys[0]:
        playerpos[1]-=5
        movement = movement + 1
    elif keys[2]:
        playerpos[1]+=5
        movement = movement + 1
    if keys[1]:
        playerpos[0]-=5
        movement = movement + 1
    elif keys[3]:
        playerpos[0]+=5
        movement = movement + 1
