from itertools import combinations

l, n = input().split(" ")
n = int(n)
l = list(l)
l.sort()
res = []
for i in range(1,n + 1):
  if i > 1:
    tmp = list(combinations(l,i))
    tmp = ["".join(a) for a in tmp]
  else :
    tmp = list(l)
  tmp.sort()
  res += tmp
for i in res:
  print(i)
