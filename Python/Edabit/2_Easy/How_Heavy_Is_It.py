# 20200822 - How Heavy Is It?
def weight(r, h):
    import math
    ans = (math.pi * r ** 2) * h / 1000
    return round(ans, 2)

print(weight(4, 10))