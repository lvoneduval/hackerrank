#!/usr/bin/python3
from collections import deque
class Spot(object):
  def __init__(self,t,x,y,exp = 0,w = deque()):
    self.x = x
    self.y = y
    self.f = 0
    self.g = 0
    self.h = 0
    self.nei = []
    self.prev = None
    self.wall = 0 if t == '-' or t=='.' else 1 

  def addNei(self,grid,cols,rows):
    i = self.x
    j = self.y
    if (i < rows - 1):
      self.nei.append(grid[i + 1][j])
    if (j < cols - 1):
      self.nei.append(grid[i][j + 1])
    if (i > 0):
      self.nei.append(grid[i - 1][j])
    if (j > 0):
      self.nei.append(grid[i][j - 1])
  
def heuristic(cur,i):
  return(abs(cur.x - i.x) + abs(cur.y - i.y))

def Astar( r, c, p_r, p_c, f_r, f_c, grid):
  openSet = [grid[p_r][p_c]]
  closSet = []
  end = grid[f_r][f_c]
  while (openSet):
    winner = 0
    l_o = len(openSet)
    for i in range(l_o):
      if (openSet[i].f < openSet[winner].f):
        winner = i
    cur = openSet[winner]
    if (cur == end):
      break;
    del openSet[winner]
    closSet.append(cur)
    for i in cur.nei:
      if i in closSet or i.wall == 1:
        continue
      tempg = cur.g + 1
      if i in openSet:
        if (i.g >= tempg):
          i.g = tempg
        else:
          continue
      else:
        i.g = tempg
        openSet.append(i)
      i.h = heuristic(i,end)
      i.f = i.g + i.h
      i.prev = cur
  path = []
  temp = cur
  path.append(cur)
  while(temp.prev):
    path.append(temp.prev)
    temp = temp.prev
  return(path)

pacman_r, pacman_c = [ int(i) for i in input().strip().split() ]
food_r, food_c = [ int(i) for i in input().strip().split() ]
r,c = [ int(i) for i in input().strip().split() ]

grid = [[] for i in range(r)]
for i in range(0, r):
    l = input().strip()
    for j in range(c):
      grid[i].append(Spot(l[j],i,j))

for i in range(0,r):
  for j in range(0,c):
    grid[i][j].addNei(grid,c,r)
      
res = Astar(r, c, pacman_r, pacman_c, food_r, food_c, grid)
l_r = len(res)
print(l_r - 1)
for i in range(l_r):
  tmp = res[l_r - i - 1]
  print(tmp.x, tmp.y)
