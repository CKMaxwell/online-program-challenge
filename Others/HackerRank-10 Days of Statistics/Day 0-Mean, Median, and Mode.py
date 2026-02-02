# Day 0: Mean, Median, and Mode
'''
Task
Given an array, , of  integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.
Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of  decimal place (i.e., ,  format).

'''
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
arr = input()
arr = [int(v) for v in arr.split(" ")]

mean = sum(arr) / n

arr.sort()
if n % 2 == 0:
    median = (arr[n//2 - 1] + arr[n // 2]) / 2
else:
    median = arr[n//2 - 1]
    
counter = Counter(arr)
mode = counter.most_common(1)[0][0]

print(mean)
print(median)
print(mode)