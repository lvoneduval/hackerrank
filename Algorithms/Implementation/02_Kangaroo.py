#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
    dx = x1 - x2
    dv = v1 - v2
    if (dv == 0):
      if dx == 0:
        return ("YES")
      else:
        return ("NO")
    elif (dx % dv == 0) and (dx/dv < 0):
      return ("YES")
    else:
      return ("NO")
    # Complete this function

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
