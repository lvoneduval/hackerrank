n = int(input())
l = [int(a) for a in input().split(" ")]

tab = [0] * 100
for i in range(n):
  tab[l[i]] += 1
print(*tab)
