# 20200708 - Zeros and Ones
""""
print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]]

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]]

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]
"""
import numpy as np
ans1 = []
ans2 = []
data = list(map(int, input().split()))
ans1 = (np.zeros(data,  dtype=np.int))
ans2 = (np.ones(data,  dtype=np.int))
print(ans1)
print(ans2)
