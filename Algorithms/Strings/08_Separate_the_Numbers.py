#!/bin/python3

import sys

def grandeur(n):
  i = 1
  c = 0
  while(i <= n):
    c += 1
    i *= 10
  return(c)

q = int(input().strip())
for a0 in range(q):
    grandmin = 1
    grand = 1
    grandbef = 1
    s = input().strip()
    l = len(s)    
    i = 0
    cmp = int(s[:grand])
    while (i < l - grand + 1):
      if(int(s[i:i + grand]) != cmp or s[i] == "0"):
        grandbef += 1
        grandmin = grandbef
        cmp = int(s[:grandbef])
        grand = grandbef
        i = 0
      else:
        i += grand
        cmp += 1
        grand = grandeur(cmp)
    grand = grandeur(cmp - 1)  
    if (grandmin > len(s)/2 or (cmp - 1) != int(s[-grand:])):
      print("NO")
    else:
      print("YES", s[:grandmin])
