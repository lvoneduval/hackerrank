import numpy
n,m = map(int,input().split(" "))
arr = numpy.array([list(map(int,input().split(" "))) for i in range(n)])
print(numpy.prod(numpy.sum(arr,axis=0)))
