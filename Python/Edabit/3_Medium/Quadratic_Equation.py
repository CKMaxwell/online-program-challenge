# 20200903 - Quadratic Equation
def quadratic_equation(a, b, c):
    import math
    root = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return round(root)


print(quadratic_equation(2, -7, 3))
