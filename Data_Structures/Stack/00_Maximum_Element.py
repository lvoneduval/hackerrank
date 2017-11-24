n = int(input())
l = []
class stacknode(object):
    def __init__(self, value=None, dis=0):
      self.value = value
      self.dis = dis
maxi = stacknode(-(2**63))
for _ in range(n):
  s = list(map(int,input().split(" ")))
  if (s[0] == 1):
    if (s[1] > maxi.value):
      l.append(maxi)
      maxi = stacknode(s[1])
    else:
      maxi.dis += 1
  elif (s[0]== 2):
    maxi.dis -= 1
    if (maxi.dis == -1):
      maxi = l.pop()
  else :
    print(maxi.value)
