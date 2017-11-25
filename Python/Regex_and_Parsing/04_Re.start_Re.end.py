import re
s = input()
len(s)
exp = re.compile(input())
m = exp.search(s)
if not (m):
  print("(-1, -1)")
else:
  while(m):
    print("({}, {})".format(m.start(),m.end() - 1))
    m = exp.search(s,m.start() + 1)
