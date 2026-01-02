# 20201029 - Combined Consecutive Sequence
def consecutive_combo(lst1, lst2):
    total = lst1 + lst2
    total.sort()
    check = (min(total) + max(total)) * len(total) / 2
    if sum(total) == check:
        return True
    else:
        return False

print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))