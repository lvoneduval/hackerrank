#!/bin/python3

import sys

def getRecord(s):
    r = [0,0]
    hr = s[0]
    lr = s[0]
    for el in s:
      if el > hr:
        hr = el
        r[0] += 1
      if el < lr:
        lr = el
        r[1] += 1
    return (r)
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))

