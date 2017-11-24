nT = input()
nT = int(nT)
for i in range(nT):
  n = input()
  a = input()
  b = input()
  n,a ,b = [int(n),int(a),int(b)]
  i = 0
  c = []
  while(i < n):
    tmp = i * a + (n - 1 - i) * b
    if not(tmp in c):
      c.append(tmp)
    i += 1
  c.sort()
  print(" ".join(str(x) for x in c))
