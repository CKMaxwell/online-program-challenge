# 20200901 - Volume of a Spherical Shell
def vol_shell(r1, r2):
	import math
	vol = 4 / 3 * math.pi * abs(r2 ** 3 - r1 ** 3)
	return round(vol, 3)

