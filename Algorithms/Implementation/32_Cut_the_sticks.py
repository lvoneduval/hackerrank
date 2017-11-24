#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while (arr):
  print(len(arr))
  arr = [a for a in arr if (a != min(arr))]
