n = int(input())
l = [int(a) for a in input().split(" ")]
res = 0
for i in range(1 ,n):
  x = l[i]
  j = i
  while j > 0 and l[j - 1] > x:
    l[j] = l[j - 1]
    j -= 1
  if (l[j] != x):
    res += i - j
  l[j] = x
print(res)
