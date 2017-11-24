#!/bin/python3

import sys


s = str(input().strip())
t = str(input().strip())
k = int(input().strip())
i = 0
len_t = len(t)
len_s = len(s)
len_min = len_s if len_s < len_t else len_t
while (i < len_min and s[i] == t[i]):
  i += 1
cost_min = k - ((len_s - i) + (len_t - i))
if (cost_min >= 0 and cost_min % 2 == 0) or (k >= len_s + len_t):
  print("Yes")
else :
  print("No")
