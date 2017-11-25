import re
n = int(input())
regs = [r'^[a-zA-Z0-9]{10}$',r'[A-Z]{2,}',r'[0-9]{3,}']
for _ in range(n):
  s = "".join(sorted(input()))
  if (all(re.search(r,s) for r in regs) and not re.search(r'(.).*\1',s)):
    print("Valid")
  else:
    print("Invalid")
