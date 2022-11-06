#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    # initialize the valley count and sea level count to 0
    valley_c = 0
    sea_level = 0

    # create a dictionatry the handle the steps and convert it to an int
    hiker_step = {
        "U": 1,
        "D": -1,
    }
    # iterate the string steps
    for steps in path:
        sea_level += hiker_step[steps] # add the steps to the sea level
        if sea_level == 0 and steps == "U":
            valley_c += 1

    return valley_c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
