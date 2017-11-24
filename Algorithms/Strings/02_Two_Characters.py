#!/bin/python3

import sys

def valide(s):
  for i in range(len(s) - 1):
    if(s[i] == s[i + 1]):
      return(False)
  return(True)

s_len = int(input().strip())
s = input().strip()
l = list(set(s))
res = 0
for i in range(len(l)):
  for j in range(i + 1, len(l)):
    c = [a for a in s if (a == l[i] or a== l[j])]
    if(valide(c)):
      res = max(res,len(c))
print(res)
