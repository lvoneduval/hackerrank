#!/bin/python3

import sys

def solve(n, p):
    end = int (n / 2)
    g = int (p/2)
    return min(end - g, g) 
    # Complete this function

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
