X = (15,12,8,8,7,7,7,6,5,3)
Y = (10, 25, 17, 11, 13, 17, 20, 13, 9, 15)

l = len(X)

x_mean = sum(X) / l
y_mean = sum(Y) / l

XY = []
Xsq = []
for i in range(l):
    XY.append(X[i] * Y[i])
    Xsq.append(X[i] * X[i])
xy_mean = sum(XY) / l
xsq_mean = sum(Xsq) / l

res = (x_mean * y_mean - xy_mean)/(x_mean * x_mean - xsq_mean)
print("{0:.3f}".format(res))
