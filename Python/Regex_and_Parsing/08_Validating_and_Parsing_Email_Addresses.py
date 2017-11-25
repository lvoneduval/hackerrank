import re
n = int(input())
exp = re.compile('<[a-z0-9][\w._-]+@[a-z]+\.[a-z]{1,3}>')
for _ in range(n):
  s = input()
  if (bool(exp.search(s))):
    print(s)
