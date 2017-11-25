from itertools import combinations_with_replacement
l,n = input().split(" ")
l = list(l)
l.sort()
n = int(n)
res = list(combinations_with_replacement(l,n))
for i in res:
  print("".join(i))
