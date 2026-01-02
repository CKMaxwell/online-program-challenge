# 20201120 - Next Number Greater Than A and B and Divisible by B
def divisible_by_b(a, b):
    i = 1
    while b * i < a:
        i += 1
    return b * i

print(divisible_by_b(98, 3))