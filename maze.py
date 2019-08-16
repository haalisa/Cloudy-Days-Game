
import os
import random
import pygame
from pygame.locals import *
from smallcatclass import Cat
flags = FULLSCREEN | DOUBLEBUF

# Initialise pygame

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((1200, 800), flags)
# ?screen = pygame.display.set_mode((320, 240))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Cat() # Create the player

# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W              W                                                       W",
"W              W                                                       W",
"W              W                                                       W",
"W   WWWWWWWW   W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW   W",
"W   W      W   W                        W                          W   W",
"W   W      W   W                        W                          W   W",
"W   W      W   W                        W                          W   W",
"W   W   WWWW   WWWWWWWWWWWWWWWWWWWWWW   WWWWWWWWWWW   WWWWWWWWWW   W   W",
"W   W   W           W               W             W   W            W   W",
"W   W   W           W               W             W   W            W   W",
"W   W   W           W               W             W   W            W   W",
"W   W   WWWWWWWWW   W   WWWWWWWWW   WWWWWWWWWWW   W   W   WWWWWWWWWW   W",
"W   W   W           W   W       W   W             W   W            W   W",
"W   W   W           W   W       W   W             W   W            W   W",
"W   W   W           W   W       W   W             W   W            W   W",
"W   W   W   WWWWWWWWW   W   W   W   W   WWWWWWWWWWW   WWWWWWWWWW   W   W",
"W   W   W               W   W   W   W                 W            W   W",
"W   W   W               W   W   W   W                 W            W   W",
"W   W   W               W   W   W   W                 W            W   W",
"W   W   WWWWWWWWWWWWWWWWW   W   W   WWWWWWWWWWW   W   W   WWWWWWWWWW   W",
"W   W                       W   W                 W   W            W   W",
"W   W                       W   W                 W   W            W   W",
"W   W                       W   W                 W   W            W   W",
"W   WWWWWWWWWWWWWWWWWWWWW   W   W                 W   WWWWWWWWWW   W   W",
"W                               W                 W            W   W   W",
"W                               W                 W            W   W   W",
"W                               W                 W            W   W   W",
"W   WWWWWWWWWWWWWWWWWWWWWWWWWWWWW                 WWWWWWWWWW   W   W   W",
"W            W                  W                          W   W   W   W",
"W            W                  W        E                 W   W   W   W",
"W            W                  W                          W   W   W   W",
"WWWWWWWWWW   W    WWW   WWWW    WWWWWWWWWWWWWWWWWWWW   WWWWW   W   W   W",
"W        W   W    WWW   WWWW    W       W   W              W   W   W   W",
"W        W   W    WWW   WWWW    W       W   W              W   W   W   W",
"W        W   W    WWW   WWWW    W       W   W              W   W   W   W",
"W   WW   W   W    WWW   WWWW    W   W   W   W   WWWWWWWW   W   W   W   W",
"W   WW   W   W    WWW   WWWW    W   W   W   W   W          W   W   W   W",
"W   WW   W   W    WWW   WWWW    W   W   W   W   W          W   W   W   W",
"W   WW   W   W    WWW   WWWW    W   W   W   W   W          W   W   W   W",
"W   WW   W   WWWWWWWW   WWWW    W   W   W   W   W   WWWWWWWW   W   W   W",
"W   WW   W              WWWW    W   W   W   W   W   W          W   W   W",
"W   WW   W              WWWW    W   W   W   W   W   W          W   W   W",
"W   WW   W              WWWW    W   W   W   W   W   W          W   W   W",
"W   WW   WWWWWWWWWWWWWWWWWWW    W   W   W   W   W   WWWWWWWWWWWW   W   W",
"W   WW                              W           W          W       W    ",
"W   WW                              W           W          W       W    ",
"W   WW                              W           W          W       W    ",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            walls.append(pygame.Rect(x, y, 16, 16))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-3, 0, walls)
    if key[pygame.K_RIGHT]:
        player.move(3, 0, walls)
    if key[pygame.K_UP]:
        player.move(0, -3, walls)
    if key[pygame.K_DOWN]:
        player.move(0, 3, walls)

    # Just added this to make it slightly fun ;)
    # if player.rect.colliderect(end_rect):
    #     raise SystemExit, "You win!"

    # making cat move
    # pressed_keys = pygame.key.get_pressed()
    # player.update(pressed_keys)

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    # pygame.draw.rect(screen, (255, 200, 0), player.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
