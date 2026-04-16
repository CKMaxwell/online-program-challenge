# Day 4: Geometric Distribution I
"""
Objective
In this challenge, we learn about geometric distributions. Check out the Tutorial tab for learning materials!

Task
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect occurs the 5th item produced?

Input Format

The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of being the first defect for:

1 3
5
"""
# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem?isFullScreen=true
defective_ratio = 1 / 3
amount = 5
ans = (1 - defective_ratio) ** (amount - 1) * defective_ratio
print(round(ans, 3))
