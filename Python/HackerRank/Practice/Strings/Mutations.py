# 20200624 - Mutations
def mutate_string(string, position, character):
    ans = string[:position] + character + string[position+1:]
    return ans

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)