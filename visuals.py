import pygame
import time, math

# Initialize Pygame
pygame.init()

# Set window size
window_size = (1200, 800)

# Create window
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("crazy8")

# Fill background color
background_color= (0,0,0)
window.fill(background_color)

# Set font and font size
font_size = 72
font = pygame.font.Font(None, font_size)

# Define font properties
button_font_size = 24
button_font = pygame.font.Font(None, button_font_size)

# Create function to display text on window
def display_text(text, seconds, x=None, y=None):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()

    # If x and y are given, use them as the center position
    if x is not None and y is not None:
        text_rect.center = (x, y)
    else:
        text_rect.center = (window_size[0] // 2, window_size[1] // 2)

    window.blit(text_surface, text_rect)
    pygame.display.flip()
    time.sleep(seconds)
    #window.fill((0,0,0))
    # Fill the background color only around the text
    background_rect = pygame.Rect(text_rect.left, text_rect.top, text_rect.width, text_rect.height)
    pygame.draw.rect(window, background_color, background_rect)

    # Update the screen to show the cleared background
    pygame.display.update()

# Create function to display button on window
def display_button(text, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Check if mouse is over button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, active_color, (x, y, w, h))
        if click[0] == 1:
            return True  # button clicked
    else:
        pygame.draw.rect(window, inactive_color, (x, y, w, h))

    # Draw button text
    text_surface = button_font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x + w // 2, y + h // 2)
    window.blit(text_surface, text_rect)

def display_persistent_text(text, x, y):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

move = 0
display_persistent_text("This text will never disappear", window_size[0] // 2, window_size[1] - 50)
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display welcoming text and button
    if move == 0:
        display_text("Hello, Player!", 3)
        move += 1

    if display_button("Play card", 200, window_size[1] - 200, 100, 50, (255, 0, 0), (200, 0, 10)):
        display_text("Card played!", 1.5)
    
    if display_button("Draw card", 300, window_size[1] - 200, 100, 50, (255, 0, 0), (200, 0, 10)):
        display_text("Card drawn!", 1.5)
    
    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
