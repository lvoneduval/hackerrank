# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
l = list(map(int,input().split(" ")))
l.sort()
lenl = len(l)
print("{:.1f}".format(sum(l)/lenl))
print("{:.1f}".format(l[lenl//2] if (lenl % 2 == 1) else (l[lenl//2 - 1] + l[lenl//2])/2))
print(sorted(Counter(l).most_common(),key = lambda x:(-x[1],x[0]))[0][0])
