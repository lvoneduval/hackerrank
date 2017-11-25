from itertools import product

A = [int(a) for a in input().split(" ")]
B = [int(a) for a in input().split(" ")]
l = list(product(A,B))
print (*l)
# Enter your code here. Read input from STDIN. Print output to STDOUT
