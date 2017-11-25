i , n = map(int,input().split(" "))
l =[]
for _ in range(n):
  l.append(list(map(float,input().split(" "))))
l = zip(*l)
for i in l:
  print("{0:.1f}".format(sum(i)/n))
