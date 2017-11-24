#!/bin/python3

import sys

orde = ord("a") - 1
s = input().strip()
tab = set()
tmp = 0
for a in s:
  if (a != tmp):
    tmp = a
    lena = 1
    tab.add(ord(a) - orde)
  else:
    lena +=1
    tab.add(lena * (ord(a) - orde))
n = int(input().strip())
for a0 in range(n):
    x = int(input().strip())
    print("Yes" if (x in tab) else "No")
