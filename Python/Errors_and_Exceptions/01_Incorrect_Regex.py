import re
n = int(input())
for _ in range(n):
  try:
    re.compile(input())
  except re.error:
    print("False")
    continue
  print("True")
