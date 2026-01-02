# 20200704 - Compare the Triplets
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    val_a = 0
    val_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            val_a = val_a + 1
        if a[i] < b[i]:
            val_b = val_b + 1
    return [val_a, val_b]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
