# 20200712 - Find Angle MBC
"""
import math
import numpy as np
ab, bc = map(int, input().split())
vec_cb = np.array([-bc, 0])
vec_ca = np.array([-bc, ab])
ans = math.acos(np.dot(vec_cb, vec_ca) /
                (math.sqrt(bc**2) * math.sqrt(bc**2 + ab ** 2))
                )
#print(vec_cb, vec_ca)
#print(np.dot(vec_cb, vec_ca)/ (ab * bc))
print(round(math.degrees(ans)), "°")
"""
import math
ab = int(input())
bc = int(input())
ans = math.degrees(math.atan(ab/bc))
print(str(round(ans)) + "°")
