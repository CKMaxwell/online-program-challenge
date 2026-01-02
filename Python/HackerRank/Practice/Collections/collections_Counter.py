# 20200803 - collections.Counter()
"""
from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
 print Counter(myList)

Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]

print Counter(myList).keys()
[1, 2, 3, 4, 5]
print Counter(myList).values()
[3, 4, 4, 2, 1]
"""
from collections import Counter
number = int(input())
data = list(map(int, input().split()))
customer = int(input())
print(Counter(data).items())
sum = 0
print(Counter(data).values())
aaa = (Counter(data)[2])
print(aaa)
Counter(data)[2] = aaa-1
print(Counter(data)[2])
print(Counter(data).items())
"""
for i in range(customer):
    cus_data = list(map(int, input().split()))
    
"""