n = int(input())
l = list(map(int,input().split(" ")))
for i in range(n):
  print(l[l[i] - 1])
