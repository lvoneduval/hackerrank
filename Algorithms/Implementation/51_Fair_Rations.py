#!/bin/python3

import sys


n = int(input().strip())
b = [int(B_temp) for B_temp in input().strip().split(' ')]
c = []
cnt = 0
i = 0
while (i < n):
  if (b[i] % 2):
    j = i + 1
    while (j < n and not(b[j] % 2)):
      j += 1
    if (j == n):
      cnt = -1
      i = n
    else:
      cnt += (j - i) * 2
      i = j
      b[i] += 1
  else:
    i +=1
print(cnt if (cnt >= 0) else "NO")
