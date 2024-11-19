# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Simple Picture')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen.fill(WHITE)

pygame.draw.rect(screen, RED, (50, 50, 300, 200))

pygame.draw.circle(screen, BLUE, (200, 300), 50)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
exit()