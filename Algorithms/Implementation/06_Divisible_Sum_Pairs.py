#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    nb = 0
    i = 0
    j = 0
    while (i < n - 1):
      j = i + 1
      while (j < n):
        if ((ar[i] + ar [j]) % k == 0):
          nb += 1
        j += 1
      i += 1
    return (nb)
    # Complete this function

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
