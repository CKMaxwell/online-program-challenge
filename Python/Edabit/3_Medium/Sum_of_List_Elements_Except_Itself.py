# 20201202 - Sum of List Elements Except Itself
def lst_ele_sum(args):
    ans =[]
    for i in args:
        val = sum(args) - i
        ans.append(val)
    return ans

print(lst_ele_sum([1, 2, 3, 2, 1]))