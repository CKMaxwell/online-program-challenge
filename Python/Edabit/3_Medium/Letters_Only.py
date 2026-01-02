# 20201007 - Letters Only
def letters_only(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            return False
    if len(s) == 0:
        return False
    elif s.lower() == s:
        return True
    else:
        return False

print(letters_only("PYTHON"))