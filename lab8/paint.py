import pygame  # type: ignore

pygame.init()

# Window setup
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint | r:red, g:green, b:blue, w:black, e:eraser, c:clear")

# Color definitions
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

# Initial states
is_running = True
is_drawing = False
previous_position = None
current_draw_mode = "line"
current_color = COLOR_BLACK
brush_radius = 5

# Create drawing canvas (surface)
drawing_canvas = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
drawing_canvas.fill(COLOR_WHITE)

# Main loop
while is_running:
    window.fill(COLOR_WHITE)
    window.blit(drawing_canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            # Color selection
            if event.key == pygame.K_r:
                current_color = COLOR_RED
                current_draw_mode = "line"
            elif event.key == pygame.K_g:
                current_color = COLOR_GREEN
                current_draw_mode = "line"
            elif event.key == pygame.K_b:
                current_color = COLOR_BLUE
                current_draw_mode = "line"
            elif event.key == pygame.K_w:
                current_color = COLOR_BLACK
                current_draw_mode = "line"
            elif event.key == pygame.K_e:
                current_color = COLOR_WHITE
                current_draw_mode = "line"  # Simulate eraser by drawing white

            # Clear the canvas
            elif event.key == pygame.K_c:
                drawing_canvas.fill(COLOR_WHITE)

            # Change brush size
            elif event.key == pygame.K_UP:
                brush_radius = min(200, brush_radius + 3)
            elif event.key == pygame.K_DOWN:
                brush_radius = max(1, brush_radius - 3)

        # Mouse button pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            previous_position = event.pos
            if event.button == 1:  # Left mouse button — draw line
                current_draw_mode = "line"
                is_drawing = True
            elif event.button == 3:  # Right mouse button — draw rectangle
                current_draw_mode = "rect"
            elif event.button == 2:  # Middle mouse button — draw circle
                current_draw_mode = "circle"

        # Drawing lines while dragging
        elif event.type == pygame.MOUSEMOTION and is_drawing and current_draw_mode == "line":
            pygame.draw.line(drawing_canvas, current_color, previous_position, event.pos, brush_radius)
            previous_position = event.pos

        # Mouse button released — draw rect or circle
        elif event.type == pygame.MOUSEBUTTONUP:
            if current_draw_mode == "rect":
                rect_x = min(previous_position[0], event.pos[0])
                rect_y = min(previous_position[1], event.pos[1])
                rect_width = abs(previous_position[0] - event.pos[0])
                rect_height = abs(previous_position[1] - event.pos[1])
                pygame.draw.rect(drawing_canvas, current_color, (rect_x, rect_y, rect_width, rect_height), brush_radius)
            elif current_draw_mode == "circle":
                center_x, center_y = previous_position
                end_x, end_y = event.pos
                radius_circle = int(((end_x - center_x) ** 2 + (end_y - center_y) ** 2) ** 0.5)
                pygame.draw.circle(drawing_canvas, current_color, previous_position, radius_circle, brush_radius)
            is_drawing = False

    pygame.display.update()

pygame.quit()
