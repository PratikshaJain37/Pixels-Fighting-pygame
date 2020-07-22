# Main.py #
# Author: Pratiksha Jain #

# Imports #
import pygame
from pygame.locals import *
from helpers import *
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Initialize screen, status and clock
screen = pygame.display.set_mode((500,500))
running = True
clock = pygame.time.Clock()


# Defining Colors 
DARK_BLUE = (0,128,255)
BLUE = (0,200,255)

# Starting status of array
current_status_array = np.array([[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1]])


class Box():
    
    def __init__(self, x,y, status):
        self.status = status
        self.x = x
        self.y = y
    
    def draw(self):
        if self.status == 0:
            pygame.draw.rect(screen, DARK_BLUE, Rect(30 + 45*self.x, 30 + 45*self.y, 40,40))
        else:
            pygame.draw.rect(screen, BLUE, Rect(30 + 45*self.x, 30 + 45*self.y, 40,40))
    
    def update(self):
        self.status = current_status_array[self.x][self.y]

        if self.status == 0:
            pygame.draw.rect(screen, DARK_BLUE, Rect(30 + 45*self.x, 30 + 45*self.y, 40,40))
        else:
            pygame.draw.rect(screen, BLUE, Rect(30 + 45*self.x, 30 + 45*self.y, 40,40))
    
boxes = []

for i in range(64):

    x = i//8
    y = i%8

    if y > 3:
        boxes.append(Box(x,y,1))
    else:
        boxes.append(Box(x,y,0))



while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.lock()

    current_status_array = UpdateArray(current_status_array)
    for box in boxes:
        box.update()
        
    
    # Refresh screen
    screen.unlock()
    pygame.display.update()
    clock.tick(10)
    

