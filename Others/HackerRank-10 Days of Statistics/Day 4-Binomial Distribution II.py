# Day 4: Binomial Distribution II
"""
Objective
In this challenge, we go further with binomial distributions. We recommend reviewing the previous challenge's Tutorial before attempting this problem.

Task
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects?
At least 2 rejects?
"""
# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem?isFullScreen=true

from math import comb

fail_ratio, amount = 12, 10
fail_perc = fail_ratio / 100
# 計算P(X<=2) = P(X=0) + P(X=1) + P(X=2)
ans = 0
for x in range(0, 3):
    ans += comb(amount, x) * (fail_perc**x) * ((1 - fail_perc) ** (amount - x))
print(round(ans, 3))

# 計算P(X>=2) = P(X=2) + ... + P(X=10)
ans = 0
for x in range(2, 11):
    ans += comb(amount, x) * (fail_perc**x) * ((1 - fail_perc) ** (amount - x))
print(round(ans, 3))
