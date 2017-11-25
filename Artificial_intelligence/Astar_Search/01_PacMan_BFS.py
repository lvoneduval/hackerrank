#!/usr/bin/python3
from collections import deque
class Graph(object):
  def __init__(self,t,x,y,exp = 0,w = deque()):
    self.x = x
    self.y = y
    self.v = 0 if t == '-' or t == '.' else 1
    self.e = exp
    self.w = w

def dfs( r, c, p_r, p_c, f_r, f_c, grid):
  l = deque()
  l.append(grid[p_r][p_c])
  way = deque()
  exp = []
  while(1):    
    tmp = l.pop()
    tmp.v = 1
    way = (tmp.w).copy()
    exp.append(tmp)
    way.appendleft(tmp)
    p_r, p_c = tmp.x, tmp.y
    if (p_r == f_r and p_c == f_c):
      break
    if (p_r > 0 and grid[p_r - 1][p_c].v == 0 and grid[p_r - 1][p_c].e == 0):
      grid[p_r - 1][p_c].e = 1
      grid[p_r - 1][p_c].w = way
      l.appendleft(grid[p_r - 1][p_c])
    if (p_c > 0 and grid[p_r][p_c - 1].v == 0 and grid[p_r][p_c - 1].e == 0):
      grid[p_r][p_c - 1].e = 1
      grid[p_r][p_c - 1].w = way
      l.appendleft(grid[p_r][p_c - 1])
    if (p_c < c - 1 and grid[p_r][p_c + 1].v == 0 and grid[p_r][p_c + 1].e == 0):
      grid[p_r][p_c + 1].e = 1
      grid[p_r][p_c + 1].w = way
      l.appendleft(grid[p_r][p_c + 1])
    if (p_r < r - 1 and grid[p_r + 1][p_c].v == 0 and grid[p_r + 1][p_c].e == 0):
      grid[p_r + 1][p_c].e = 1
      grid[p_r + 1][p_c].w = way
      l.appendleft(grid[p_r + 1][p_c])
  return (way,exp)

pacman_r, pacman_c = [ int(i) for i in input().strip().split() ]
food_r, food_c = [ int(i) for i in input().strip().split() ]
r,c = [ int(i) for i in input().strip().split() ]

grid = [[] for i in range(r)]
for i in range(0, r):
    l = input().strip()
    for j in range(c):
      grid[i].append(Graph(l[j],i,j))

res,exp = dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)
l_r = len(res)
l_e = len(exp)
print(l_e)
for i in range(l_e):
  tmp = exp[i]
  print(tmp.x, tmp.y)
print(l_r - 1)
for i in range(l_r):
  tmp = res[l_r - i - 1]
  print(tmp.x, tmp.y)
