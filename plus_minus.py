'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
  '''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    
    print(f'{pos/len(arr)}\n{neg/len(arr)}\n{zero/len(arr)}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
