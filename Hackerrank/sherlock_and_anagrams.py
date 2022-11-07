#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    sub_string = 0
    #iterates through the string to check whether there are any character substring
    for i in range(1, len(s)):
        ana_count = {} #to count the anagram chars
        for j in range(len(s)-i+1): #iterate through s backwards to check if there is anything we can cound as anagrams
            sub = ''.join(sorted(s[j:j+i]))
            # compare it wiht the anacount dictionary
            if sub not in ana_count:
                ana_count[sub] = 1 # assigns a place for this substing in the dictionary
            else:
                ana_count[sub] += 1
            sub_string += ana_count[sub] - 1
    return sub_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
