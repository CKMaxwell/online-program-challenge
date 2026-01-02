# 20200628 - Introduction to Sets
def average(array):
    ans = set()
    for i in range(len(arr)):
        ans.add(arr[i])
    final = sum(ans) / len(ans)
    return final
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)