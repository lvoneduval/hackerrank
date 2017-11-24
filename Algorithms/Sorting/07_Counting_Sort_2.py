n = int(input())
l = [int(a) for a in input().split(" ")]
tab = [0] * 100
res = [0] * n
for i in range(n):
  tab[l[i]] += 1
j = 0
for i in range(100):
  while (tab[i] > 0):
    res[j] = i
    tab[i] -= 1
    j += 1
print(*res)
