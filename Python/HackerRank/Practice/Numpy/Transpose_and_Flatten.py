# 20200718 - Transpose and Flatten
"""
import numpy
my_array = numpy.array([[1,2,3], [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]

 ----------------------------------------------
my_array = numpy.array([[1,2,3], [4,5,6]])
print my_array.flatten()
#Output
[1 2 3 4 5 6]
"""
import numpy as np
N, M = map(int, input().split())
data = np.array([input().split() for i in range(N)], int)
print(np.transpose(data))
print(data.flatten())
