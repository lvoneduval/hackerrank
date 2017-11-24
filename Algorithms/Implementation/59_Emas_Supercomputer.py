r,c = (int(a) for a in input().split(" "))
m = []
for i in range(r):
  tmp = input()
  tmp = [0 if a == "G" else - 1 for a in tmp]
  m.append(tmp)

pos = []
for i in range(1 ,r - 1):
  for j in range (1, c - 1):
    size = 0
    if (m[i][j] == 0):
      while(i - size >= 0 and i + size < r and j - size >= 0 and j + size < c and m[i - size][j] != -1 and m[i + size][j] != -1 and m[i][j - size] != -1 and m[i][j + size] != -1):
        size += 1
      pos.append([i,j, size])
l = len(pos)
max_l = 0
for i in range(l):
  for j in range(i + 1,l):
    x1,y1,size1 = pos[i]
    x2,y2,size2 = pos[j]
    if ((((size1 - 1) * 4) + 1) * (((size2 - 1) * 4) + 1)) > max_l:
      b = 0
      for t in range(size1):
        m[x1 + t][y1] = -1
        m[x1 - t][y1] = -1
        m[x1][y1 + t] = -1
        m[x1][y1 - t] = -1
        q = 0
        while q < size2 and (m[x2 + q][y2] != -1 and m[x2 - q][y2] != -1 and m[x2][y2 + q] != -1 and m[x2][y2 - q] != -1):
          q += 1
        max_l = max(max_l, ((t * 4)  +1) * (((q - 1) * 4) + 1))
      for t in range(size1):
        m[x1 + t][y1] = 0
        m[x1 - t][y1] = 0
        m[x1][y1 + t] = 0
        m[x1][y1 - t] = 0
print(max_l)

