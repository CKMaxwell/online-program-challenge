# 20200826 - How Many Solutions Does This Quadratic Have?
def solutions(a, b, c):
    det = (b ** 2 - 4 * a * c)
    if det > 0:
        return 2
    if det == 0:
        return 1
    if det < 0:
        return 0
