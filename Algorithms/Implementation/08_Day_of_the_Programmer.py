#!/bin/python3

import sys

def solve(year):
    if (year == 1918):
      return("26.09.1918")
    elif (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))) or (year < 1918 and year % 4 == 0):
      return ("12.09.%d" % year)
    else:
      return ("13.09.%d" % year)
      
      
    # Complete this function

year = int(input().strip())
result = solve(year)
print(result)
