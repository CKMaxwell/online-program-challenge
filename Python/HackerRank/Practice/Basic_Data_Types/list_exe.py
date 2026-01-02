# 20200618 - Find the Runner-Up Score!
n = int(input())
arr = list(map(int, input().split()))
# print(arr)
max_val = max(arr)
# print(max_val)
arr_copy = arr.copy()
for i in range(0, n):
    if arr[i] == max_val:
        arr_copy.remove(max_val)

print(max(arr_copy))

