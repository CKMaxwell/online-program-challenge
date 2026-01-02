# 20200924 - Tallest Skyscraper
# 關於跳出多層迴圈的寫法，請多查資料多看解答
def tallest_skyscraper(lst):
    height = len(lst)
    for i in range(height):
        for j in range(len(lst[i])):
            if lst[i][j] == 1:
                ans = height - i
                return ans


print(tallest_skyscraper([  [0, 0, 0, 0],  [0, 1, 0, 0],  [0, 1, 1, 0],  [1, 1, 1, 1]] ))