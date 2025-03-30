import pygame # type: ignore
import random
import time

# Initialize Pygame
pygame.init()

# Game settings
screen_width = 600
screen_height = 400
snake_size = 10
snake_speed = 15  # Initial speed
food_size = 10

# Colors (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 150, 0)
red = (255, 0, 0)

# Fonts
font_style = pygame.font.SysFont(None, 30) 

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Clock object for controlling game speed
clock = pygame.time.Clock()

def display_score(score):
    value = font_style.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def display_level(level):
    value = font_style.render("Level: " + str(level), True, white)
    screen.blit(value, [0, 30])  # Display below score

def display_timer(seconds):
    value = font_style.render("Time: " + str(seconds), True, white)
    screen.blit(value, [0, 60])  # Display below level

def draw_snake(snake_size, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_size, snake_size])

def generate_food(wall_list, snake_list):  # Add snake_list as argument
    while True:
        food_x = random.randrange(0, screen_width - food_size, 10)
        food_y = random.randrange(0, screen_height - food_size, 10)

        if (food_x, food_y) not in wall_list and (food_x, food_y) not in snake_list:
            return food_x, food_y


def game_over():
    message = font_style.render("Game Over", True, red)
    screen.blit(message, [screen_width / 3, screen_height / 3])
    pygame.display.update()
    time.sleep(2)  # Pause before loop restarts

def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1  

    food_x, food_y = generate_food([], snake_list)  # Pass snake_list here

    current_score = 0
    level = 1
    seconds = 0
    food_eaten_time = pygame.time.get_ticks()

    snake_speed = 15  # Initialize snake_speed here


    while not game_over:

        # Game close logic (when you hit the close button)
        while game_close:
            screen.fill(black)
            message = font_style.render("Quit? Y/N", True, red) 
            screen.blit(message, [screen_width / 3, screen_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
         
                        x1 = screen_width / 2
                        y1 = screen_height / 2
                        x1_change = 0
                        y1_change = 0
                        snake_list = []
                        snake_length = 1
                        food_x, food_y = generate_food([], snake_list)
                        current_score = 0
                        level = 1
                        snake_speed = 15
                        game_over = False  # Exit game over loop
                        game_close = False  # Exit game close loop
                        
                    if event.key == pygame.K_y:
                        pygame.quit()
                        quit()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Movement controls
                if event.key == pygame.K_LEFT and x1_change != snake_size:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_size:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_size:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_size:
                    y1_change = snake_size
                    x1_change = 0
        
        # Boundary collision check
        if x1 < 0 or x1 >= screen_width or y1 < 0 or y1 >= screen_height:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        screen.fill(black) 

        # Draw food
        pygame.draw.rect(screen, red, [food_x, food_y, food_size, food_size])
        
        snake_head = [x1, y1] 
        snake_list.append(snake_head)

        # Limit snake's length 
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake hits itself 
        for x in snake_list[:-1]: 
            if x == snake_head:
                game_close = True

        draw_snake(snake_size, snake_list)
        display_score(current_score)
        display_level(level)
        elapsed_time = (pygame.time.get_ticks() - food_eaten_time) // 1000
        display_timer(elapsed_time)

        pygame.display.update() 
        
        # Collision with food
        if x1 == food_x and y1 == food_y:
            food_x, food_y = generate_food([], snake_list)  # Pass snake_list here
            random_num = random.randint(1, 4)  # Randomly increase score
            current_score += random_num
            snake_length += random_num
            food_eaten_time = pygame.time.get_ticks()
            

            # Level Progression
            if current_score % 5 == 0:
                level += 1
                snake_speed += 5  # Increase speed 
        elif (x1 != food_x and y1 != food_y) and elapsed_time == 5:
            food_x, food_y = generate_food([], snake_list) 


        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
game_loop() 