#!/bin/python3

import sys

def migratoryBirds(n, ar):
    ar.sort()
    typ = [0] * (ar[-1] + 1)
    r = range(ar[-1] + 1)
    for i in r:
      typ[i] = ar.count(i)
    maxi = max(typ)
    
    return [i for i, j in enumerate(typ) if  j == maxi][0]
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
