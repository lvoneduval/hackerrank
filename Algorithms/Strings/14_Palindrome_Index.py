#!/bin/python3

import sys
from math import floor

def ispalyndrome(s,i,j):
  while(i < j):
    if s[i] != s[j]:
      return(False)
    i+=1
    j-=1
  return(True)

def palindromeIndex(s):
    lens = len(s)
    b = False
    res = -1
    i = 0
    while i < floor(lens//2) and not(b) and res == -1:
      if (not(b) and s[i] != s[lens - i - 1]):
        if (ispalyndrome(s,i,lens- i -2)):
          res = lens - i - 1
        elif(ispalyndrome(s,i+1,lens- i - 1)):
          res = i
        else:
          b = True
      i += 1
    return(res)
          
    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
