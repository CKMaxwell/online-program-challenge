# 20201116 - Cricket Balls to Overs!
def total_overs(balls):
    return balls // 6 + (balls % 6) / 10


print(total_overs(945))