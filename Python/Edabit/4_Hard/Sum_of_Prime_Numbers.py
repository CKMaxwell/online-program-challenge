# 20200926 - Sum of Prime Numbers
def sum_primes(lst):
    if len(lst) == 0:
        return None
    else:
        ans = 0
        for i in lst:
            if i == 1:
                continue
            flag = True
            for j in range(2, i//2 + 1):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                ans += i
        return ans

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))