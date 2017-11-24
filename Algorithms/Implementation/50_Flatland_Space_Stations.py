#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
res = [n] * n
for i in c:
  res[i] = 0
for i in c:
  j = 1
  while (i - j >= 0 and j < res[i - j]) or (i + j < n and j < res[i + j]):
    if (i - j >= 0 and j < res[i - j]):
      res[i - j] = j
    if (i + j < n and j < res[i + j]):
      res[i + j] = j
    j += 1
print(max(res))
