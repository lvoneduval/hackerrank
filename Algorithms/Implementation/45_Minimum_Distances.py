#!/bin/python3

import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
min_d = n
for i in range(n):
  for j in range(i + 1, n):
    if(A[i] == A[j]):
       min_d = min(abs(i - j), min_d)
       break
print(min_d if min_d != n else -1)
