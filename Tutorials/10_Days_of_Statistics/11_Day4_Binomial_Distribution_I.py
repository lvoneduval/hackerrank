from math import factorial
def coef(n,k):
  return(factorial(n)/(factorial(k)* factorial(n - k)))

def prob(i,n,p,q):
  return(coef(n,i) * (p ** i) * (q ** (n - i)))
  
p = 1.09/2.09
q = 1 - p

n = 6
p3 = 0
for i in range(3,n+1):
  p3 += prob(i,n,p,q)
print("{0:.3f}".format(p3))
