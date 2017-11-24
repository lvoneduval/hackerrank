#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    del ar[k]
    part = sum(ar)/2
    if (part == b):
      return ("Bon Appetit")
    else:
      return int(abs(part - b))
    # Complete this function

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
