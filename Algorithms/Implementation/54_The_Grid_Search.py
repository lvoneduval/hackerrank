#!/bin/python3

import sys

def search(G, S, P,s):
  R,C = S
  r,c = s
  for I in range(R - r + 1):
    for J in range(C - c + 1):
      i = 0
      j = 0
      while (i < r and G[I + i][J + j] == P[i][j]):
        j +=1
        if (j == c):
          i += 1
          j = 0
      if(i == r):
        return("YES")
  return("NO")

t = int(input().strip())
for a0 in range(t):
  R,C = input().strip().split(' ')
  R,C = [int(R),int(C)]
  G = []
  G_i = 0
  for G_i in range(R):
    G_t = str(input().strip())
    G.append(G_t)
  r,c = input().strip().split(' ')
  r,c = [int(r),int(c)]
  P = []
  P_i = 0
  for P_i in range(r):
    P_t = str(input().strip())
    P.append(P_t)
  print(search(G,[R,C], P, [r,c]))
