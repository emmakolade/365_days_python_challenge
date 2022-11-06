#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_sum = -70 # the value has to be more than the min value of the calulated sum in the example
    # logic
    for i in range(4): # cos it is a 6 X 6 matrix, i have to iterate through 4 values both in rows and colomns.
        for j in range(4):
            # hour glass value
            #top value
            top = sum(arr[i][j:j+3]) # for the hour glass, i have to consider the first three elements.
            #middle value
            mid = arr[i+1][j+1]
            #bottom value
            bot = sum(arr[i+2][j:j+3])

            #calculate the total sum
            hourglass = top + mid + bot

            #store the total sum to the max_sum variable
            max_sum = max(hourglass, max_sum)
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
