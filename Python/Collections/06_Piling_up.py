from collections import deque
q = int(input())
for _ in range(q):
  n = int(input())
  d = deque(map(int,input().split(" ")))
  last = 2**63
  b = True
  while (d and b):
    if (d[-1] >= d[0]  and d[-1] <= last):
      last = d.pop()
    elif (d[0] > d[-1] and d[0] <= last):
      last = d.popleft()
    else :
      b = False
  print("Yes" if b else "No")
  
