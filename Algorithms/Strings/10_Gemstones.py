#!/bin/python

import sys

def gemstones(arr):
    alphab = [0] * 26
    lena = len(arr)
    orda = ord('a')
    for s in arr:
      s = set(s)
      for l in s:
        alphab[ord(l) - orda] += 1
    return(alphab.count(lena))
    # Complete this function

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)

