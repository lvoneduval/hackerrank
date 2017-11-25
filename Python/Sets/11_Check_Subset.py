A = set(input().split())
l = True
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted. 
    B = set(input().split())
    l &= A > B
print(l)
