#!/bin/python

import sys

def alternatingCharacters(s):
    lens = len(s)
    res = 0
    for i in range(1, lens):
      if (s[i] == s[i - 1]):
        res += 1
    return(res)
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = alternatingCharacters(s)
    print(result)
