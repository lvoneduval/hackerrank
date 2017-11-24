#!/bin/python3

import sys


t = int(input().strip())
c = 3
k = 1
i = 1
while (i <= t):
  i += c*k
  k *=2
k //= 2
i -= c*k
print(c * k - (t - i))
