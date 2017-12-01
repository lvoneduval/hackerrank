import operator
n = input()
l = list(map(int,input().split()))
w = list(map(int,input().split()))
print("{0:.1f}".format(sum(map(operator.mul,l,w))/sum(w)))
