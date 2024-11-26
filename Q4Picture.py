# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Pizza Design')

LIGHT_BLUE = (173, 216, 230)
PIZZA_YELLOW = (255, 223, 132)
CRUST_BROWN = (205, 133, 63)
RED = (255, 0, 0) 
BOX_GRAY = (192, 192, 192)

screen.fill(LIGHT_BLUE)

pygame.draw.rect(screen, BOX_GRAY, (50, 50, 300, 300)) 

pygame.draw.circle(screen, CRUST_BROWN, (200, 200), 130) 
pygame.draw.circle(screen, PIZZA_YELLOW, (200, 200), 120)  

toppings = [(160, 160), (240, 160), (200, 240), (150, 220), (250, 220)]
for topping in toppings:
    pygame.draw.circle(screen, RED, topping, 10)

pygame.draw.polygon(screen, PIZZA_YELLOW, [(200, 200), (130, 350), (270, 350)]) 
pygame.draw.lines(screen, CRUST_BROWN, True, [(200, 200), (130, 350), (270, 350)], 10) 

pygame.draw.circle(screen, RED, (200, 280), 15)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
exit()