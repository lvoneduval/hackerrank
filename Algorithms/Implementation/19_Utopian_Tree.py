#!/bin/python3

import sys

def function(n):
    if (n == 0):
      return (1)
    elif (n % 2 == 0):
      return(function(n - 1) + 1)
    else :
      return(function(n - 1) * 2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(function(n))
