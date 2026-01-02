# 20200702 - Plus Minus
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(n, arr):
    pos = 0
    neg = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos = pos + 1
        if arr[i] == 0:
            zero = zero + 1
        if arr[i] < 0:
            neg = neg + 1
    print('%.6f' % float(pos / n))
    print('%.6f' % float(neg / n))
    print('%.6f' % float(zero / n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)
