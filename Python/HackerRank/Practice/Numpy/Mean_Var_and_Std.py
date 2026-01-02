# 20200717 - Mean, Var, and Std
import numpy as np
n, m = map(int, (input().split()))
data = np.array([input().split() for i in range(n)], int)
np.set_printoptions(legacy='1.13')
print(np.mean(data, axis=1))
print(np.var(data, axis=0))
print(np.std(data))