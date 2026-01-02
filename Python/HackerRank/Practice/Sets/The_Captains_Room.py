# 20200707 - The Captain's Room
num = int(input())
orig = list(map(int, input().split()))
# orig_set = set(orig)
empty = set()
second = set()
for i in orig:
    if i not in empty:
        empty.add(i)
    else:
        second.add(i)
for j in second:
    empty.remove(j)
ans = list(map(int, empty))
print(ans[0])