#!/bin/python3

import sys

def leftRotation(a, d):
  lena = len(a)
  return(a[d % lena:] + a[:d % lena])
    # Complete this function

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (*result)
