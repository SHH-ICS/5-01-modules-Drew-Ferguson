# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Simple Picture')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fill the screen with white color
screen.fill(WHITE)

# Draw a red rectangle (x, y, width, height)
pygame.draw.rect(screen, RED, (50, 50, 300, 200))

# Draw a blue circle (center_x, center_y, radius)
pygame.draw.circle(screen, BLUE, (200, 300), 50)

# Update the display
pygame.display.flip()

# Keep the window open until the user closes it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
exit()