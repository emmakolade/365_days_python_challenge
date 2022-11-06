#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    n_jump = 0
    current_cloud = 0
    while current_cloud < n-1: # to reach the last current_cloud
        if current_cloud+2 < n and c[current_cloud+2] == 0: #so that the cloud is cumulus
            n_jump += 1
            current_cloud = 2
        elif current_cloud+2 < n and c[current_cloud+1] == 0:
            n_jump += 1
            current_cloud += 1

    return n_jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
