import pygame
from pygame.locals import *
import random
from movement3 import Cat

from movement3 import Wall
# from movement import Cat
#
# from movement import Wall
#initialize game
pygame.init()
pygame.display.set_caption('test')
clock = pygame.time.Clock()
#screen size
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

#beginning position
coinpos = [random.randint(0,600), random.randint(0,400)]

# print(coinpos)


# class Coin(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Coin,self).__init__()
#         self.image = pygame.image.load("coin.png")
#         self.image.set_colorkey((255, 255, 255), RLEACCEL)
#         self.image = pygame.transform.scale(self.image, (15,22))
#         self.rect= self.image.get_rect(
#             center =(random.randint(0,600), random.randint(200,400))
#         )
#         self.radius = int(self.rect.width / 2)

#pictures!
player = Cat()
forest = pygame.image.load("pics/forest.jpg")

# coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# for i in range (8):
#     i = Coin()
#     coins.add(i)
#     all_sprites.add(i)

block = Wall((200, 250))

while True:
    screen.fill(0)
    screen.blit(forest,(0,0))
    player.update()
    rectangle = pygame.draw.rect(screen, (0,0,0), block)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-3)
    if key[pygame.K_RIGHT]:
        player.move(3)
    if key[pygame.K_UP]:
        player.jump()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # for coin in coins:
    #     if pygame.sprite.collide_circle(player, coin):
    #         coin.kill()

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
