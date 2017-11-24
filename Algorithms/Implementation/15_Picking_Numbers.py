#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a.sort()
count = [0] * (a[-1] + 1)
for i in range(a[-1] + 1):
  count[i] = a.count(i) + a.count(i - 1)
print(max(count))
