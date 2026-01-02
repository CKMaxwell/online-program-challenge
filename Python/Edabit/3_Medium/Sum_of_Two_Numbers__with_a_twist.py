# 20201112 - Sum of Two Numbers (with a twist!)
# 別人的答案
# `str(int(a) + int(b))` ARE good enough!
# But imagining numbers are really HUGE:
from itertools import zip_longest as zipl
def sum2(a, b):
    res, c = [], 0
    for d1, d2 in zipl(reversed(a), reversed(b), fillvalue=0):
        s = int(d1) + int(d2) + c
        res.append(s % 10)
        c = s // 10
    if c: res.append(c)
    return ''.join(map(str, reversed(res)))