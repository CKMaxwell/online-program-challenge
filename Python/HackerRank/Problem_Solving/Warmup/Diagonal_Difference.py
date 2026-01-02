# 20200706 - Diagonal Difference
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(n,arr):
    ans1 = []
    ans2 = []
    for i in range(n):
        ans1.append(arr[i][i])
        ans2.append(arr[i][n-i-1])
    #print(ans1, ans2)
    ans = abs(sum(ans1) - sum(ans2))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    #print(arr)
    #print(arr[2][2])
    result = diagonalDifference(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

