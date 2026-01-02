# 20200703 - Check Strict Superset
set_a = set(map(int, input().split()))
num = int(input())
ans = []
for i in range(num):
    set_b = set(map(int, input().split()))
    if set_a.intersection(set_b) == set_b and set_a.intersection(set_b) != set_a:
        ans.append("True")
    else:
        ans.append("False")
    #print(set_a.intersection(set_b))
    #print(set_b)
    #print(ans)
if "False" not in ans:
    print("True")
else:
    print("False")