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

def text_objects2(text, font):
    white = (255,255,255)
    textSurface = font.render(text, True, white)
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

    truevar = True
    clock = pygame.time.Clock()
    enter= 0

    clock.tick(180)

    pygame.init()


    full_kitchen = pygame.image.load("pics/lvl-bgs/full_kitchen.png").convert()
    full_kitchen = pygame.transform.scale(full_kitchen, (width,height))


    player = Cat()
    table = Wall((400,400))
    full_kitchen = pygame.image.load("pics/lvl-bgs/full_kitchen.png").convert()
    full_kitchen = pygame.transform.scale(full_kitchen, (width,height))

    kaicon = pygame.image.load("KAI/uh2.png")
    kaicon = pygame.transform.scale(kaicon, (100,130))

    cereal = pygame.image.load("pics/lvl-bgs/cereal.png")
    cereal = pygame.transform.scale(cereal, (60,78))
    test_rect2 = cereal.get_rect()

    # beforekitchentext = pygame.font.Font('fonts/arcade.ttf', 50)
    # TextSurf, TextRect = text_objects("Kai", beforekitchentext)
    # TextRect.center = (100,80)
    dialogue = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)
    TextSurf, TextRect = text_objects2("Don't forget breakfast! It's the most important meal of the day.", dialogue)
    TextRect.center = (500,80)

    TextSurf1, TextRect1 = text_objects2("I have no appetite", dialogue)
    TextRect1.center = (500,80)

    TextSurf2, TextRect2 = text_objects2("You have to eat! I'll get the cereal", dialogue)
    TextRect2.center = (500,80)
    TextSurf3, TextRect3 = text_objects2("Thanks Kit Kat, I appreciate you caring about me :)", dialogue)
    TextRect3.center = (500,80)
    TextSurf4, TextRect4 = text_objects2("I want you to care about yourself, and I know it's hard. But you can get through it.", dialogue)
    TextRect4.center = (500,80)
    TextSurf5, TextRect5 = text_objects2("Yeah...I finished the cereal, let's go!", dialogue)
    TextRect5.center = (500,80)

    TextSurf_n, TextRect_n = text_objects("Press enter to continue!", dialogue)
    TextRect_n.center = (900,540)
    TextSurf_n1, TextRect_n1 = text_objects("Jump to reach the box!", dialogue)
    TextRect_n1.center = (900,540)

    text_box = pygame.image.load("pics/teal_rect.png")
    text_box.set_alpha(200)
    text_box = pygame.transform.scale(text_box, (width,150))





    didplaycereal = False
    next = 0

    player.rect.x = 1000


    player.image = pygame.image.load("KIT_KAT/kitkat_left2.png")
    kai = Kai()
    kai.rect.x = 700
    while truevar:
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        cerealRectPos = (520,126,60,78)
        cerealRect = pygame.draw.rect(screen, white, cerealRectPos)

        rectangle = pygame.draw.rect(screen, (0,0,0), table)

        screen.blit(full_kitchen, (0,0))
        screen.blit(cereal, (520,126))
        screen.blit(text_box, (0,0))
        key = pygame.key.get_pressed()

        if enter == 0:
            next=0
        if enter == 1:
            next=1
        if enter == 2:
            next=2
        if enter == 4 and next==3:
            next=4
        if enter == 5 and next==4:
            next=5

        if next==0:
            screen.blit(TextSurf,TextRect) #dont forget breakfast
            screen.blit(TextSurf_n,TextRect_n) #enter to continue
        if next==1:
            screen.blit(TextSurf1,TextRect1) #appetite
            screen.blit(kaicon,(80,10))
            screen.blit(TextSurf_n,TextRect_n) #enter to continue
        if next==2:
            screen.blit(TextSurf2,TextRect2) #get cereal
            screen.blit(TextSurf_n1,TextRect_n1) #jump
        if next ==3:
            screen.blit(TextSurf3,TextRect3) #thanks kit kat
            screen.blit(kaicon,(80,10))
            screen.blit(TextSurf_n,TextRect_n) #enter tp continue
        if next ==4:
            screen.blit(TextSurf4,TextRect4) #I want you to care about yourself!
            screen.blit(TextSurf_n,TextRect_n) #enter to continure
        if next ==5:
            screen.blit(TextSurf5,TextRect5) #let's go
            screen.blit(kaicon,(80,10))
            kai.gotox= -200
            kai.gotoy= 250

        kai.update()
        screen.blit(kai.image, kai.rect)
        if didplaycereal == False:
            if player.rect.y < 100 and player.rect.x> 420 and player.rect.x<540 :
                didplaycereal = True
                cereal_game.cerealgame()
                next=3
                enter=3
                continue

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
                table.delet()
                level_two_outside.leveltwooutside()

        # if didplaycereal == False:
        #     if player.rect.x < -100:
        #         kitkat_thoughtpos = (player.rect.x + 75, player.rect.y - 100, 100,75)
        #         kitkat_thought = pygame.draw.ellipse(screen, white, kitkat_thoughtpos)
        #
        #         TextRect1.center = (player.rect.x - 200, player.rect.y - 50)
        #         screen.blit(TextSurf1,TextRect1)

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
            if event.type == pygame.KEYDOWN:
                if event.key==K_RETURN:
                    enter += 1

#
# leveltwo()
