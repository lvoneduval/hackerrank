#!/bin/python3

import sys

def minSteps(n, B):
    return(B.count('010'))
    # Complete this function

n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)
