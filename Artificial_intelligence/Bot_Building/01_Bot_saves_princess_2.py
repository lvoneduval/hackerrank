#
def findPrincess(n, grid):
  pos = [0 , 0]
  while (pos[0] < n):
    pos[1] = 0
    while (pos[1] < n):
      if (grid[pos[0]][pos[1]] == 'p'):
        return(pos)
      pos[1] += 1
    pos[0] += 1
    
def nextMove(n,r,c,grid):
  pos = findPrincess(n, grid)
  ret = ""
  if (r > pos[0]):
    ret = "UP"
  elif (r < pos[0]):
    ret = "DOWN"
  elif (c > pos[1]):
    ret = "LEFT"
  else :
    ret = 'RIGHT'
  return ret

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
