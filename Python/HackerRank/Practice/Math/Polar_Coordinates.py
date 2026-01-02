# 20200712 - Polar Coordinates
"""
import cmath
phase(complex(-1.0, 0.0))
3.1415926535897931
abs(complex(-1.0, 0.0))
1.0
"""
from cmath import phase
orig = input()
x = 0
y = 0
for i in range(len(orig)):
    if orig[i] == "+":
        x = float(orig[:i])
        y = float(orig[i + 1:-1])
        break
    elif orig[i] == "-" and i != 0:
        x = float(orig[:i])
        y = float(orig[i:-1])
        break
print(abs(complex(x, y)))
print(phase(complex(x, y)))


"""
更好的寫法
import cmath
print(*cmath.polar(complex(input())), sep='\n')
"""