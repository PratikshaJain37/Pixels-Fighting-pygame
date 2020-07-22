# Main.py #
# Author: Pratiksha Jain #

# Imports #
import pygame
from helpers import *
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Initialize screen, status and clock
screen = pygame.display.set_mode((750,750))
running = True
clock = pygame.time.Clock()


# Defining Colors 
WHITE = (0,128,255)
BLUE = (0,200,255)

# Starting status of array
current_status = np.array([[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1]])

# This will be a list that will contain all the boxes (sprites) used.
all_sprites_list = pygame.sprite.Group()


class Box(pygame.sprite.Sprite):
    '''
    This class represents the boxes. Derives from Sprite class in Pygame.
    '''
    def __init__(self, x, y):
        
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface((40,40))
        self.rect = self.image.get_rect()
        if current_status[x][y] == 0:
            self.image.fill(BLUE)
        else:
            self.image.fill(WHITE)

    def update(self):
        updated_status = UpdateArray(current_status)
        if current_status[x][y] == 0:
            self.image.fill(BLUE)
        else:
            self.image.fill(WHITE)



for i in range(64):

    # This represents the x,y position in array
    x = i//8
    y = i%8

    # This represents a box
    box = Box(x,y)
    
    # Set location for the block
    box.rect.x = 30 + 45*x
    box.rect.y = 30 + 45*y
   
    # Add the block to the list of objects
    all_sprites_list.add(box)


while running:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites - Game logic
    all_sprites_list.update()

    # Drawing on screen
    all_sprites_list.draw(screen)

    # Refresh screen
    pygame.display.flip()

    # Number of frames per second
    clock.tick(60)