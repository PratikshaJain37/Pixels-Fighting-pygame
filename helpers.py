# Helpers.py - Pixels Fighting #
# Author: Pratiksha Jain #

# ---------------------#

# Imports #
import random
import numpy as np

# ---------------------#

# For updating the array
def UpdateArray(current_status, INT):

    # Generating new updated array (empty)
    updated_status = np.zeros((INT,INT), dtype=int)

    # Iterating over all in current_status
    for i in range(0,INT):
        for j in range(0,INT):

            # Getting the ratio of surrouding boxes which are dead
            status, ratio = GetRatio(i,j,current_status,INT)
            updated_status[i][j] = GetStatus(status, ratio)
    
    return updated_status

# ----------#

# For calculating status of individual box - based on the rules mentioned.
def GetStatus(status,ratio):

    # Generating a random number between (0,1)
    random_number = random.random()
    
    # Test for the random number - decides whether it's status will flip or not
    flip = False
    if random_number <= ratio:
        flip = True
    
    # Returning the outcome after the flip
    if flip == True:
        return status
    else:
        return 1 - status

# ----------#

# For calculating alive ratio of individual box
def GetRatio(x,y,current_status,INT):
    
    # Initialising counters
    around_alive = 0
    around_total = 0
    
    # Iterating through neighbors
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):

            # Condition to make sure the neighbor exists
            if i in range(0, INT) and j in range(0,INT):
                
                # To make sure the number is not the box itself
                if i == x and j == y:
                    pass
                else:
                    around_total += 1

                    # Identifying alive neighbors
                    if current_status[i][j] == 1:
                        around_alive += 1

    # Depending on the status itself, the ratio is decided
    if current_status[x][y] == 0:
        return 0, 1 - around_alive/around_total
    else:
        return 1, around_alive/around_total

# ----------#

# Function to check if Alive is Winning - to get a fraction
def IsAliveWinning(current_status_array, INT_SQ):
    
    # Counts number of 1's
    alive = np.count_nonzero(current_status_array == 1)
    
    return alive/INT_SQ
    
# ---------------------#

