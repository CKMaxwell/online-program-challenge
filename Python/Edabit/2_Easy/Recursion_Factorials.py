# 20200825 - Recursion: Factorials
def factorial(n):
    if n == 0:
        return 1
    else:
        ans = 1
        for i in range(1, n+1):
            ans = ans * i
        return ans