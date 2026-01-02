# 20200904 - A Long Long Time
# 簡化寫法很多 可多留意


def longest_time(h, m, s):
    h2 = h * 3600
    m2 = m * 60
    ans = max(h2, m2, s)
    if ans == h2:
        return h
    elif ans == m2:
        return m
    elif ans == s:
        return s