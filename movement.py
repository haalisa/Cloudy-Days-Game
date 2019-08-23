import pygame
from pygame.locals import *
walls= []
class Cat (pygame.sprite.Sprite):
    def __init__(self):
        super(Cat, self).__init__()
        self.image = pygame.image.load("KIT_KAT/kitkat_right2.png")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 355 #change y position
        self.radius = int(self.rect.width / 2)
        self.isjump = 0
        self.v = 8
    def move(self, dx):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.rect.x += dx
        # If you collide with a wall, move out based on velocity
        # for wall in walls:
        #     if self.rect.colliderect(wall.rect):
        #         if dx > 0: # Moving right; Hit the left side of the wall
        #             self.rect.right = wall.rect.left
        #         if dx < 0: # Moving left; Hit the right side of the wall
        #             self.rect.left = wall.rect.right

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
                        self.isjump = 0
                        self.v=8


            if self.rect.y >= 370:
                self.rect.y = 370
                self.isjump = 0
                self.v=8

        elif self.isjump==0:
            for wall in walls:
                if not self.rect.colliderect(wall.rect):
                    self.isjump= 1
                    self.v =0


class Wall(pygame.sprite.Sprite):
    def __init__(self,pos):
        walls.append(self)
        # self.surf = pygame.Surface((250,100))
        # self.rect = self.surf.get_rect(center(pos[0], pos[1]))
        self.rect = pygame.Rect(pos[0],pos[1], 250, 100)

    def delet(self):
        walls.remove(self)

class Kai (pygame.sprite.Sprite):
    def __init__(self):
        super(Kai, self).__init__()
        self.image = pygame.image.load("KAi/kai(l).png")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 250 #change y position
        self.radius = int(self.rect.width / 2)
        self.isjump = 0
        self.gotox= self.rect.x
        self.gotoy= self.rect.y
    def update(self):
        if self.rect.x > self.gotox :
            self.rect.x -= 3
            self.image = pygame.image.load("KAi/kai(l).png")
        elif self.rect.x < self.gotox :
            self.rect.x += 3
            self.image = pygame.image.load("KAi/kai(r).png")
        if self.rect.y > self.gotoy:
            self.rect.y -= 3
        elif self.rect.y <self.gotoy:
            self.rect.y += 3
class Kainobackpack (pygame.sprite.Sprite):
    def __init__(self):
        super(Kainobackpack, self).__init__()
        self.image = pygame.image.load("KAI/kai1.png")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 250 #change y position
        self.radius = int(self.rect.width / 2)
        self.isjump = 0
        self.gotox= self.rect.x
        self.gotoy= self.rect.y
    def update(self):
        if self.rect.x > self.gotox :
            self.rect.x -= 3
            self.image = pygame.image.load("KAi/kai(wwl).png")
        elif self.rect.x < self.gotox :
            self.rect.x += 3
            self.image = pygame.image.load("KAi/kai1.png")
        if self.rect.y > self.gotoy:
            self.rect.y -= 3
        elif self.rect.y <self.gotoy:
            self.rect.y += 3
