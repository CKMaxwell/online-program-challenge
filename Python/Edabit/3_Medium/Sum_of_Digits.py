# 20200829 - Are the Sum of Digits in the Numbers Equal?
def is_equal(lst):
    a = str(lst[0])
    b = str(lst[1])
    a_val = 0
    b_val = 0
    for i in range(len(a)):
        a_val = int(a[i]) + a_val
    for j in range(len(b)):
        b_val += int(b[j])
    if a_val == b_val:
        return True
    else:
        return False

is_equal([105, 42])