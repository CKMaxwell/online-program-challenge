# 20200713 - Triangle Quest 2
for i in range(1, int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(*list(map(lambda x: i - abs(x - i), range(1, i * 2))), sep='')
"""
lambda語法說明：
    lambda m, n: m if m > n else n
    輸入數值[m,n]  (可以只有一個)
    回傳值：分號後的[m if m > n else n]
    通常這邊也會順便帶運算
"""
