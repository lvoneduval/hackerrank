import collections
n,data= int(input()) , collections.namedtuple('data', input())
res = sum([float(data(*input().split()).MARKS) for i in range(n)])
print("{0:.2f}".format(res/n))  
