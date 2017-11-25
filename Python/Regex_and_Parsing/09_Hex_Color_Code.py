import re
n = int(input())
b = False
for _ in range(n):
  cur = input()
  if(b):
    l = re.findall("#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}",cur)
    if (l):
      print(*l, sep="\n")
  elif re.search(r'{',cur):
        b=True
  if re.search(r'}',cur):
        b=False
