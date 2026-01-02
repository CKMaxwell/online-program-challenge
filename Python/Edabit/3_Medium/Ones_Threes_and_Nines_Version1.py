# 20201017 - Ones, Threes and Nines (Version #1)
class ones_threes_nines:
    def __init__(self, num):
        self.num = num
        self.ones = num // 1
        self.threes = num // 3
        self.nines = num // 9
        """
    def ones(self):
        print(self.num)
        return self.num // 1
    def threes(self):
        return self.num // 3
    def nines(self):
        return self.num // 9
"""
n1 = ones_threes_nines(5)
print(n1.ones)