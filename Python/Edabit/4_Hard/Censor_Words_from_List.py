# 20201110 - Censor Words from List
def censor_string(txt, lst, char):
    a = txt.split( )
    for i in range(len(a)):
        if a[i] in lst:
            a[i] = char * len(a[i])
    return " ".join(a)

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))