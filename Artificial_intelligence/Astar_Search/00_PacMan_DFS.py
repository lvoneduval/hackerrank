#!/usr/bin/python3
from collections import deque
class Graph(object):
  def __init__(self,t,x,y,exp = 0):
    self.x = x
    self.y = y
    self.v = 0 if t == '-' or t == '.' else 1
    self.e = exp

def dfs( r, c, p_r, p_c, f_r, f_c, grid):
  l = deque()
  l.appendleft(grid[p_r][p_c])
  way = deque()
  exp = []
  while(1):
    continu = 0
    tmp = l[0]
    tmp.v = 1
    exp.append(tmp)
    way.appendleft(tmp)
    p_r, p_c = tmp.x, tmp.y
    if (p_r == f_r and p_c == f_c):
      break
    if (p_r > 0 and grid[p_r - 1][p_c].v == 0 and grid[p_r - 1][p_c].e == 0):
      grid[p_r - 1][p_c].e = 1
      l.appendleft(grid[p_r - 1][p_c])
      continu = 1
    if (p_c > 0 and grid[p_r][p_c - 1].v == 0 and grid[p_r][p_c - 1].e == 0):
      grid[p_r][p_c - 1].e = 1
      l.appendleft(grid[p_r][p_c - 1])
      continu = 1
    if (p_c < c - 1 and grid[p_r][p_c + 1].v == 0 and grid[p_r][p_c + 1].e == 0):
      grid[p_r][p_c + 1].e = 1
      l.appendleft(grid[p_r][p_c + 1])
      continu = 1
    if (p_r < r - 1 and grid[p_r + 1][p_c].v == 0 and grid[p_r + 1][p_c].e == 0):
      grid[p_r + 1][p_c].e = 1
      l.appendleft(grid[p_r + 1][p_c])
      continu = 1
    if (continu == 0):
      while(l[0] == way[0]):
        l.popleft()
        tmp = way.popleft()
        tmp.v = 0
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
