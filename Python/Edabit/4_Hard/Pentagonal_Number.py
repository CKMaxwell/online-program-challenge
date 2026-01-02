# 20200909 - Pentagonal Number
def pentagonal(num):
    dot = 0
    for i in range(2, num+1):
    # 第一層需要額外考慮 --> 最後再 + 1
        dot_layer = i + (i-1)*3 + (i-2)
        dot += dot_layer
    return dot + 1


print(pentagonal(8))