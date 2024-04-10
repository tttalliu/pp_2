import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#fps
pygame.time.Clock().tick(60)

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

W=400
H=600
SPEED = 5
SCORE = 0

#fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, WHITE)

#bg
background = pygame.image.load("AnimatedStreet.png")

#screen
screen=pygame.display.set_mode((W,H))

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, H-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        keys=pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < 600:        
              if keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top>H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)

class rndm_coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top>H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)

#LIM
n=50

# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2=rndm_coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

#increasing the speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    screen.blit(scores, (W - scores.get_width() - 10, 10))
    #CHECK AND INC
    if SCORE>=n:
        for enemy in enemies:
            enemy.rect.move_ip(0.5, SPEED)

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound("coin.wav").play()
        for coin in coins:
            if coin==C1:
                SCORE += 1
            elif coin==C2:
                SCORE+=10
            coin.rect.top = 0
            coin.rect.center = (random.randint(10, W-10), 0)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(1)
        screen.fill(BLACK)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    pygame.time.Clock().tick(60)