import pygame
from pygame import *
pygame.init()
screen = pygame.display.set_mode((1000,500))
done = False
is_blue = True
x=30
y=30
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue  # Тек SPACE басылғанда ғана өзгерсін
    # pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(40, 40, 100, 100)) 
    #"pygame.Rect(40, 40, 100, 100))" бірінші екі координата шеттерінен арақашықтық, келесі екі координата ені мен ұзындығы
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 2
    if pressed[pygame.K_DOWN]: y += 2
    if pressed[pygame.K_LEFT]: x -= 2
    if pressed[pygame.K_RIGHT]: x += 2
    screen.fill((0, 0, 0))
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))  
    pygame.display.flip()
    clock.tick(100)