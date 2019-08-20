import pygame
from pygame.locals import *
walls= []

class Cat (pygame.sprite.Sprite):

    #makes the cat
    def __init__(self):
        super(Cat, self).__init__()
        self.image = pygame.image.load("pics/cat.gif")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 260 #change y position
        self.radius = int(self.rect.width / 2)
        self.isjump = 0
        self.v = 8 #velocity

    #moves cat
    def move(self, dx):
        # if x not moving then move by dx
        if dx != 0:
            self.rect.x += dx

        # if you collide with a wall left/right, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right

    def jump(self):
        self.isjump = 1 #1 is true

    def update(self):
        #if jump is called and velocity is more than 0 then
        if self.isjump:
            if self.v > 0:
                dy = -(.25*self.v*self.v) #apply gravity to make bounce more realistic
            else:
                for wall in walls:
                    dy = (.25*self.v*self.v) # add extra bounce/speed
                    if self.rect.colliderect(wall.rect):
                        if dy > 0: # Moving down; Hit the top side of the wall
                            dy = 0
                            self.isjump = 0
                            self.v=8



            self.rect.y += dy
            self.v -= .25



            if self.rect.y >= 260:
                self.rect.y = 260
                self.isjump = 0
                self.v=8
                print("Bottom3: ")
                print(self.rect.bottom)
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)
