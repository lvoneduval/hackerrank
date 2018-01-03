import numpy

F,N = list(map(int, input().split(' ')))
a = 0.1
iteration = 100

feature = numpy.array([0 for i in range((F + 1) * N)], float)
feature.shape = (N, F + 1)

price = numpy.array([0 for i in range(N)], float)
price.shape = (N,1)

theta = numpy.array([1 for i in range(F + 1)], float)
theta.shape = (F + 1, 1)

for i in range (N):
	tmp = list(map(float,input().split(' ')))
	price[i] = [tmp[F]]
	tmp2 = tmp[:-1]
    	tmp2.insert(0,1)
        feature[i] = tmp2

ft = numpy.transpose(feature)
tet = numpy.dot(numpy.dot(numpy.linalg.inv(numpy.dot(ft, feature)), ft), price)

T = int(input())

for i in range(T):
    tmp = list(map(float,input().split(' ')))
    tmp.insert(0,1)
    tmp2 = numpy.array(tmp,float)
    print("{0:.3f}".format(numpy.dot(tmp,tet)[0]))
