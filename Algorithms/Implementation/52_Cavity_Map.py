#!/bin/python3

import sys


n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
  b = str(input().strip())
  b = [int(a) for a in b]
  grid.append(b)
for i in range(0, n):
  for j in range(0 ,n):
    tmp = grid[i][j]
    if (i > 0 and i < n - 1 and j > 0 and j < n - 1 and tmp > grid[i + 1][j] and tmp > grid[i - 1][j] and tmp > grid[i][j + 1] and tmp > grid[i][j - 1]):
      sys.stdout.write('X')
    else:
      sys.stdout.write(str(tmp))
  sys.stdout.write('\n')
