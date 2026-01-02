# 20201005 - Next Prime
def next_prime(num):
    def prime(current):
        check = True
        for i in range(2, current//2):
            if current % i == 0:
                check = False
        return check

    if prime(num) == True:
        return num
    else:
        while True:
            num += 1
            if prime(num) == True:
                return num


print(next_prime(24))