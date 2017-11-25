from collections import OrderedDict
l = OrderedDict()
n = int(input())
for _ in range(n):
  inp = input().split(" ")
  inp,nb = " ".join(inp[0:-1]),int(inp[-1])
  l[inp] = l.get(inp,0) + nb
for i in l:
  print("{} {}".format(i,l[i]))
