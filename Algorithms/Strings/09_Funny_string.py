#!/bin/python

import sys

def funnyString(s):
    ls = len(s)
    res = "Funny"
    cmp = -1
    for i in range(1,ls//2 + 1):
      if (abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[ls - i - 1]) -ord(s[ls - i ]))):
        res = "Not Funny" 
    return (res)
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = funnyString(s)
    print(result)
