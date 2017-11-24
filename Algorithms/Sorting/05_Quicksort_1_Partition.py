n = int(input())
l = [int(a) for a in input().split(" ")]
p = l[0]
left = []
right = []
equal = []
for i in range(0, n):
  if (l[i] < p):
    left.append(l[i])
  elif (l[i] > p):
    right.append(l[i])
  else :
    equal.append(l[i])
print(*left, *equal, *right)
