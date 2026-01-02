# 20200702 - Set .intersection() Operation
n_num = int(input())
n = set(map(int, input().split()))
b_num = int(input())
b = set(map(int, input().split()))
ans = len(n.intersection(b))
print(ans)