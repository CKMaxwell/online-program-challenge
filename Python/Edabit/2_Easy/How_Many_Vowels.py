# 20200909 - How Many Vowels?
def count_vowels(txt):
    vow = ["a", "e", "i", "o", "u"]
    count = 0
    for i in txt:
        if i in vow:
            count += 1
    return count