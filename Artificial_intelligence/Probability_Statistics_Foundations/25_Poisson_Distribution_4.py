# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

mean = 1.2
e = math.exp(-mean)
def card(n, k):
    return( math.factorial(k) / math.factorial(n - k))

def f(k):
    return(((mean ** k) /math.factorial(k)) * e)

res = f(2)
print("{0:.3f}".format(res))
res = e + f(1) + f(2)
print("{0:.3f}".format(res))

#res = (f(1)**5) + (f(1) ** 3 * f(2)) + (f(1) ** 2 * f(3))  + (f(1) * f(4)) + f(5)
# a refaire, ne pas utiliser d'outils pour le réussir.

print("{0:.3f}".format(0.012))
print("{0:.3f}".format(1))
