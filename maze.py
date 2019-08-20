
import os
import random
import pygame
from pygame.locals import *

import level_three_aftermaze

flags = FULLSCREEN | DOUBLEBUF

class Cat (pygame.sprite.Sprite):
    def __init__(self):
        super(Cat, self).__init__()
        self.image = pygame.image.load("smallcat.png")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 700
        self.radius = int(self.rect.width / 2)

    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Class for the orange dude
class Player(object):

    def __init__(self):
        super(Player, self).__init__()
        # self.image = pygame.image.load("smallcat.png")
        # self.image.set_colorkey((255, 255, 255), RLEACCEL)
        # self.rect = self.image.get_rect(
        # center = (25,25)
        # )
        self.rect = pygame.Rect(32, 32, 16, 16)


    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)


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
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def main():
    running = True

    # Set up the display
    pygame.display.set_caption("Get to the red square!")
    screen = pygame.display.set_mode((1200, 800), flags)
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
            player.move(-3, 0)
        if key[pygame.K_RIGHT]:
            player.move(3, 0)
        if key[pygame.K_UP]:
            player.move(0, -3)
        if key[pygame.K_DOWN]:
            player.move(0, 3)

        # Just added this to make it slightly fun ;)
        # if player.rect.colliderect(end_rect):
        #     raise SystemExit, "You win!"

        # making cat move
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        # Draw the scene
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        # pygame.draw.rect(screen, (255, 200, 0), player.rect)
        mouse = pygame.mouse.get_pos()
        # print(mouse)
        if player.rect.x > 100:
            # youwin = pygame.font.Font('fonts/arcade.ttf', 100)
            # TextSurf_yw, TextRect_yw = text_objects("YOU WIN", youwin)
            # TextRect_yw.center = (600,400)
            # screen.blit(TextSurf_yw, TextRect_yw)
            # pygame.time.delay(5000)
            level_three_aftermaze.levelthreeaftermaze()

        screen.blit(player.image, player.rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()
