#!/usr/bin/python
def findPrincess(n, grid):
  if (grid[0][0] == "p"):
    return([0, 0])
  elif (grid[0][n -1] == "p"):
    return([0,n -1])
  elif (grid[n - 1][0] == "p"):
    return([n -1, 0])
  else:
    return([n -1,n -1])

def displayPathtoPrincess(n,grid):
  pos_p = findPrincess(n, grid)
  pos_m = [(n - 1)/ 2, (n - 1)/2]
  while(pos_m[0] > pos_p[0]):
    print("UP")
    pos_m[0] -=1
  while(pos_m[0] < pos_p[0]):
    print("DOWN")
    pos_m[0] +=1
  while(pos_m[1] > pos_p[1]):
    print("LEFT")
    pos_m[1] -=1
  while(pos_m[1] < pos_p[1]):
    print("RIGHT")
    pos_m[1] +=1

#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
