#kitchen

import pygame
from pygame.locals import *
# import transitions
# from transitions import *
import random
from movement2 import *

# import start_menu this is what is causing only lvl 1 to run

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def cerealgame ():

    pygame.init()
    # flags = FULLSCREEN | DOUBLEBUF

    #define colors
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    lightBlue = (180,180,225)
    darkBlue = (141,138,186)
    darkerBlue = (114,111,161)
    brown = (111,83,76)

    #defining screen
    width, height = 1200,600
    screen = pygame.display.set_mode((width, height))
    # transitions.init ( screen, width, height )

    truevar = True
    clock = pygame.time.Clock()


    clock.tick(60)

    x = random.randint(0,1200)
    y = random.randint(-100,-10)

    newx = random.randint(0,1200)
    newy = random.randint(-250,-10)

    newestx = random.randint(0,1200)
    newesty = random.randint(-500,-250)

    cereal_count = 0

    player = Cat()

    while truevar:
        screen.fill(darkBlue)
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()

        # creates 3 OREO O's
        # o = pygame.draw.circle(screen, brown, (x,y),20,10)
        # o2 = pygame.draw.circle(screen, brown, (newx,newy),20,10)
        # o3 = pygame.draw.circle(screen, brown, (newx,newy),20,10)
        o = pygame.draw.rect(screen, brown, (520,126,60,78))

        # makes 3 OREO O's fall
        if y < 650:
            y = y + 1
        elif y >= 650:
            x = random.randint(0,1200)
            y = random.randint(-150,-10)

        if newy < 650:
            newy = newy + 1
        elif newy >= 650:
            newx = random.randint(0,1200)
            newy = random.randint(-500,-200)

        if newesty < 650:
            newesty = newesty + 1
        elif newesty >= 650:
            newestx = random.randint(0,1200)
            newesty = random.randint(-700,-500)

        # tracks cereal collected
        if o.rect.colliderect(player.rect):
            cereal_count += 1
            print("hello world")
        # collide = pygame.sprite.collide_mask(player, o)
        # if collide:
        #     print("collided")
        # if player_surface.collidepoint(o):
        #     cereal_count = cereal_count + 1
        # elif player.collidepoint(o2):
        #     cereal_count = cereal_count + 1
        # elif player.collidepoint(o3):
        #     cereal_count = cereal_count + 1

        # defining text score
        score_text = pygame.font.Font('fonts/Roboto-Light.ttf', 50)
        TextSurf_score, TextRect_score = text_objects("score:", score_text)
        TextRect_score.center = (100,50)
        screen.blit(TextSurf_score,TextRect_score)

        cereal_count_text = pygame.font.Font('fonts/Roboto-Light.ttf', 50)
        TextSurf_cc, TextRect_cc = text_objects(str(cereal_count), cereal_count_text)
        TextRect_cc.center = (250,50)
        screen.blit(TextSurf_cc,TextRect_cc)

        screen.blit(player.image, player.rect)

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

            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     click_img = event.pos

cerealgame ()
