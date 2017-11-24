n = int(input())
l = [int(a) for a in input().split(" ")]
toin = l[n - 1]
b = False
for i in range(n - 1, -1,-1):
  if (i == 0):
    l[i] = toin
  elif (l[i - 1] > toin):
    l[i] = l[i - 1]
  elif (l[i - 1] < toin):
    l[i] = toin
    b = True
  print(" ".join([str(a) for a in l]))
  if (b):
    break;
