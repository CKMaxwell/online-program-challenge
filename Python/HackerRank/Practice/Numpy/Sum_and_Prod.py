# 20200711 - Sum and Prod
""""
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])
print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
"""
import numpy as np
shape = list(map(int, input().split()))
ar = np.array([input().split() for i in range(shape[0])], int)
print(np.prod(np.sum(ar, axis=0)))
