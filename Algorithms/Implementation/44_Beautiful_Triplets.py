import sys
n, d= input().split(" ")
n, d = [int(n) , int(d)]
a = input().split(" ")
a = [int(b) for b in a]
a.sort()
count = 0
for i in range(n):
  count += (a[i] + d in a) and (a[i] + 2 * d in a)      
print(count)
