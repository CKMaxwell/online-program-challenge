# Day 0: Weighted Mean
'''
Task
Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e.,  format).
'''
# https://www.hackerrank.com/challenges/s10-weighted-mean/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    sum_val = 0
    total_weight = 0
    for i in range(len(X)):
        sum_val += X[i] * W[i]
        total_weight += W[i]
    result = round(sum_val / total_weight, 1)
    print(result)
        

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
