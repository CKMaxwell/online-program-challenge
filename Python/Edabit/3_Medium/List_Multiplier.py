# 20200904 - List Multiplier
def multiply(l):
    ans = []
    for i in range(len(l)):
        data = []
        for j in range(len(l)):
            data.append(l[i])
        ans.append(data)
    return ans

print(multiply(["*", "%", "$"]))

#其他解法
def multiply(lst):
	return [[i]*len(lst) for i in lst]

#其他解法 2
multiply = lambda l : [[item] * len(l) for item in l]