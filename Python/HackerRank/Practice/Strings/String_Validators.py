# 20200626 - String Validators
s = input()
a = False
b = False
c = False
d = False
e = False
for i in range(0,len(s)):
    if s[i].isalnum() == True:
        a = True
    if s[i].isalpha() == True:
        b = True
    if s[i].isdigit() == True:
        c = True
    if s[i].islower() == True:
        d = True
    if s[i].isupper() == True:
        e = True
print(a)
print(b)
print(c)
print(d)
print(e)