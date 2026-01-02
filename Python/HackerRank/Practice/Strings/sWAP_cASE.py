# 20200622 - sWAP cASE
def swap_case(s):
    ans = ""
    for i in range(0, len(s)):
        if s[i].islower() == True:
            ans = str(ans + s[i].upper())
        elif s[i].isupper() == True:
            ans = str(ans + s[i].lower())
        else:
            ans = str(ans + s[i])
    return ans


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)