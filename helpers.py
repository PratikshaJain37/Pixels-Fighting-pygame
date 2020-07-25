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
            updated_status[i][j] = GetStatus(GetAliveRatio(i,j,current_status,INT))
    
    return updated_status

# For calculating status of individual box
def GetStatus(alive_ratio):
    random_number = random.random()
    if random_number <= alive_ratio:
        return 1
    else:
        return 0

# For calculating alive ratio of individual box
def GetAliveRatio(x,y,current_status_array,INT):
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


    return around_alive/around_total

# ---------------------#
