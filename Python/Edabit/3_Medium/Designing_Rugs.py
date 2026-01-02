# 20201115 - Designing Rugs
def make_rug(m, n, s="#"):
    sol = []
    for i in range(m):
        ans = s * n
        sol.append(ans)
    return sol

print(make_rug(3, 5))
print(make_rug(3, 5, '$'))
print(make_rug(2, 2, 'A'))