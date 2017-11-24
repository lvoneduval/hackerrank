#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
i = 0
e = 100
while (i != n):
  if (c[i] == 1):
    e -= 2
  i +=k
  e -=1
print(e)
