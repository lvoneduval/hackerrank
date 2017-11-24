n = int(input())
l = [int(i) for i in input().split(" ")]
for i in range(1, n):
  x = l[i]
  j = i
  while j > 0 and l[j-1] > x:
    l[j] = l[j-1]
    j = j - 1
  l[j] = x
  print(*l)
