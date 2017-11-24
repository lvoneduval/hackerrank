#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
      M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
      M.append(M_t)
    
    row = []
    for r_i in range(n):
      r_t = sum(M[r_i])
      row.append(r_t)
    
    col = []
    for i in range(n):
      c = 0
      for j in range(n):
        c += M[j][i]
      col.append(c)
    print("Possible" if sorted(col) == sorted(row) else "Impossible")
