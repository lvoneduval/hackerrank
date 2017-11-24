#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
s = [str(a) for a in s]
k = int(input().strip())
for i in range(n):
  if(s[i].isalpha()):
    if(s[i].islower()):
      s[i] = chr(((ord(s[i]) - ord('a')) + k) % 26 + ord('a'))
    else:
      s[i] = chr(((ord(s[i]) - ord('A')) + k) % 26 + ord('A'))
print("".join([str(a) for a in s]))
