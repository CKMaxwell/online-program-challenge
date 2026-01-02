# 20201006 - Oddly or Evenly Positioned
# 其他人的答案有一行寫法
def char_at_pos(r, s):
    if type(r) == list:
        ans = []
        if s == "even":
            for i in range(1, len(r), 2):
                ans.append(r[i])
        if s == "odd":
            for i in range(0, len(r), 2):
                ans.append(r[i])
        return ans
    elif type(r) == str:
        ans = ""
        if s == "even":
            for i in range(1, len(r), 2):
                ans += r[i]
        if s == "odd":
            for i in range(0, len(r), 2):
                ans += r[i]
        return ans

print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))
print(char_at_pos("EDABIT", "odd"))