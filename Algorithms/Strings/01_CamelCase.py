#!/bin/python3

import sys


s = input().strip()
res = 0
b = False
for a in s:
  if (not(b) and a.islower()):
    b = True
    res += 1
  elif(b and not(a.islower())):
    b = False
print(res)
