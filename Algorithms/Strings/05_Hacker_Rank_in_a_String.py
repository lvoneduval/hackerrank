#!/bin/python3

import sys

cmp = "hackerrank"
lencmp = len(cmp)
q = int(input().strip())
for a0 in range(q):
    i = 0
    s = input().strip()
    for a in s:
      if (i < lencmp and a == cmp[i]):
        i += 1
    print("YES" if lencmp == i else "NO")
