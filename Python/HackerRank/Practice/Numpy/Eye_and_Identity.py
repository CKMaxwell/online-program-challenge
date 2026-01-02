# 20200803 - Eye and Identity
"""
import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.
"""
import numpy
N, M = map(int, input().split())
ans = str(numpy.eye(N, M)).replace('1', ' 1').replace('0', ' 0')
print(ans)