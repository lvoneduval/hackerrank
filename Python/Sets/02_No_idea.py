n,m = [int(a) for a in input().split(" ")]
arr = [int(a) for a in input().split(" ")]
A = set([int(a) for a in input().split(" ")])
B = set([int(a) for a in input().split(" ")])
res = sum((a in A) - (a in B) for a in arr )
print(res)
