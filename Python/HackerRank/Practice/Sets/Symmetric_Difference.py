#20200701 - Symmetric Difference
m_count = input()
m = set(input().split())
n_count = input()
n = set(input().split())
ans = m.difference(n)
ans2 = n.difference(m)
result = list(ans.union(ans2))
result2 = []
for i in range(len(result)):
    result2.append(int(result[i]))
result2.sort()
for j in range(len(result2)):
    print(result2[j])


