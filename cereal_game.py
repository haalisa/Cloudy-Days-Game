# cereal game
# to do:
# link to kitchen
# make multiple oreos if enough time

import pygame
from pygame.locals import *
# import transitions
# from transitions import *
import random
from movement2 import *

# import start_menu this is what is causing only lvl 1 to run
# import level_two

#defining screen
width, height = 1200,600
screen = pygame.display.set_mode((width, height))

class Oreo(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.image.load("pics/oreo.png")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.image = pygame.transform.scale(self.image, (50,50))
        super(Oreo,self).__init__()
        self.rect= self.image.get_rect(
            center = (random.randint(0,600), random.randint(5,10))
        )
        self.cereal_count = 0
        #radius

    def update(self):
        # fall until its y is more than 650
        if self.rect.y < 650:
            self.rect.y += 1

        # if it falls offscreen, reappear to top and fall again
        if self.rect.y >= 650:
            self.rect.x = random.randint(10,1100)
            self.rect.y = random.randint(-150,-10)

        # if touching, add point and disappear
        if player.rect.colliderect(o.rect):
            self.rect.x = random.randint(10,1100)
            self.rect.y = random.randint(-150,-10)
            self.cereal_count += 1

player = Cat()

o = Oreo()

oreos = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Create a custom event for adding a new enemy.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 150)

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def cerealgame ():
    pygame.init()
    # flags = FULLSCREEN | DOUBLEBUF
    width, height = 1200,600
    screen = pygame.display.set_mode((width, height))

    #define colors
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    lightBlue = (180,180,225)
    darkBlue = (141,138,186)
    darkerBlue = (114,111,161)
    brown = (111,83,76)

    # transitions.init ( screen, width, height )

    truevar = True
    clock = pygame.time.Clock()

    clock.tick(60)

    # click = pygame.mouse.get_pressed()
    # mouse = pygame.mouse.get_pos()
    while truevar:
        screen.fill(darkBlue)

        #defining text for instructions
        instructions = pygame.font.Font('fonts/Roboto-Light.ttf', 30)
        TextSurf_i, TextRect_i = text_objects("Reach 15 oreos to win.", instructions)
        TextRect_i.center = (600,300)
        screen.blit(TextSurf_i,TextRect_i)

        # runs the update function
        o.update()

        # draws oreo
        screen.blit(o.image, o.rect)

        # defining text score
        score_text = pygame.font.Font('fonts/Roboto-Light.ttf', 50)
        TextSurf_score, TextRect_score = text_objects("score:", score_text)
        TextRect_score.center = (100,50)
        screen.blit(TextSurf_score,TextRect_score)

        cereal_count_text = pygame.font.Font('fonts/Roboto-Light.ttf', 50)
        TextSurf_cc, TextRect_cc = text_objects(str(o.cereal_count), cereal_count_text)
        TextRect_cc.center = (250,50)
        screen.blit(TextSurf_cc,TextRect_cc)

        # draws the cat
        screen.blit(player.image, player.rect)


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
            elif(event.type == ADDENEMY):
                new_oreo = Oreo()
                oreos.add(new_oreo)
                all_sprites.add(new_oreo)
        oreos.update()

        # if o.cereal_count >= 1:
        #     # truevar = False
        #     level_two.leveltwo()

        pygame.display.flip()

            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     click_img = event.pos

cerealgame () #take this out later
