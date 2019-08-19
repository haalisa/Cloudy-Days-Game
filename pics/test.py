import pygame
from pygame.locals import *
import random
#initialize game
pygame.init()
pygame.display.set_caption('test')
clock = pygame.time.Clock()
#screen size
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

#beginning position
playerpos = [200,200]
coinpos = [random.randint(0,600), random.randint(0,400)]

# print(coinpos)

class Player (pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("cat.gif")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center = (300,350)
        )
        self.radius = int(self.rect.width / 2)

    def update(self, pressed_keys):
        if pressed_keys[K_UP] :
            self.rect.move_ip(0, -3)
        
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT] :
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT] :
            self.rect.move_ip(3, 0)

        if self.rect.colliderect(block_rect):
            if pressed_keys[K_RIGHT]: # Moving right; Hit the left side of the wall
                self.rect.right = block_rect.left
            if pressed_keys[K_LEFT]: # Moving left; Hit the right side of the wall
                self.rect.left = block_rect.right
            if pressed_keys[K_DOWN]: # Moving down; Hit the top side of the wall
                self.rect.bottom = block_rect.top
            if pressed_keys[K_UP]: # Moving up; Hit the bottom side of the wall
                self.rect.top = block_rect.bottom

        # Keep player on the screen
        if self.rect.left < -50:
            self.rect.left = -50
        elif self.rect.right > 650:
            self.rect.right = 650
        if self.rect.top <= -50:
            self.rect.top = -50
        elif self.rect.bottom >= 500:
            self.rect.bottom = 500

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin,self).__init__()
        self.image = pygame.image.load("coin.png")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.image = pygame.transform.scale(self.image, (15,22))
        self.rect= self.image.get_rect(
            center =(random.randint(0,600), random.randint(200,400))
        )
        self.radius = int(self.rect.width / 2)

#pictures!
player = Player()
forest = pygame.image.load("forest.jpg")

coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

for i in range (8):
    i = Coin()
    coins.add(i)
    all_sprites.add(i)

block_rect = pygame.Rect(200,150,50,100)

while True:
    screen.fill(0)
    screen.blit(forest,(0,0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    rectangle = pygame.draw.rect(screen, (0,0,0), block_rect)

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    for coin in coins:
        if pygame.sprite.collide_circle(player, coin):
            coin.kill()

    pygame.display.flip()
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit(0)
