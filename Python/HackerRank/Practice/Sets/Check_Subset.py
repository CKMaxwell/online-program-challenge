# 20200703 - Check Subset
num = int(input())
for i in range(num):
    a_num = int(input())
    a = set(map(int, input().split()))
    b_num = int(input())
    b = set(map(int, input().split()))
    if b.intersection(a) == a:
        print("True")
    else:
        print("False")
