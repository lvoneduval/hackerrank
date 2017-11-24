#!/bin/python3

import sys

def f(clo, p_q, p_o, n):
  if(p_q[0] == p_o[0] and p_o[1] < p_q[1]):
    clo[0] = min(abs(p_o[1] - p_q[1]) - 1, clo[0])
  elif(p_q[0] == p_o[0] and p_o[1] > p_q[1]):
    clo[1] = min(abs(p_o[1] - p_q[1]) - 1, clo[1])
  elif(p_q[0] < p_o[0] and p_o[1] == p_q[1]):
    clo[2] = min(abs(p_o[0] - p_q[0]) - 1, clo[2])
  elif(p_q[0] > p_o[0] and p_o[1] == p_q[1]):
    clo[3] = min(abs(p_o[0] - p_q[0]) - 1, clo[3])
  elif(p_q[0] - p_o[0] == p_q[1] - p_o[1] and p_o[0] > p_q[0]):
    clo[4] = min(abs(p_o[0] - p_q[0]) - 1, clo[4])
  elif(p_q[0] - p_o[0] == p_q[1] - p_o[1] and p_o[0] < p_q[0]):
    clo[5] = min(abs(p_o[0] - p_q[0]) - 1, clo[5])
  elif(p_q[0] - p_o[0] == -(p_q[1] - p_o[1]) and p_o[0] > p_q[0]):
    clo[6] = min(abs(p_o[0] - p_q[0]) - 1, clo[6])
  elif (p_q[0] - p_o[0] == -(p_q[1] - p_o[1]) and p_o[0] < p_q[0]):
    clo[7] = min(abs(p_o[0] - p_q[0]) - 1, clo[7])
  return(clo)

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
pos_q = [rQueen, cQueen]
closest=[n] * 8
for i in range(n + 2):
    pos_o = [0,i]
    closest = f(closest, pos_q, pos_o, n)
    pos_o = [i,0]
    closest = f(closest, pos_q, pos_o, n)
    pos_o = [i,n+1]
    closest = f(closest, pos_q, pos_o,n)
    pos_o = [n + 1, i]
    closest = f(closest, pos_q, pos_o,n)

for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    pos_o = [int(rObstacle),int(cObstacle)]
    closest = f(closest, pos_q, pos_o, n)
# your code goes here

print(sum(closest))
