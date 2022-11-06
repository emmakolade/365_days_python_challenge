#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    total_char = 0
    #iterate through the characters from the string
    for char in s:
        if char == 'a': #calculates the num of a in the string
            total_char += 1
    # calculate the number of a's when n is given a value
    total_char = n//len(s) * total_char # to find the total number of a in the repeated string

    #to find the total number of a in the remaining string( traverse the string)
    for char_rem in s[:n % len(s)]:
        if char_rem == 'a':
            total_char += 1

    return total_char


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
