r,c,n =[int(a) for a in input().split(" ")]
g = []
e = []
g_= []
f = []
for a in range(r):
  line = str(input())
  f.append([-2 if d== "." else 1 for d in line])
  g_.append(["O"] * c)
  g.append(line)
  line = str("O" * c)
  e.append(line)
  
if (n % 2 == 0 and n):
  g = e
elif (n == 0 or n == 1):
  g = g
else:
  if ((n - 1)% 4 == 0):
    n = 5
  else:
    n = 3
  while (n):
    for i in range(r):
      for j in range(c):
        f[i][j] += 1
        if (f[i][j] == 3):
          if(i > 0):
            f[i - 1][j] = -1
          if(j > 0):
            f[i][j - 1] = -1
          if (i < r - 1 and f[i + 1][j] != 2):
            f[i + 1][j] = -2
          if (j < c - 1 and f[i][j + 1] != 2):
            f[i][j + 1] = -2
          f[i][j] = -1
    n -= 1
  for i in range(r):
    g[i] = "".join(["O" if b > 0 else "." for b in f[i]])
for d in g:
  print(d)
