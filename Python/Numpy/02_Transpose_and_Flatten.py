import numpy
n,m = map(int,input().split(" "))
l = []
for _ in range(n):
  l.append(list(map(int,input().split(" "))))
l = numpy.array(l)
print(numpy.transpose(l))
print(l.flatten())
