import sys
p = int(input())
q = int(input())
b = 0
for i in range(p, q + 1):
  s = str(i * i)
  l = len(s)
  if (s == '1'):
    sys.stdout.write(s)
    b += 1
  if (l > 1):
    m = len(s)//2
    k = s[: m]
    j = s[-(l-m): ]
    sum = int(k) + int(j)
    if (sum == i):
      if (b):
        sys.stdout.write(' ')
      sys.stdout.write(str(i))
      b += 1
if (not b):
  print("INVALID RANGE")
