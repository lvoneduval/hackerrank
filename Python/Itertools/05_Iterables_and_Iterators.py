n = int(input())
l = input().split(" ")
ch = int(input())
res = 1
k = l.count('a')
for i in range(ch):
  p = 1 - (k/(n - i))
  res *= p
print("{0:.4f}".format(1 - res))
