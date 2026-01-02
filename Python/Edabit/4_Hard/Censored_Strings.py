# 20201027 - C*ns*r*d Str*ngs
def uncensor(txt, vowels):
    flag = 0
    ans = ""
    for i in range(len(txt)):
        if txt[i] == "*":
            ans += vowels[flag]
            flag += 1
        else:
            ans += txt[i]
    return ans

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))