# 20200826 - Two Distinct Elements
def return_unique(lst):
    sol = {}
    for i in lst:
        if i not in sol:
            sol[i] = 1
        elif i in sol:
            sol[i] = sol[i] + 1
    print(sol)
    ans = []
    for j in sol:
        if sol[j] == 1:
            ans.append(j)

    ans_sort = []
    for k in lst:
        if k in ans:
            ans_sort.append(k)
    return ans_sort


print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
