# 20200825 - Let's Meet!
def lets_meet(distance, va, vb):
    import math
    hr_temp = distance / (va + vb)
    hr = round(math.modf(hr_temp)[1])
    mi = round(math.modf((math.modf(hr_temp)[0]) * 60)[1])
    sec = math.floor(math.modf((math.modf(hr_temp)[0]) * 60)[0]*60)
    time = str(hr) + "h " + str(mi) + "min " + str(sec) + "s"
    return time

print(lets_meet(90, 75, 65))