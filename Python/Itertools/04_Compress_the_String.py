from itertools import groupby
l = list(map(int,list(input())))
res = [(len(list(c)),k)  for k, c in groupby(l)]
print(*res
