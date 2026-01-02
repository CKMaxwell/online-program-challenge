# 20200913 - Classes For Fetching Information on a Sports Player
class player():

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def get_age(self):
        return (str(self.name) + " is age " + str(self.age))
    def get_height(self):
        return (str(self.name) + " is " + str(self.height) + "cm")
    def get_weight(self):
        return (str(self.name) + " weighs " + str(self.weight) + "kg")

player1 = player('Patrick Mahomes', 24, 188, 104)
player1.get_age(), 'Patrick Mahomes is age 24'

