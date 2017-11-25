import operator
if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    l = sorted(l,key=operator.itemgetter(1, 0),reverse=True)
    tmp = l[_ ]
    s = tmp[1]
    while(tmp[1] == s):
      tmp = l.pop()
    s = tmp[1]
    while(tmp[1] == s):
      print(tmp[0])
      if (l):
        tmp = l.pop()
      else:
        break
