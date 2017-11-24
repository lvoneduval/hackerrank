n = int(input())
tab = [[] for i in range(100)]
res = ""
for _ in range(n):
  i, s = input().split(" ")
  i = int(i)
  if (_ < n//2):
    s = "-"
  tab[i].append(s)
for i in range(100):
  while(tab[i]):
    a = tab[i][0]
    if (res):
      res += " "
    res += a
    del tab[i][0]
print(res)
