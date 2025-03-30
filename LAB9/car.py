#Imports
import pygame, sys # type: ignore
from pygame.locals import * # type: ignore
import random, time
import pygame.transform # type: ignore

from pygame.sprite import Group # type: ignore
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load(r"AnimatedStreet.png")

# coins counter and the last time a coin spawned
COINS_COUNTER = 0
last_coin_time = pygame.time.get_ticks()
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

N = 0


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]: # type: ignore
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:# type: ignore
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:# type: ignore
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:# type: ignore
                  self.rect.move_ip(5, 0)

# Coin class 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    
    def move(self):
        self.rect.move_ip(0, SPEED)

                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins_group = pygame.sprite.Group()
coins_group.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)



def game_start(): 
    global SCORE, COINS_COUNTER, SPEED, last_coin_time
    #Game Loop
    while True:
        
        #Cycles through all events occurring  
        for event in pygame.event.get():
            
            if event.type == QUIT: # type: ignore
                pygame.quit()
                sys.exit()
    
        DISPLAYSURF.blit(background, (0,0))
        scores = font_small.render(str(SCORE), True, BLACK)
        DISPLAYSURF.blit(scores, (10,10))
        coins = font_small.render(str(COINS_COUNTER), True, BLACK)
        DISPLAYSURF.blit(coins, (370, 10))
    
        #Moves and Re-draws all Sprites
        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
        
        # Coin collection logic
        if pygame.sprite.spritecollideany(P1, coins_group):
            a = random.randint(1, 4)# Randomly add 1 to 3 coins
            COINS_COUNTER += a
            SPEED += a/100

            entity.kill()  # remove the coin

        
            

        # Coin generation logic
        current_time = pygame.time.get_ticks()
        if current_time - last_coin_time > 5000:
            new_coin = Coin()
            all_sprites.add(new_coin)
            coins_group.add(new_coin)
            last_coin_time = current_time  

        #To be run if collision occurs between Player and Enemy
        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound(r'crash.wav').play()
            time.sleep(0.5)
                        
            DISPLAYSURF.fill(RED)
            DISPLAYSURF.blit(game_over, (30,250))
            
            pygame.display.update()
            for entity in all_sprites:
                    entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()        
            
        pygame.display.update()
        FramePerSec.tick(FPS)

# Game intro

intro = True
while intro:
    for event in pygame.event.get():
        if event.type == QUIT: # type: ignore
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(WHITE)
    intro_text = font.render("Press(4-8)", True, BLACK)
    DISPLAYSURF.blit(intro_text, (10, 250))
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[K_4]: # type: ignore
         N = 4
         game_start()
    elif keys[K_5]: # type: ignore
         N = 5  
         game_start()
    elif keys[K_6]: # type: ignore
         N = 6
         game_start()
    elif keys[K_7]: # type: ignore
         N = 7
         game_start()
    elif keys[K_8]: # type: ignore
         N = 8
         game_start()