# 20200618 - Nested Lists
total = []
total_score = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    new_data = [name, score]
    total.append(new_data)
    total_score.append(score)

final_score = total_score.copy()
max_score = min(final_score)
for j in range(0, n):
    if total_score[j] == max_score:
        final_score.remove(max_score)
sec_sco = min(final_score)

# 輸出答案
ans = []
for k in range(n):
    if total_score[k] == sec_sco:
        ans.append(total[k][0])
# 依字母順序做排序
ans.sort()
for m in range(0, len(ans)):
    print(ans[m])
