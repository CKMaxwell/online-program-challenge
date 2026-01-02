# 20200915 - Recursion: Sum
def sum_numbers(n):
    ans = 0
    for i in range(1, n + 1):
        ans = ans + i
    return ans

print(sum_numbers(5))

#%%
#遞迴寫法
def sum_numbers(n):
	if not n: return 0
	return n + sum_numbers(n-1)
