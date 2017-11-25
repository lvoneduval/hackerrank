import re
n = int(input())
regs = [r'^[4-6]([0-9]{15}|[0-9]{3}(-[0-9]{4}){3})$']  

for _ in range(n):
  s = input()
  sorte = "".join(sorted(s, key = lambda x: x.isdigit()))
  if (all(re.search(r,s) for r in regs) and not(bool(re.search(r"([\d])\1\1\1",sorte)))):
    print("Valid")
  else:
    print("Invalid")
