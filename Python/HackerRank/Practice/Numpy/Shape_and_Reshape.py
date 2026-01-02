# 20200717 - Shape and Reshape
"""
import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns

import numpy
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array

#Output
[[1 2]
[3 4]
[5 6]]

import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]
"""
import numpy as np
data = list(map(int, (input().split())))
ans = np.array(data)
ans.shape = (3, 3)
print(ans)
