#!/bin/python3

import sys

def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    if (len(s1 & s2)):
      return("YES")
    return("NO")
    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
