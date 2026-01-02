# 20200810 - Exceptions
count = int(input())
for i in range(count):

    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception  as e:
        print("Error Code:", e)
