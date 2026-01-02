# 20201015 - Geometry 1: Length of Line Segment
import math
def line_length(dot1, dot2):
    dis = ((dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2) ** 0.5
    return round(dis, 2)

print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [0, 0]))