#!/bin/python3

import sys

def makingAnagrams(s1, s2):
    lens1 = len(s1)
    lens2 = len(s2)
    tab1= [0] * 26
    tab2= [0] * 26
    orda = ord("a")
    res = 0
    for i in range(0,lens1):
      tab1[ord(s1[i]) - orda] += 1
    for i in range(0,lens2):
      tab2[ord(s2[i]) - orda] += 1
    for i in range(26):
      res += abs(tab1[i] - tab2[i])
    return(res)
    # Complete this function


s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
