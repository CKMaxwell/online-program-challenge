# You are given three integers x,y and z, representing the dimensions of a cuboid along with an integer N.
# You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of  is not equal to N
# Here, 0 <= i <= x, 0 <= j <= y, 0 <= k <= z
x = int(input())
y = int(input())
z = int(input())
n = int(input())
ans = []
for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i + j + k != n:
                temp = [i, j, k]
                ans.append(temp)
print(ans)
