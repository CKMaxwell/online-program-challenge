# 20200810 - Incorrect Regex
import re
for i in range(int(input())):
    test = input()
    try:
        a, b = map(int, input().split())
        print(a // b)
    except Exception  as e:
        print("Error Code:", e)