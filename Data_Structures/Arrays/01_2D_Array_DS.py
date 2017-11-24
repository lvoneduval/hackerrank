#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
res = 0
maxi = -(2**63 - 1)
for i in range(0,4):
  for j in range(0,4):
    res = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
    res += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
    res += arr[i + 1][j + 1]
    maxi = max(res,maxi)
print(maxi)
