# 20200702 - Set .difference() Operation
n_num = int(input())
n = set(map(int, input().split()))
b_num = int(input())
b = set(map(int, input().split()))
ans = len(n.difference(b))
print(ans)