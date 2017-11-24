#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = int((input().strip()), 2)
   topic.append(topic_t)

c = [0] * (m + 1)
for i in range(n - 1):
  for j in range(i + 1, n):
    l = 0
    l = bin(topic[i] | topic[j]).count("1")
    c[l] += 1
l = m
while (l > 0 and c[l] == 0):
  l -= 1
print(l)
print(c[l])
