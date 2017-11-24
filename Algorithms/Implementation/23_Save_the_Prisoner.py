#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    k = (m + s - 1)% n
    return (k if k != 0 else n)
    # Complete this function

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
