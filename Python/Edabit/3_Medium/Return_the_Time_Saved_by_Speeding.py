# 20200827 - Return the Time Saved by Speeding
def time_saved(s_lim, s_avg, d):
    t = (d/s_lim - d/s_avg) * 60
    return round(t, 1)

print(time_saved(80, 90, 40))