#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    # initialize the array with zeros
    arr = [0] * (n + 2) # n+2 to avoid index bound error

    # perform the query operations
    for a,b,k in queries:
        arr[a] += k #updates the starting index
        arr[b+1] -= k
        print(arr)
    # find max element from the array
    max_num = 0
    temp = 0 # just to check whether is grreater than the max_num
    for value in arr:
        temp += value
        max_num = max(max_num, temp)
    return max_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
