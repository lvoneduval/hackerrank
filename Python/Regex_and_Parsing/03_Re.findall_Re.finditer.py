import re
expR = r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiouAEIOU]{2,})[qwrtypsdfghjklzxcvbnm]'
l = re.findall(expR,input())
if l:
  print(*l,sep = "\n")
else:
  print(-1)
