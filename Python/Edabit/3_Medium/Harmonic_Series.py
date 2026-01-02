# 20200902 - Harmonic Series
def harmonic(n):
    ans = 0
    for i in range(1, n+1):
        ans += (1 / i)
    return round(ans, 3)

print(harmonic(3))