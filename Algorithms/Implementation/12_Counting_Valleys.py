#!/bin/python3

import sys

result = 0;
n = int(input().strip())
way = input()
altitude = 0
for i in way:
  if (i == "U"):
    altitude += 1
    if (altitude == 0):
      result += 1
  else:
    altitude -= 1
print (result)
