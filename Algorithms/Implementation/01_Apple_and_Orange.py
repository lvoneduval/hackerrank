#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

for i, el in enumerate(apple):
   apple[i] += a
for i, el in enumerate(orange):
   orange[i] += b
print(len([nb for nb in apple if (nb >= s and nb <= t)]))
print(len([nb for nb in orange if (nb >= s and nb <= t)]))
