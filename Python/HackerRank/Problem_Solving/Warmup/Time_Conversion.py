# 20200706 - Time Conversion
#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    check = s[len(s)-2:]
    if s[:2] == "12" and check == "AM":
        ans = "0" + str(int(s[0:2]) - 12) + s[2:len(s) - 2]
    elif s[:2] == "12" and check == "PM":
        ans = s[:len(s)-2]
    elif check == "AM":
        ans = s[:len(s)-2]
    elif check == "PM":
        ans = str(int(s[0:2]) + 12) + s[2:len(s)-2]
    return ans

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
