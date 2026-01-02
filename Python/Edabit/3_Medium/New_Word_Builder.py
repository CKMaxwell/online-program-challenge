# 20200829 - New Word Builder
def word_builder(ltr, pos):
    ans = ""
    for i in pos:
        ans += ltr[i]
    return ans
