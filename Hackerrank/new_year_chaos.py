#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribe = 0
    for i in range(len(q)-1, 0, -1): # -1 reducces the quantity of the iteration
        # to sort the array
        if q[i] != i + 1:
            if q[i - 1] == i + 1: # check if the perosn ahead is not the person above
                bribe += 1
                # swap
                q[i - 1], q[i] = q[i],q[i - 1]
            elif q[i - 2] == i + 1: #condition of the second bribe
                bribe += 2
                q[i - 2], q[i - 1], q[i] = q[i -1], q[i], q[i-2] #swap
            else:
                print("Too chaotic")
                return void
    print(bribe)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
