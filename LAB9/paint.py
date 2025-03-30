
import pygame # type: ignore
import math

#Intialization pygame
pygame.init()

#Parameters for window
SCREEN_WIDTH, SCREEN_HEIGHT=800, 600
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")

#Colors
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

#Variables
running=True
drawing=False
last_pos=None
draw_mode="line"
color=BLACK
radius=5

#Paint desk
canvas=pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
canvas.fill(WHITE)

#Game cycle
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        #Checking for switching colors, and eraser
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                color=RED
            elif event.key==pygame.K_g:
                color=GREEN
            elif event.key==pygame.K_b:
                color=BLUE
            elif event.key==pygame.K_k:
                color=BLACK
            elif event.key==pygame.K_e:
                color=WHITE
                draw_mode="eraser"
            elif event.key == pygame.K_s:
                draw_mode = "square"
            elif event.key == pygame.K_t:
                draw_mode = "right_triangle"
            elif event.key == pygame.K_y:
                draw_mode = "equilateral_triangle"
            elif event.key == pygame.K_d:
                draw_mode = "rhombus"

        #Checking for line, circle, rectangle
        elif event.type==pygame.MOUSEBUTTONDOWN:
            last_pos=event.pos
            if event.button==1: #LBM-line
                draw_mode="line"
                drawing=True
            elif event.button==3: #RBM-rectangle
                draw_mode="rect"
            elif event.button==2: #CBM-circle
                draw_mode="circle"

        #Case when user clicked to left button of mouse
        elif event.type==pygame.MOUSEMOTION and drawing and draw_mode=="line":
            pygame.draw.line(canvas, color, last_pos, event.pos, radius)
            last_pos=event.pos

        #Case when user clicked to right button of mouse or central one       
        elif event.type==pygame.MOUSEBUTTONUP:
            x1, y1 = last_pos
            x2, y2 = event.pos

            if draw_mode=="rect":
                pygame.draw.rect(canvas, color, (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), radius)
            elif draw_mode=="circle":
                pygame.draw.circle(canvas, color, last_pos, int(math.hypot(x2 - x1, y2 - y1)), radius)
            elif draw_mode=="square":
                side = max(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(canvas, color, (x1, y1, side, side), radius)
            elif draw_mode=="right_triangle":
                pygame.draw.polygon(canvas, color, [(x1, y1), (x1, y2), (x2, y2)], radius)
            elif draw_mode == "equilateral_triangle":
                height = abs(y2 - y1)
                base_x1 = x1 - height // 2
                base_x2 = x1 + height // 2
                pygame.draw.polygon(canvas, color, [(x1, y1), (base_x1, y2), (base_x2, y2)], radius)
            elif draw_mode == "rhombus":
                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2
                pygame.draw.polygon(canvas, color, [(x1, y1 - dy), (x1 - dx, y1), (x1, y1 + dy), (x1 + dx, y1)], radius)
            drawing = False


    pygame.display.update()

pygame.quit()
