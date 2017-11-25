from itertools import product 
K,M = map(int,input().split(" "))
maxi = 0

def f (x):
  return(sum((i ** 2 for i in x))) % M

l = [map(int,input().split(" ")[1:]) for i in range(K)]
print(max(map(f,(product(*l)))))
