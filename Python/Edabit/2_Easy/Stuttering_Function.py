# 20200817 - Stuttering Function
def stutter(word):
    stu = word[0:2]
    ans = stu + "... " + stu + "... " + word + "?"
    return ans

print(stutter("apple"))
