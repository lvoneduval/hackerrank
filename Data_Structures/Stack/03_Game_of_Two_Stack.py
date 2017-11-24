#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    tot = 0
    res = 0
    i = 0
    j = 0
    while (i < n and tot + a[i] <= x):
      tot += a[i]
      i += 1
    res = i
    while (j < m and i >= 0):
      tot += b[j]
      j += 1
      while (tot > x and i > 0):
        i -= 1
        tot -= a[i]
      if (i + j > res and tot <= x):
        res = i + j
    print(res)
