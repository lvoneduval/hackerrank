#!/bin/python3

import sys

def isValid(s):
  tmp = list(set(s))
  orda = ord("a")
  tab = [0] * 26
  for i in tmp:
    tab[ord(i) - orda] += s.count(i)
  tmp1 = set(tab)
  tmp1.discard(0)
  if (len(tmp1) == 1):
    return("YES")
  if (len(tmp1) == 2):
    maxi = max(tmp1)
    mini = min(tmp1)
    if((tab.count(maxi) == 1 and (maxi - mini == 1)) 
      or (tab.count(mini) == 1 and mini == 1)):
      return("YES")
  return("NO")
    
    # Complete this function

s = input().strip()
result = isValid(s)
print(result)
