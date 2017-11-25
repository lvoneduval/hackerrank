from collections import OrderedDict
n = int(input())
l = OrderedDict()
for _ in range(n):
  s = input()
  l[s] = l.get(s,0) + 1
print(len(l))
print(*[l[a] for a in l])
