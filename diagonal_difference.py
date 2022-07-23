'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal => 1 + 5 + 9 = 15. The right to left diagonal => 3 + 5 + 9 = 17. 
Their absolute difference is |15 - 17| = 2.

Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .
'''

#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    diagonal1, diagonal2 = 0, 0
    
    for num in range(0, len(arr)):
        diagonal1 += arr[num][num]
        diagonal2 += arr[num][len(arr)-num-1]
     
    return abs(diagonal1 - diagonal2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
