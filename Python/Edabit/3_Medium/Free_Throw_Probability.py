# 20201217 - Free Throw Probability
def free_throws(success, rows):
    rate = int(success[:-1])/100
    ans = round(rate ** rows *100)
    return str(ans) + "%"

print(free_throws("75%", 5) )