# 20201121 - Histogram Function
def histogram(lst, char):
    ans = ""
    for i in lst:
        ans += i * char + "\n"
    return ans[:-1]

print(histogram([6, 2, 15, 3], "="))