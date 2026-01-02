# 20200701 - Merge the Tools
def merge_the_tools(string, k):
    seg = int(len(string) / k)
    # print(seg)
    for i in range(0, seg):
        ans = string[k * i: k * i + k]
        ans2 = ""
        for j in range(k):
            if ans[j] not in ans2:
                ans2 = ans2 + ans[j]
        print(ans2)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)