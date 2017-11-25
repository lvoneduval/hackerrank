from operator import itemgetter
n = int(input())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(n):
  orda = ord('A')
  key = input()
  s = list(input())
  
  lens = len(s)
  skey = set()
  for a in key:
    if not(a in skey):
      skey.add(a)
  skey = list(sorted(skey, key= key.index))
  nr = len(skey)
  
  for a in alpha:
    if not(a in skey):
      skey.append(a)

  tmp = [[] for a in range(nr)] 
  for i in range(26):
    tmp[i%nr].append(skey[i])
  tmp = sorted(tmp, key=lambda x:x[0])
  tmp ="".join(["".join(a) for a in tmp])
  for i in range(lens):
    if s[i] != ' ':
      s[i] = alpha[tmp.index(s[i])]
  print("".join(s))
