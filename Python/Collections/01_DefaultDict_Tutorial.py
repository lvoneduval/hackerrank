from collections import defaultdict
n,m = map(int,input().split(" "))
A = defaultdict(list)
for i in range(n):
  A[input()].append(i + 1)
for _ in range(m):
  l = A[input()]
  if (l):
    print(*l)
  else:
    print(-1)
