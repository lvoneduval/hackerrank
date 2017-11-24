#!/bin/python3

import sys


n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
li = list(set(scores))
li.sort()
rank = 0
n = len(li)
for i in alice:
  j = rank
  while (j < n and (i >= li[j])):
      j += 1
  rank = j
  print(n - rank + 1)
