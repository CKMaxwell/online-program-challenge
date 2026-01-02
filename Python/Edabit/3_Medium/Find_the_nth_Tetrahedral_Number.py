# 20201020 - Find the nth Tetrahedral Number
def tetra(n):
    return (n * (n + 1) * (n + 2)) / 6

print(tetra(6))