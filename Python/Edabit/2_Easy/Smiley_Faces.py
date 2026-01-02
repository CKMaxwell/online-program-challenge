# 20200910 - Smiley Faces :)
def happiness_number(s):
    count = 0
    for i in range(len(s)-1):
        if s[i:i+2] == ":)" or s[i:i+2] == "(:":
            count += 1
        elif s[i:i+2] == ":(" or s[i:i+2] == "):":
            count -= 1
    return count

print(happiness_number(":):("))