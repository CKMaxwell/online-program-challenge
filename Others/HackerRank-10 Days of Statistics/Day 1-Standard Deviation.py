# Day 1: Standard Deviation
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = 0
    for i in arr:
        mean += i
    mean /= len(arr)
    std = 0
    for j in arr:
        std += (j - mean) ** 2
    std = round(math.sqrt(std / len(arr)), 1)
    print(std)


stdDev([2, 5, 7, 2, 4])
# if __name__ == '__main__':
#     n = int(input().strip())

#     vals = list(map(int, input().rstrip().split()))

#     stdDev(vals)
