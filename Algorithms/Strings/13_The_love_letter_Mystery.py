#!/bin/python

import sys

def theLoveLetterMystery(s):
    lens = len(s)
    res = 0
    for i in range(lens //2):
      res += abs(ord(s[i]) - ord(s[lens - i -1]))
    return(res)
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    print(result)
