# 20201014 - Operations
def operation(a, b, op):
    if op == "add":
        return str(round(int(a) + int(b)))
    elif op == "subtract":
        return str(round(int(a) - int(b)))
    elif op == "divide":
        if b == "0":
            return "undefined"
        else:
            return str(round(int(a) / int(b)))
    elif op == "multiply":
        return str(round(int(a) * int(b)))

print(operation("6", "3", "divide"))