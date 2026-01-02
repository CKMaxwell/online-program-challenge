# 20201109 - Valid Division
def valid_division(d):
    check = d.split("/")
    if check[1] == "0":
        return "invalid"
    else:
        return eval(d) == round(eval(d))

print(valid_division("6/3"))
print(valid_division("30/25"))
