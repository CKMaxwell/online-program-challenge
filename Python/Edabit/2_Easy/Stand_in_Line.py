# 20201030 - Stand in Line
def next_in_line(lst, num):
    if len(lst) == 0:
        return "No list has been selected"
    else:
        lst.pop(0)
        lst.append(num)
        return lst

print(next_in_line([1, 10, 20, 42 ], 6))