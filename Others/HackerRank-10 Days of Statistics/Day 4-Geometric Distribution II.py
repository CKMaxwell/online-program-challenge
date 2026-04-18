# Day 4: Geometric Distribution II
"""
Objective
In this challenge, we go further with geometric distributions. We recommend reviewing the Geometric Distribution tutorial before attempting this challenge.

Task
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the first 5 inspections?
"""
# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem?isFullScreen=true

defective_ratio = 1 / 3
amount = 5
ans = 0
for i in range(1, amount + 1):
    ans += (1 - defective_ratio) ** (i - 1) * defective_ratio
print(round(ans, 3))