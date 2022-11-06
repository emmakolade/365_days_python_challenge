#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # we have to count through the number of pairs
    #initialize the count to 0
    count_sock = 0
    # create a dictionary to calc the number of socks for each color
    socksPile = {}

    #iterate through the array
    for color in ar:
        socksPile[color] = socksPile.get(color, 0) + 1  #if color already exsits in the dictionary  it  will return a value otherwise 0
    # iterate the keys of the dictionbary
    for key in socksPile.keys():
        count_sock += socksPile[key]//2 # gives total number of socks for a particular color

    return count_sock