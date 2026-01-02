# 20201208 - Invert Keys and Values
def invert(dct):
    ans = {v: k for k, v in dct.items()}
    return ans

print(invert({ "z": "q", "w": "f" }))
print(invert({ "zebra": "koala", "horse": "camel" }))