import pygame
from pygame.locals import *
# import transitions
#
# transitions.init ( screen, window_width, window_height [ , background_color = [0, 0, 0] ] )
# clock = pygame.time.Clock()

# flags = FULLSCREEN | DOUBLEBUF

#define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
lightBlue = (224,223,236)
darkBlue = (141,138,186)
darkerBlue = (114,111,161)

#defining screen
width, height = 1200,600
screen = pygame.display.set_mode((width, height))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():

    while True:
        #setting up stage
        screen.fill(lightBlue)
        # cloud1 = pygame.image.load("pics/cloud1.png").convert()
        # cloud1 = pygame.transform.scale(cloud1,(100,100))
        # # cloud2 = pygame.image.load("pics/cloud2.png")
        # screen.blit(cloud1, (0,0))
        # screen.blit(cloud2, (0,0))

        #buttons
        mouse = pygame.mouse.get_pos()
        buttonPos = ((width/2)-50,450,100,50)
        startButton = pygame.draw.rect(screen, darkBlue, buttonPos)

        if startButton.collidepoint(mouse):
            startButton = pygame.draw.rect(screen, darkerBlue,buttonPos)
        else:
            startButton = pygame.draw.rect(screen, darkBlue,buttonPos)

        #if button is clicked
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and startButton.collidepoint(mouse):
            levelone()

        #define texts
        largeText = pygame.font.Font('fonts/Roboto-Thin.ttf', 100)
        TextSurf, TextRect = text_objects("Cloudy Days", largeText)
        TextRect.center = ((width/2),(height/2)-100)

        descriptionText = pygame.font.Font('fonts/Roboto-Thin.ttf', 30)
        TextSurf1, TextRect1 = text_objects("a game about mental health", descriptionText)
        TextRect1.center = ((width/2),(height/2))

        buttonText = pygame.font.Font('fonts/Roboto-Thin.ttf', 35)
        TextSurf2, TextRect2 = text_objects("start", buttonText)
        TextRect2.center = ((width/2),470)

        #draw texts
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf1, TextRect1)
        screen.blit(TextSurf2, TextRect2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   exit(0)

def levelone ():

    truevar = True
    hideText = True
    clock = pygame.time.Clock()
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    while truevar:
        bg = pygame.image.load("pics/lvl-bgs/bedroom.png").convert()
        bg = pygame.transform.scale(bg, (width,height))
        screen.blit(bg, (0,0))
        #
        # cueBubble = pygame.time.set_timer(USEREVENT+1, 100)

        #player
        # krabsPos = [0,100] #player position
        # krabs = pygame.image.load("pics/krabs.png")
        # # krabs.transform.scale(250,350)
        # screen.blit(krabs, krabsPos) #draw screen elements

        #hide or not hide speech bubble
        if hideText == True:
            speechPos = [1500,1000,300,200]
        else:
            speechPos = [0,100,300,200]
            screen.blit(TextSurf4,TextRect4)

        #speech bubble drawn
        speechBubble = pygame.draw.ellipse(screen, darkBlue, speechPos) #position,size

        #the go back button
        button2Pos = (1000,100,100,50)
        goBackButton = pygame.draw.rect(screen, red, button2Pos)

        if goBackButton.collidepoint(mouse):
            goBackButton = pygame.draw.rect(screen, red,button2Pos)
        else:
            startButton = pygame.draw.rect(screen, white,button2Pos)

        #if button is clicked

        if click[0] == 1 and goBackButton.collidepoint(mouse):
            print("wassup")
            game_intro()
            truevar = False

        #defining texts
        #button text
        buttonText = pygame.font.Font('fonts/Roboto-Thin.ttf', 25)
        TextSurf3, TextRect3 = text_objects("go back", buttonText)
        TextRect3.center = (1050,125)

        #speech bubble text
        speechText = pygame.font.Font('fonts/Roboto-Thin.ttf', 20)
        TextSurf4, TextRect4 = text_objects("Hello world! Sample text!", speechText)
        TextRect4.center = (450,200)

        screen.blit(TextSurf3,TextRect3)

        # if click[0] == 1 and krabs.collidepoint(mouse):
        #     print("wassup")
        #     hideText = False

        pygame.display.flip()

        runSecondTime = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   exit(0)

def main ():
    level = 0;
    pygame.init()
    game_intro()

    # if level == 1:
    #     levelone ()
    #     print("hi")



if __name__ == '__main__':
    main()
