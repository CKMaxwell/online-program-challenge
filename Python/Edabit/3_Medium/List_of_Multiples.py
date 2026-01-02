# 20200827 - List of Multiples
def list_of_multiples(num, length):
    return [i * num for i in range(1, length + 1)]

print(list_of_multiples(7, 5))