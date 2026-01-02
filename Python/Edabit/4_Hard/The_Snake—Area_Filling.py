# 20201125 - The Snake — Area Filling
def snakefill(n):
    i = 1
    while 2 ** i <= n ** 2:
        i += 1
    return i-1

print(snakefill(8))