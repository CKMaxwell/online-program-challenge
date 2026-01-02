# 20200627 - Text Wrap
import textwrap

def wrap(string, max_width):
    ans = ""
    for i in range(0, len(string)//max_width+1):
        if i + max_width < len(string):
            ans = ans + string[(max_width*i):(max_width*i)+max_width] + "\n"
        else:
            ans = ans + string[(max_width*i):len(string)] + "\n"
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)