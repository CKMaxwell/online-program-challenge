# 20200901 - Sum of v0w3ls
def sum_of_vowels(sentence):
    tran = {"a": 4, "e": 3, "i": 1, "o": 0, "u": 0}
    sent = sentence.lower()
    val = 0
    print()
    for i in sent:
        if i in tran.keys():
            val += tran[i]
    return val


print(sum_of_vowels("Let\'s test this function."))
