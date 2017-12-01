from math import factorial
p = 12/100
q = 1 - p
f10 = factorial(10)
def comb (x,n):
  return(factorial(10)/ (factorial(x) * factorial(n - x)))
def b (x,n,p):
  q = 1 - p
  return (comb(x,n) * (p ** x) * (q ** (n-x))) 
  
print("{0:.3f}".format(sum([b(i,10,p) for i in range(3)])))
print("{0:.3f}".format(sum([b(i,10,p) for i in range(2,11)])))
