n,q = list(map(int,input().split(" ")))
l = [[] for i in range(n)]
last = 0
for _ in range(q):
  query,x,y = list(map(int,input().split(" ")))
  if (query == 1):
    l[(x ^ last) % n].append(y)
  elif (query == 2):
    last = l[(x ^ last) % n][y % len(l[(x ^last) % n])]
    print(last)
