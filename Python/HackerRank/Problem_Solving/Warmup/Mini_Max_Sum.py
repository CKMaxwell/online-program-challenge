# 20200703 - Mini-Max Sum
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max_v = arr.copy()
    min_v = arr.copy()
    max_v.remove(min(arr))
    min_v.remove(max(arr))
    print(sum(min_v), sum(max_v))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
