# 20200714 - itertools.combinations()
"""
from itertools import combinations
print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]

A = [1,1,3,3,3]
 print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
"""
from itertools import combinations
data = input().split()
action = []
for i in range(len(data[0])):
    action.append(data[0][i])
    action.sort()
# print(action)

for j in range(int(data[1])):
    sol = list(combinations(action, j+1))
    # print(sol)
    for k in range(len(sol)):
        print("".join(sol[k]))
