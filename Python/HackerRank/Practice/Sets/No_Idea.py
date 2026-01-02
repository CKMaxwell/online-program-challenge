# 20200702 - No Idea!
n_num, m_num = input().split()
cal = list(map(int, input().split()))
n = set(map(int, input().split()))
m = set(map(int, input().split()))
happiness = 0
for i in range(len(cal)):
    if cal[i] in n:
        happiness = happiness + 1
    elif cal[i] in m:
        happiness = happiness - 1
    else:
        happiness = happiness
print(happiness)