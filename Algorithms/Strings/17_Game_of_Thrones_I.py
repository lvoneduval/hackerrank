#!/bin/python3

import sys

def gameOfThrones(s):
  tab = [0] * 26
  orda = ord("a")
  b = False
  for a in s:
    tab[ord(a) - orda] += 1
  for i in range(26):
    if (tab[i] % 2 and not(b)):
      b = True
    elif (tab[i] % 2):
      return("NO")
  return("YES")
    # Complete this function

s = input().strip()
result = gameOfThrones(s)
print(result)
