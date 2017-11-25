def merge_the_tools(string, k):
  lens = len(string)
  l = []
  i = 0
  while i < lens:
    l.append(string[i:i + k])
    i += k
  for h in l:
    dictmp = {}
    t = [dictmp.setdefault(e,e) for e in h if e not in dictmp]
    print("".join(t))
    # your code goes here
