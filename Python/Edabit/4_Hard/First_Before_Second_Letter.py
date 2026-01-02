# 20200902 - First Before Second Letter
def first_before_second(s, first, second):
    for i in range(len(s)):
        if s[i] == first:
            loc_a = i
    for j in range(len(s)-1, 0-1, -1):
        if s[j] == second:
            loc_b = j
    if loc_a < loc_b:
        return True
    else:
        return False

print(first_before_second("happy birthday", "a", "y"))

def first_before_second(s, first, second):
	return s.rindex(first) < s.index(second)

def first_before_second(s, first, second):
    return s.rfind(first) < s.find(second)