# Helpers.py - Pixels Fighting #

# ---------------------#

# Imports #
import random
import numpy as np

# ---------------------#

# For updating the array
def UpdateArray(current_status, INT):
    updated_status = np.zeros((INT,INT), dtype=int)
    for i in range(0,INT):
        for j in range(0,INT):
            status, ratio = GetRatio(i,j,current_status,INT)
            updated_status[i][j] = GetStatus(status, ratio)
    
    return updated_status

# For calculating status of individual box
def GetStatus(status,ratio):
    random_number = random.random()
    if random_number >= ratio:
        flip = False
    else:
        flip = True
    if flip == True:
        return status
    else:
        return 1 - status

# For calculating alive ratio of individual box
def GetRatio(x,y,current_status_array,INT):
    around_alive = 0
    around_total = 0
    for i in range(x-1,x+2):
        if i in range(0,INT) and i != x:
            around_total += 1
            if current_status_array[i][y] == 1:
                around_alive += 1

    for j in range(y-1,y+2):
        if j in range(0,INT) and j != y:
            around_total += 1
            if current_status_array[x][j] == 1:
                around_alive += 1

    if current_status_array[x][y] == 0:
        return 0, 1 - around_alive/around_total
    else:
        return 1, around_alive/around_total

# ---------------------#
