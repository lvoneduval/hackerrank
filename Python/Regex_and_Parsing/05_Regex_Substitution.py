import re
def replace (x):
  if x.group(0) == ("&&"):
    return("and")
  else:
    return("or")
  
i = int(input())
for _ in range(i):
  print(re.sub(r'(?<= )(\&\&|\|\|)(?= )',replace,input()))
