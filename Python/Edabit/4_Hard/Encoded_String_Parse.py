# 20201027 - Encoded String Parse
def parse_code(txt):
    data = {"first_name": "", "last_name": "", "id": ""}
    ans = txt.split("0")
    ans2 = []
    for i in ans:
        if i != "":
            ans2.append(i)
    data["first_name"] = ans2[0]
    data["last_name"] = ans2[1]
    data["id"] = ans2[2]
    return data

print(parse_code("John000Doe000123"))