# Day 1: Quartiles
# https://www.hackerrank.com/challenges/s10-quartiles/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quartiles(arr):
    arr.sort()
    n = len(arr)
    q2_index = n // 2

    def median(new_arr):
        n = len(new_arr)
        if n % 2 == 1:
            median = new_arr[n // 2]
        else:
            median = (new_arr[n // 2 - 1] + new_arr[n // 2]) / 2
        return int(median)

    median_val = median(arr)
    if n % 2 == 1:
        lower = arr[:q2_index]
        upper = arr[q2_index + 1 :]
    else:
        lower = arr[:q2_index]
        upper = arr[q2_index:]
    print(lower, upper)
    q1_val = median(lower)
    q3_val = median(upper)
    return [q1_val, median_val, q3_val]


print(quartiles([9, 5, 7, 1, 3]))
print(quartiles([5, 7, 1, 3]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     data = list(map(int, input().rstrip().split()))

#     res = quartiles(data)

#     fptr.write('\n'.join(map(str, res)))
#     fptr.write('\n')

#     fptr.close()
