# 20201124 - Sum of Odd and Even Numbers
def sum_odd_and_even(lst):
    ans1 = 0
    ans2 = 0
    for i in lst:
        if i % 2 == 0:
            ans1 += i
        else:
            ans2 += i
    return [ans1, ans2]

print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))