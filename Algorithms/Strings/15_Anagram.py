#!/bin/python3

import sys

def anagram(s):
    lens = len(s)
    tab1= [0] * 26
    tab2= [0] * 26
    orda = ord("a")
    res = 0
    if (lens % 2):
      return(-1)
    lens = lens//2
    for i in range(0,lens):
      tab1[ord(s[i]) - orda] += 1
      tab2[ord(s[i + lens])- orda] += 1
    for i in range(26):
      res += abs(tab1[i] - tab2[i])
    return(int(res/2))
    # Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
