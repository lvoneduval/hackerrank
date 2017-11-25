import re
exp = re.compile('^[7-9][0-9]{9}$')
n = int(input())
for _ in range(n):
  print("YES" if bool(exp.search(input())) else "NO")
