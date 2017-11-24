#!/bin/python3

import sys
def ispossible(n, b):
  if b.count('_'):
    for k in b:
      if b.count(k) == 1 and k != '_':
        return(False)
  else:
    for i in range(n):
      if not((i > 0 and b[i] == b[i - 1]) or (i < n - 1 and b[i] == b[i + 1])):
        return(False)
  return(True)

Q = int(input().strip())
for a0 in range(Q):
  n = int(input().strip())
  b = input().strip()
  print("YES" if ispossible(n,b) else "NO")
