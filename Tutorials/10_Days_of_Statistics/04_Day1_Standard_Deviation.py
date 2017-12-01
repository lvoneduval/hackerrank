
n = int(input())
l = list(map(int,input().split(" ")))
moy = sum(l)/n
l = sum([(i-moy) ** 2 for i in l]) / n
print("{0:.1f}".format(l ** (1/2)))
