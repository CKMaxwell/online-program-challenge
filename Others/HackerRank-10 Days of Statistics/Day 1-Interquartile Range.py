# Day 1: Interquartile Range
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
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
    q1_val = median(lower)
    q3_val = median(upper)
    return [q1_val, median_val, q3_val]


def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    target_list = []
    for i in range(len(values)):
        target_list += [values[i]] * freqs[i]
    qua_val = quartiles(target_list)
    print(round(float(qua_val[2] - qua_val[0]), 1))


interQuartile([1, 2, 3], [3, 2, 1])
# if __name__ == '__main__':
#     n = int(input().strip())

#     val = list(map(int, input().rstrip().split()))

#     freq = list(map(int, input().rstrip().split()))

#     interQuartile(val, freq)
