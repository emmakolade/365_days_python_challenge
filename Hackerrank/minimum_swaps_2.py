#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    # we need to iterate through every index  to check whether it is part of a complete closed loop
    visited = [False] * len(arr) #sets a flag for every index
    for i in range(len(arr)):
        if visited[i] == False:
            assign = i #assigning and storing the index
            b = arr[i] - 1 # stores the index of the next element
            l = 1 # stores the lenght and count the lenght of the loop
            visited[i] = True
            while b != i: # if the number is at the right postion, then no swap should run
                visited[b] = True:
                assign = b
                b = arr[b] - 1
                l += 1
            swap += l - 1
    return swap



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
