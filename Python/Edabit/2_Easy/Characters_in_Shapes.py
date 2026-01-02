# 20201019 - Characters in Shapes
def count_characters(lst):
    ans = 0
    for i in range(len(lst)):
        ans += len(lst[i])
    return ans

print(count_characters([
  "###",
  "###",
  "###"
]))