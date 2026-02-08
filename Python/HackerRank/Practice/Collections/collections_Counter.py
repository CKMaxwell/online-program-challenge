# 20200803 - collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

"""
Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""

"""
>> from collections import Counter
>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>> print Counter(myList).values()
[3, 4, 4, 2, 1]
"""
from collections import Counter
number = int(input())
data = list(map(int, input().split()))
data_dict = Counter(data)
customer = int(input())

total_earn = 0
for i in range(customer):
    customer_dict = {}
    key, value = map(int, input().split())
    customer_dict[key] = value
    if (key in data_dict.keys()) and (data_dict[key] > 0):
        total_earn += value
        data_dict[key] -= 1
print(total_earn)
