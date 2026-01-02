# if __name__ == '__main__':
n = int(input())
for i in range(1, n):
    print(i * i)

# 閏年問題
def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                leap = True
    return leap

year = int(input())
print(is_leap(year))

# 輸出數字不換行
n = int(input())
for i in range(1, n+1):
    print(i, end='')       # print()的原型  print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

