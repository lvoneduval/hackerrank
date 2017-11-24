#!/bin/python3

import sys

def super_reduced_string(s):
    l  = len(s)
    i = 0
    while i < l - 1:
      if (s[i] == s[i + 1]):
        del s[i + 1]
        del s[i]
        l -= 2
        i = 0
      else:
        i += 1
    return(s)
    # Complete this function

s = input().strip()
s = [a for a in s]
result = super_reduced_string(s)
print("".join([str(r) for r in result]) if result else "Empty String" )
