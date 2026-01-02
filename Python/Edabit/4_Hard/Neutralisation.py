# 20201003 - Neutralisation
def neutralise(s1, s2):
    ans = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            ans += s1[i]
        else:
            ans += "0"
    return ans

print(neutralise("-+-+-+", "-+-+-+"))
print(neutralise("--++--", "++--++"))