# Helpers.py #

import random
import numpy as np

current_status = np.array([[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1]])


def GetStatus(alive_ratio):
    random_number = random.random()
    if random_number >= alive_ratio:
        return 1
    else:
        return 0

def UpdateArray(current_status):
    # iterate over all 64 elements, and then display new array
    
    for i in range(0,8):
        for j in range(0,8):
            current_status[i][j] = GetStatus(GetAliveRatio(i,j,current_status))
    
    return current_status

def GetAliveRatio(x,y,current_status_array):
    around_alive = 0
    around_total = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i in range(0,8) and j in range(0,8) and i != x and j != y:
                around_total += 1
                if current_status_array[i][j] == 1:
                    around_alive += 1
            else:
                pass
   
    return around_alive/around_total

