n = int(input())
l1 = set([int(a) for a in input().split(" ")])
n = int(input())
l2 = set([int(a) for a in input().split(" ")])
k = l1 ^ l2
for i in sorted(k):
  print(i)
