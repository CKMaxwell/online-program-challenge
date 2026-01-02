# 20200811 - Input()
x, k = map(int, input().split())
pol = list(input().split())
ans = ""
for i in range(len(pol)):
    ans = ans + pol[i]
result = eval(ans)
if int(result) == k:
    print("True")
else:
    print("False")