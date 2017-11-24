#!/bin/python3

import sys

def solve(n, s, d, m):
  w = 0
  if (n < m):
    return(0)
  else:
    r = range(n - m + 1)
  for i in r:
    if (sum(s[i:i + m]) == d):
      w += 1
    # Complete this function
  return w

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
