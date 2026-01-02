# 20201019 - Harshad Number
def is_harshad(n):
    word = str(n)
    check = 0
    for i in range(len(word)):
        check += int(word[i])
    return n % check == 0

print(is_harshad(171))