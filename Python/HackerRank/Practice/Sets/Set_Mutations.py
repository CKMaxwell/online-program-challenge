# 20200702 - Set Mutations
num = int(input())
orig = set(map(int, input().split()))
count = int(input())
for i in range(count):
    action = input().split()
    new_data = set(map(int, input().split()))
    eval("orig." + str(action[0] + "(" + str(new_data) + ")"))
print(sum(orig))
