import sys
class Node(object):
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def findnod(r,n):
  if (not r):
    return []
  res = []
  l1 = [r]
  l2 = []
  d = 0
  while (l1):
    tmp = l1[len(l1) - 1]
    l2.append(tmp)
    d += 1
    if (not tmp.left and not tmp.right):
      i = len(l1) - 1
      j = len(l2) - 1
      while (l2 and l1[i] == l2[j]):
        l1.pop()
        l2.pop()
        i -= 1
        j -= 1
        d -= 1
    else:
      if (d % n == 0):
        res.append(tmp)
      if (tmp.right):
        l1.append(tmp.right)
      if (tmp.left):
        l1.append(tmp.left)
  return(res)

def swapn(r):
  if (not r):
    return
  tmp = r.left
  r.left = r.right
  r.right = tmp
   
def inOrder(root):
  l1 = []
  cur = root
  while (l1 or cur):
    while(cur):
      l1.append(cur)
      cur = cur.left
    if (not cur and l1):
      cur = l1.pop()
      print(cur.data,end=" ")
      cur = cur.right
    
nb = int(input())
root = Node(1)
tmp = root
st = [root]
while(st):
  tmp = st[0]
  del st[0]
  l,r = map(int,input().split(" "))
  if (l != -1):
    tmp.left = Node(l)
    st.append(tmp.left)
  if (r != -1):
    tmp.right = Node(r)
    st.append(tmp.right)
nb = int(input())

for _ in range(nb):
  tofind = int(input())
  nodes = findnod(root,tofind)
  for node in nodes:
    swapn(node)
  inOrder(root)
  print("")
