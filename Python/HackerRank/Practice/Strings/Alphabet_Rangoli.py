# 20200628 - Alphabet Rangoli
def print_rangoli(size):
    width = ((2 * size) - 1) + ((2 * size) - 2)
    # center = chr(96+size)  #ASCII 的 97是"a"
    result = ""
    for q in range(1, 2 * size - 1 + 1):
        if q <= size:
            char1 = ""
            for m in range(q):
                char1 = char1 + chr(96 + size - m)
            char2 = ""
            for p in range(1, q):
                char2 = char2 + chr(96 + (size - q + 1) + p)
            character = "-".join(char1 + char2)

        if q > size:  # q = 6 開始
            char1 = ""
            s = q - (q - size) * 2
            for m in range(0, s):
                char1 = char1 + chr(96 + size - m)
            char2 = ""
            for p in range(1, s):
                char2 = char2 + chr(96 + (size - s + 1) + p)
            character = "-".join(char1 + char2)

        ans = character.center(width, '-')
        result = result + ans + "\n"
    print(result)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)