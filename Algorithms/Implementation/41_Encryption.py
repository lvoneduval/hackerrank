#!/bin/python3

import sys
from math import *

s = input().strip()
len_s = len(s)
r, c = [floor(sqrt(len_s)), ceil(sqrt(len_s))]
r += (r * c < len_s)
M = [[0 for i in range(c)] for i in range(r)]
for i in range(len_s):
  M[i//c][i % c] = s[i]
for i in range(c):
  for j in range(r):
    if M[j][i] != 0:
      sys.stdout.write(M[j][i])
  if (i != c - 1):
    sys.stdout.write(' ')
