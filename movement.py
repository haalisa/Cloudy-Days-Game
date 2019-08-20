import pygame
from pygame.locals import *
walls= []
class Cat (pygame.sprite.Sprite):
    def __init__(self):
        super(Cat, self).__init__()
        self.image = pygame.image.load("pics/cat.gif")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 260 #change y position
        self.radius = int(self.rect.width / 2)
        self.isjump = 0

    def move(self, dx):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.rect.x += dx
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right

    def jump(self):
    

        self.isjump = 1


    def update(self):
        if self.isjump:

            if self.v > 0:
                dy = -(.25*self.v*self.v)
            else:
                dy = (.25*self.v*self.v)

            self.rect.y += dy
            self.v -= 0.25

            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dy> 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top

                    if not self.rect.colliderect(wall.rect):
                        self.isjump= 1
                        self.v =0

            if self.rect.y >= 260:
                self.rect.y = 260
                self.isjump = 0
                self.v=8
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 50, 50)
