from itertools import permutations
s,n = input().split(" ")
n = int(n)
l = list(permutations(s,n))
l = sorted(set(l))
for i in l:
  print("".join(i))
