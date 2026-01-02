# 20200925 - Majority Vote
def majority_vote(lst):
    if len(lst) == 0:
        return None
    else:
        check = 0
        for i in set(lst):
            if lst.count(i) > (len(lst)/2):
                return i
            else:
                continue
        if check == 0:
            return None

print(majority_vote(["A", "A", "B"]))
#print(majority_vote(["A", "A", "A", "B", "C", "A"]))
#print(majority_vote(["A", "B", "B", "A", "C", "C"]))

""" 其他人更好的寫法
def majority_vote(lst): 
  for i in set(lst):
    if lst.count(i)>len(lst)//2:
      return i
  return None
"""