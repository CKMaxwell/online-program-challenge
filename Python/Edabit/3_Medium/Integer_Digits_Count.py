# 20201029 - Integer Digits Count
def count(n):
    ans = len(str(abs(n)))
    return ans

print(count(-314890))