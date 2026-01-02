# 20200911 - Prison Break
# 此題設計有問題-未來再回頭看

def freed_prisoners(prison):
    count = 0
    for i in range(len(prison)):
        if prison[i] == 1:
            count += 1
            for j in range(len(prison)):
                if prison[i] == 1:
                    prison[i] == 0
                elif prison[i] == 0:
                    prison[i] == 1
    return count

print(freed_prisoners([0,0,0]))