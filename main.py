import pygame

# import functions
import start_menu

#main function running
def main ():
    pygame.init()

    #play music
    # pygame.mixer.music.load('music/bg-music.wav')
    # pygame.mixer.music.play(-1)

    #go to start menu
    start_menu.game_intro()

if __name__ == '__main__':
    main()
