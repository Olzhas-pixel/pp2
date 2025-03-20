import pygame

# Initialize pygame
pygame.init()

# Screen settings
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dop")

# Ball settings
radius = 25
ball_x, ball_y = width // 2, height // 2  # Start in center
BALL_COLOR = (255, 0, 0)
BG_COLOR = (255, 255, 255)


# Game loop
running = True
while running:
    screen.fill(BG_COLOR)  # Clear screen

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and ball_x - radius - 20 >= 0:
                ball_x -= 20
            if event.key == pygame.K_RIGHT and ball_x + radius + 20 <= width:
                ball_x += 20
            if event.key == pygame.K_UP and ball_y - radius - 20 >= 0:
                ball_y -= 20
            if event.key == pygame.K_DOWN and ball_y + radius + 20 <= height:
                ball_y += 20

    # Draw ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), radius)

    pygame.display.flip()

# Quit pygame
pygame.quit()
