# 20201004 - Oddish vs. Evenish
def oddish_or_evenish(num):
    word = str(num)
    ans = 0
    for i in range(len(word)):
        ans += int(word[i])
    if ans % 2 == 0:
        return "Evenish"
    elif ans % 2 == 1:
        return "Oddish"

print(oddish_or_evenish(43))