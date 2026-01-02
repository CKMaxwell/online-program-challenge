# 20200930 - Alphabet Soup
def alphabet_soup(txt):
    ans = list(txt)
    ans.sort()
    ans = "".join(ans)
    return ans

print(alphabet_soup("hello"))