# 20201026 - Moving to the End
def move_to_end(lst, el):
    lst_copy = lst.copy()
    for i in range(len(lst)):
        if lst[i] == el:
            lst_copy.remove(el)
            lst_copy.append(el)
    return lst_copy

print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end(["a", "a", "a", "b"], "a"))