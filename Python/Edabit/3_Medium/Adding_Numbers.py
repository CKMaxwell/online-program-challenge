# 20201201 - Adding Numbers
def add(n1, n2):
    if n1 == "" or n2 == "" or n1 == None or n2 == None:
        return "Invalid Operation"
    else:
        return str(eval("int(n1)+int(n2)"))

print(add("10", "80"))
print(add("", "20"))

"""
其他寫法
def add(a,b):
	try:return str(int(a)+int(b))
	except:return'Invalid Operation'
"""