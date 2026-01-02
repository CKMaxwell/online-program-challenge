# 20200628 - String Formatting
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        ten = str(i)
        eight = oct(i)[2:]
        sixteen = hex(i)[2:].upper()
        two = bin(i)[2:]
        print(ten.rjust(width, " "), eight.rjust(width, " "), sixteen.rjust(width, " "), two.rjust(width, " "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
