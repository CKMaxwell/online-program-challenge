# 20200916 - Algorithms I: Introduction to Recursion
def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)

print(factorial(5))