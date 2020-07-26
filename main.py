# Main.py - Pixels Fighting #
# Author: Pratiksha Jain #

# ---------------------#

# Imports #
import pygame
from pygame.locals import *
from helpers import *
import random
import numpy as np
import time

# ---------------------#

# Initialize Pygame
pygame.init()

# Initialize screen, status and clock
screen = pygame.display.set_mode((700,700))
running = True
clock = pygame.time.Clock()

# Defining Colors 
COLOR_ALIVE = (0,128,255)
COLOR_DEAD = (0,200,255)

# Initialize number of rows/columns
INT = 100
INT_SQ = INT*INT

# Initialize size of arrays
SIZE = 5

# Initialize Status Array - Making an array with half dead and half alive
zero = np.zeros((INT,INT//2), dtype=int)
one = np.ones((INT,INT//2), dtype=int)
current_status_array = np.concatenate((zero,one), axis=1)

# ---------------------#

# Defining Box Class
class Box():
    
    # Status can be dead (0) or alive(1); 
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.surf = pygame.Surface((SIZE,SIZE))
        self.rect = (30 + SIZE*self.y, 30 + SIZE*self.x)
    
    # Function to fill surface with color
    def assign_color(self):
        if self.alive == 0:
            self.surf.fill(COLOR_DEAD)
        else:
            self.surf.fill(COLOR_ALIVE)
        screen.blit(self.surf,self.rect)

    # Function to update surface; as per current_status_array
    def update(self):
        self.alive = current_status_array[self.x][self.y]
        self.assign_color()
     

# ---------------------#

# Creating 'INT_SQ' instances of box class, and appending them to a list for accessibility

boxes = []

for i in range(INT_SQ):

    # x,y will be filled sequentially 
    x = i//INT
    y = i%INT

    # Alive status depening on current array
    boxes.append(Box(x,y,current_status_array[x][y]))

# ---------------------#

# Main python loop

while running:
    
    # Main python quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # For updating array and boxes status
    current_status_array = UpdateArray(current_status_array, INT)
    for box in boxes:
        box.update()
        
    
    # Refresh screen
    pygame.display.update()

    # A more optimal version of the clock.tick() function, determines fps of display basically
    time.sleep(0.1)

# ---------------------#

