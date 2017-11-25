import numpy
n,m,p = map(int,input().split(" "))
arr1 = numpy.array([list(map(int,input().split(" "))) for _ in range(n)])
arr2 = numpy.array([list(map(int,input().split(" "))) for _ in range(m)])
print(numpy.concatenate((arr1,arr2),axis=0))
