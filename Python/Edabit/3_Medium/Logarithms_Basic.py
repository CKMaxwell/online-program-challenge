# 20201016 - Logarithms - Basic
def logarithm(base, num):
    if base <= 1:
        return "Invalid"
    elif num < base:
        return "Invalid"
    else:
        i = 1
        while base ** i != num:
            i += 1
        return i

print(logarithm(5, 25))