import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image for the animation
image = pygame.image.load("2_of_clubs.png")
image = pygame.transform.scale(image, (100, 140))

# Set the starting position of the image
image_width, image_height = image.get_rect().size
image_x = (screen_width - image_width) // 2
image_y = screen_height

# Set the animation speed and direction
speed = 1/4
direction = -1  # negative y-direction

# Set up the trail surface
trail_surface = pygame.Surface((image_width, image_height), pygame.SRCALPHA)
trail_color = (128, 128, 128, 128)  # grey trail color
trail_surface.fill(trail_color)
trail_length = 10
trail_positions = []

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the image
    image_y += speed * direction

    # Reset the position of the image once it goes off the screen
    if image_y < -image_height:
        running = False

    # Update the trail positions
    trail_positions.append((image_x, image_y))
    if len(trail_positions) > trail_length:
        trail_positions.pop(0)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the trail
    for i, position in enumerate(trail_positions):
        alpha = int(128 * (i+1) / len(trail_positions))
        trail_surface.set_alpha(alpha)
        screen.blit(trail_surface, position)

    # Draw the image
    screen.blit(image, (image_x, image_y))

    # Update the screen
    pygame.display.update()

# Clean up
pygame.quit()
