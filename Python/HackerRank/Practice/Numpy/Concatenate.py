# 20200711 - Concatenate
"""
import numpy
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])
print numpy.concatenate((array_1, array_2, array_3))

#Output
[1 2 3 4 5 6 7 8 9]

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])
print numpy.concatenate((array_1, array_2), axis = 1)

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]
"""
import numpy as np
shape = list(map(int, input().split()))
length = shape[0] + shape[1]
fir_ans = list(map(int, input().split()))
ans = np.array(fir_ans)
for i in range(length)-1:
    

