import pygame
from pygame.locals import *

#class for player sprite
class Player (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

pygame.init()
width, height = 1200,700
screen = pygame.display.set_mode((width, height))

playerpos = [100,100] #player position
player_img = pygame.image.load("pics/krabs.png").convert()
player = Player()

all_sprites = pygame.sprite.Group() #makes all sprites group
all_sprites.add(player)


# bg = pygame.image.load("pics/bg.jpg")


all_sprites.draw(screen)


# forever looping
while 1:

    keys = [False, False, False, False]
    screen.fill((255,255,255)) #clear screen before drawing again

    # screen.blit(bg, (0,0))

    # screen.blit(player, playerpos) #draw screen elements
    all_sprites = pygame.sprite.Group() #makes all sprites group
    all_sprites.add(player)


    # bg = pygame.image.load("pics/bg.jpg")

    all_sprites.draw(screen)


    pygame.display.flip() #update screen

    #loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # movement();
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

            # Move player
    if keys[0]:
        playerpos[1]-=5 #move height down
    elif keys[2]:
        playerpos[1]+=5 #move height up
    if keys[1]:
        playerpos[0]-=5 #move width left
    elif keys[3]:
        playerpos[0]+=5 #move width right



    #
    # if playerpos[0] >= width and key[1] = True:
    #     keys[1] = True
    #
    # if playerpos[1] <= width and key[3] = True:
    #     keys[0] = True
