# 20201114 - Right Shift by Division
def shift_to_right(x, y):
    import math
    return math.floor(x/2**y)

print(shift_to_right(-24, 2))