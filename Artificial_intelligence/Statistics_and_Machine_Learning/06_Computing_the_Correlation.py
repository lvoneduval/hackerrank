import math

mth = []
msq = []
phy = []
psq = []
chm = []
csq = []
n = 0

n = int(input())
for i in range(n):
    m,p,c = map(int,input().split())
    mth.append(m)
    phy.append(p)
    chm.append(c)
    msq.append(m * m)
    psq.append(p * p)
    csq.append(c * c)

def cor(x,y, xsq , ysq , n):
    XY = []
    sumx = sum(x) 
    sumy = sum(y)
    sumxs = sum(xsq)
    sumys = sum(ysq)
    for i in range(n):
        XY.append(x[i] * y[i])
    sumxy = sum(XY)
    det = (n * sumxy - sum(x) * sum(y))
    div = math.sqrt(n * sumxs - sumx ** 2) * math.sqrt(n * sumys - sumy ** 2)
    return(det/div)
print("{0:.2f}".format(cor(mth,phy,msq,psq,n)))
print("{0:.2f}".format(cor(phy,chm,psq,csq,n)))
print("{0:.2f}".format(cor(chm, mth,csq,msq,n)))
