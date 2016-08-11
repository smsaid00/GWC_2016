"""
 Pygame base template for opening a window
 Pygame documentation: https://www.pygame.org/docs/genindex.html
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Bouncing Ball")




# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
x = 350
y = 250
x_speed = 10
y_speed = 20

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(RED)
    # pygame.draw.circle(screen, color, (x,y), radius , thickness)

    pygame.draw.circle(screen, GREEN, (x,y), 30 , 0)
    # if (y==0 or y==500) and (x==0 or x==700):
    if x>=700:
        x_speed = x_speed * -1
    if y>=500:
        y_speed = y_speed * -1
    if x<=0:
        x_speed = x_speed * -1
    if y<=0:
        y_speed = y_speed * -1
    x += x_speed
    y += y_speed


    pygame.display.update()



    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
