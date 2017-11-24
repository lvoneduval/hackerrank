#!/bin/python3

import sys


s = input().strip()
s = [a for a in s]
cmp = ["S","O","S"]
lens= len(s)
i = 0
res = 0
for i in range(lens):
    if(s[i] != cmp[i % 3]):
      res +=1
print(res)
