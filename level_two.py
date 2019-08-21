#kitchen

import pygame
from pygame.locals import *
# import transitions
# from transitions import *
# import random

# start of the dialogue for Kit Kat and Kai
    #Kit Kat is trying to cheer up Kai for school. Kit kat believes that it will be a good day, but Kai disagrees saying that it is just the usual mundane day.
    #Kit Kat goes over to the cereal and says that it will make Kai a bowl of Oreo-O's (his favorite)


# import cereal_game

# import start_menu this is what is causing only lvl 1 to run

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def leveltwo ():

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
    # transitions.init ( screen, width, height )

    truevar = True
    clock = pygame.time.Clock()

    clock.tick(180)

    pygame.init()

    full_kitchen = pygame.image.load("pics/lvl-bgs/full_kitchen.png").convert()
    full_kitchen = pygame.transform.scale(full_kitchen, (width,height))

    while truevar:
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()

        cerealRectPos = (520,126,60,78)
        cerealRect = pygame.draw.rect(screen, white, cerealRectPos)

        screen.blit(full_kitchen, (0,0))

        dialoguebarPos = (90,380,1000,300)
        dialoguebar = pygame.draw.rect(screen, white, dialoguebarPos)

        beforekitchentext = pygame.font.Font('fonts/arcade.ttf', 50)
        TextSurf, TextRect = text_objects("Kai", beforekitchentext)
        TextRect.center = (200,520)
        screen.blit(TextSurf,TextRect)

        kaicon = pygame.image.load("KAI/uh.png")
        kaicon = pygame.transform.scale(kaicon, (width,height))
        screen.blit(kaicon,(-400,100))

        cereal = pygame.image.load("pics/lvl-bgs/cereal.png")
        cereal = pygame.transform.scale(cereal, (60,78))
        test_rect2 = cereal.get_rect()
        screen.blit(cereal, (520,126))

        if click[0] == 1 and cerealRect.collidepoint(mouse):
            truevar = False
            cereal_game.cerealgame()

        screen.blit(cereal,(520, 126))
        #
        # chair1 = pygame.image.load("pics/lvl-bgs/chair1.png")
        # chair1 = pygame.transform.scale(chair1, (width,height))
        # screen.blit(chair1, (0,0))
        #
        # chair2 = pygame.image.load("pics/lvl-bgs/chair2.png")
        # chair2 = pygame.transform.scale(chair2, (width,height))
        # screen.blit(chair2, (0,0))
        #
        # bowl = pygame.image.load("pics/lvl-bgs/bowl.png")
        # bowl = pygame.transform.scale(bowl, (width,height))
        # screen.blit(bowl, (0,0))
        #
        # cereal = pygame.image.load("pics/lvl-bgs/cereal.png")
        # cereal = pygame.transform.scale(cereal, (60,78))
        # screen.blit(cereal, (520,126))
        #
        # door_out = pygame.image.load("pics/lvl-bgs/doorout.png")
        # door_out = pygame.transform.scale(door_out, (width,height))
        # screen.blit(door_out, (0,0))
        #
        # kitchen_door = pygame.image.load("pics/lvl-bgs/kitchen_door.png")
        # kitchen_door = pygame.transform.scale(kitchen_door, (width,height))
        # screen.blit(kitchen_door, (0,0))

# needs to have dialogue for Kai and Kit Kat after the cereal game



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

leveltwo()
