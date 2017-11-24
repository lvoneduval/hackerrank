#!/bin/python3

import sys

def sockMerchant(n, ar):
    # Complete this function
    ar.sort()
    sock = 0;
    lastcol = ar[-1]
    r = range(lastcol + 1)
    for i in r:
      sock += int(ar.count(i) / 2)
    return (sock)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
