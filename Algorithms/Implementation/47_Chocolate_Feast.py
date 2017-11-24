#!/bin/python3

import sys

def f(w,m):
  if (w < m):
    return(0)
  else:
    return(w // m + f(w//m + w % m, m))

t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    print(n//c + f(n//c, m))
