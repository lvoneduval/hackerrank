#!/bin/python3

import sys


n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]
for i in range(n1 - 2, -1, -1):
  h1[i] += h1[i + 1]
for i in range(n2 - 2,-1, -1):
  h2[i] += h2[i + 1]
for i in range(n3 - 2,-1, -1):
  h3[i] += h3[i + 1]
s1,s2,s3 = map(set,[h1,h2,h3])
res = s1 & s2 & s3
if (res):
  print(max(res))
else:
  print(0)
