#!/bin/python3

import sys
def rotate(l, n):
    return l[n:] + l[:n]

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    if (k == 0):
      print(" ".join([str(b) for b in range(1,n + 1)]))
    elif (n % 2 == 0 and n/k % 2 == 0):
      ran = [0] * (n + 1)
      for i in range(1,n+1):
        if (ran[i] == 0):
          ran[i] = i + k
          ran[i + k] = i
      ran = ran[1:]
      print(" ".join([str(b) for b in ran]))
    else:
      print("-1")
