# 20200627 - Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, (input().split()))
pic = ".|."
for i in range(1, N+1):
    if i < (N/2 + 0.5):
        print((pic*(2*i-1)).center(M, '-'))
    elif i == (N/2 + 0.5):
        print("WELCOME".center(M, '-'))
    elif i > (N / 2 + 0.5):
        ans = (pic * int((2*(i - (i-(N/2 + 0.5))*2))-1))
        # 這邊的文字乘法要轉成整數
        print(ans.center(M, '-'))
