import math

X = (15, 12,  8,  8,  7,  7,  7,  6, 5, 3)
Y = (10, 25, 17, 11, 13, 17, 20, 13, 9, 15)

l = len(X)
XY = []
Xsq = []
Ysq = []
for i in range(l):
    XY.append(X[i] * Y[i])
    Xsq.append(X[i] * X[i])
    Ysq.append(Y[i] * Y[i])

res = (l * sum(XY) - sum(X) * sum(Y))/ math.sqrt((l * sum(Xsq) - sum(X) * sum(X)) * (l * sum(Ysq) - sum(Y) * sum(Y)))
print("{0:.3f}".format(res))
