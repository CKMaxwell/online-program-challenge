# 20200702 - Set .discard(), .remove() & .pop()
num = int(input())
orig = set(map(int, input().split()))
count = int(input())
for i in range(count):
    action = input().split()
    if action[0] == "pop":
        eval("orig.pop()")
    else:
        eval("orig." + str(action[0]) + "(" + str(action[1]) + ")")
print(sum(orig))