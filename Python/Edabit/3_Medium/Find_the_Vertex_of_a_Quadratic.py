# 20200830 - Find the Vertex of a Quadratic
def find_vertex(a, b, c):
    x = -b / (2 * a)
    y = a * x ** 2 + b * x + c
    return [x, y]


print(find_vertex(1, 10, 4))