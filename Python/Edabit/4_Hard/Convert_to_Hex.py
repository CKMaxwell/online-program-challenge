# 20201029 - Convert to Hex
def convert_to_hex(txt):
    ans = []
    for i in range(len(txt)):
        ans.append(hex(ord(txt[i]))[2:])
    return " ".join(ans)

print(convert_to_hex("Big Boi"))