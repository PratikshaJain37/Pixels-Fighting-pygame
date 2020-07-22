# Helpers.py #

import random
import numpy as np
import time

current_status = np.array([[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1]])

def UpdateArray(current_status):
    updated_status = np.zeros((8,8), dtype=int)
    for i in range(0,8):
        for j in range(0,8):
            updated_status[i][j] = GetStatus(GetAliveRatio(i,j,current_status))
    
    return updated_status

def GetStatus(alive_ratio):
    random_number = random.random()
    if random_number <= alive_ratio:
        return 1
    else:
        return 0

def GetAliveRatio(x,y,current_status_array):
    around_alive = 0
    around_total = 0
    for i in range(x-1,x+2):
            if i in range(0,8) and i != x:
                around_total += 1
                if current_status_array[i][y] == 1:
                    around_alive += 1

    for j in range(y-1,y+2):
        if j in range(0,8) and j != y:
            around_total += 1
            if current_status_array[x][j] == 1:
                around_alive += 1


    return around_alive/around_total


print(current_status)
for i in range(1000):
    current_status = UpdateArray(current_status)
  
print (current_status)
