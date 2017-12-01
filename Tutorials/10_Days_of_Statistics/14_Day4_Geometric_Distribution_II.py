p = 1/3
nb = 5
res = 0
for i in range(nb):
  res += ((1 - p)**i)*p
print("{0:.3f}".format(res))
