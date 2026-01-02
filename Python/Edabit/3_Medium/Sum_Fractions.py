# 20201018 - Sum Fractions
def sum_fractions(lst):
    ans = 0
    for i in range(len(lst)):
        ans += lst[i][0] / lst[i][1]
    return round(ans)

print(sum_fractions([[36, 4], [22, 60]]))