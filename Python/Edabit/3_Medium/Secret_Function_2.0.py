# 20201207 - Secret Function 2.0
def secret(text):
    data = text.split("*")
    ans = ("<" + data[0] + ">" + "</" + data[0] + ">")*int(data[1])
    return ans

print(secret("div*2"))
print(secret("li*3"))

