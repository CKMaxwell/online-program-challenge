# 20200827 - Check If Lines Are Parallel
def lines_are_parallel(l1, l2):
    if l2[0] == 0 or l2[1] == 0:
        if (l1[0]+1) / (l2[0]+1) == (l1[1]+1) / (l2[1]+1):
            return True
        else:
            return False

    elif l1[0]/l2[0] == l1[1]/l2[1]:
        return True
    else:
        return False