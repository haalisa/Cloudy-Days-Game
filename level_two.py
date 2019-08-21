#kitchen

import pygame
from pygame.locals import *

# start of the dialogue for Kit Kat and Kai
    #Kit Kat is trying to cheer up Kai for school. Kit kat believes that it will be a good day, but Kai disagrees saying that it is just the usual mundane day.
    #Kit Kat goes over to the cereal and says that it will make Kai a bowl of Oreo-O's (his favorite)

import cereal_game
import level_two_outside
from movement import *

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

    player = Cat()
    table = Wall((150,470))
    full_kitchen = pygame.image.load("pics/lvl-bgs/full_kitchen.png").convert()
    full_kitchen = pygame.transform.scale(full_kitchen, (width,height))

    kaicon = pygame.image.load("KAI/uh.png")
    kaicon = pygame.transform.scale(kaicon, (width,height))

    beforekitchentext = pygame.font.Font('fonts/arcade.ttf', 50)
    TextSurf, TextRect = text_objects("Kai", beforekitchentext)
    TextRect.center = (200,520)

    kitkat_thought_text = pygame.font.Font('fonts/cambria.ttf', 20)
    TextSurf1, TextRect1 = text_objects("Oops, we need to do something first!", kitkat_thought_text)


    didplaycereal = False

    player.rect.x = 1000

    player.image = pygame.image.load("KIT_KAT/kitkat_left2.png")

    while truevar:
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        cerealRectPos = (520,126,60,78)
        cerealRect = pygame.draw.rect(screen, white, cerealRectPos)

        screen.blit(full_kitchen, (0,0))
        rectangle = pygame.draw.rect(screen, (0,0,0), table)
        key = pygame.key.get_pressed()

        #DIALOGUE GOES HERE
        if key[pygame.K_RETURN]:
            dialoguebarPos = (90,380,1000,300)
            dialoguebar = pygame.draw.rect(screen, white, dialoguebarPos)

            screen.blit(TextSurf,TextRect)
            screen.blit(kaicon,(-400,100))

        cereal = pygame.image.load("pics/lvl-bgs/cereal.png")
        cereal = pygame.transform.scale(cereal, (60,78))
        test_rect2 = cereal.get_rect()
        screen.blit(cereal, (520,126))

        if didplaycereal == False:
            if click[0] == 1 and cerealRect.collidepoint(mouse):
                didplaycereal = True
                cereal_game.cerealgame()
                continue

        if click[0] == 1 and cerealRect.collidepoint(mouse):
            truevar = False
            cereal_game.cerealgame()

        screen.blit(cereal,(520, 126))

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

        if didplaycereal == True:
            if player.rect.x < -100:
                level_two_outside.leveltwooutside()

        # if didplaycereal == False:
        #     if player.rect.x < -100:
        #         kitkat_thoughtpos = (player.rect.x + 75, player.rect.y - 100, 100,75)
        #         kitkat_thought = pygame.draw.ellipse(screen, white, kitkat_thoughtpos)
        #
        #         TextRect1.center = (player.rect.x - 200, player.rect.y - 50)
        #         screen.blit(TextSurf1,TextRect1)

        #
        # kitchen = pygame.image.load("pics/lvl-bgs/kitchen.png").convert()
        # kitchen = pygame.transform.scale(kitchen, (width,height))
        # screen.blit(kitchen, (0,0))
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

# leveltwo()
