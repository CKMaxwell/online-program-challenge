# 20200909 - Words With Duplicate Letters
def no_duplicate_letters(phrase):
    phrase = phrase.lower()
    word = map(list, phrase.split( ))
    for i in word:
        word_set = set(i)
        word_list = list(i)
        if len(word_set) == len(word_list):
            continue
        else:
            return False
            break
    return True

print(no_duplicate_letters("Look before you leap."))
