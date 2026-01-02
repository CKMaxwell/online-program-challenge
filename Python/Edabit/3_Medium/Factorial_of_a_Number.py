# 20200818 - Factorial of a Number
def fact(n):
    if n == 0:
        return 1
    else:
        ans = 1
        for i in range(1,n+1):
            ans = ans * i
        return ans

print(fact(6))