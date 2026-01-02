# 20200622-Lists
# 使用eval函數，把字串當成指令
n = int(input())
ans_list = []
for i in range(0, n):
    input_cmd = input().split()
    if input_cmd[0] == "insert":
        eval(str("ans_list.insert(" + str(input_cmd[1]) +"," + str(input_cmd[2]) + ")"))
    elif input_cmd[0] == "print":
        eval("print(ans_list)")
    elif input_cmd[0] == "remove":
        eval(str("ans_list.remove(" + str(input_cmd[1]) + ")"))
    elif input_cmd[0] == "append":
        eval(str("ans_list.append(" + str(input_cmd[1]) + ")"))
    elif input_cmd[0] == "sort":
        eval("ans_list.sort()")
    elif input_cmd[0] == "pop":
        eval("ans_list.pop()")
    elif input_cmd[0] == "reverse":
        eval("ans_list.reverse()")
