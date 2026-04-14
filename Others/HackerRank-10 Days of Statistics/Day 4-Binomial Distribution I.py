# Day 4: Binomial Distribution I
"""
Objective
In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

Task
The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

Input Format

A single line containing the following values: 1.09 1
If you do not wish to read this information from stdin, you can hard-code it into your program.

Output Format
Print a single line denoting the answer, rounded to a scale of  decimal places (i.e.,  format).
"""
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem?isFullScreen=true

from math import comb

boy_ratio, girl_ratio = 1.09, 1
pb = boy_ratio / (boy_ratio + girl_ratio)
pf = 1 - pb
# 計算P(X>=3) = P(X=3) + P(X=4) + P(X=5) + P(X=6)
ans = 0
for x in range(3, 7):
    ans += comb(6, x) * (pb**x) * (pf ** (6 - x))
print(round(ans, 3))
