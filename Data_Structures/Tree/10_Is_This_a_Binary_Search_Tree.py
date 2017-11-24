""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
  l1 = []
  res = []
  cur = root
  while (l1 or cur):
    while(cur):
      l1.append(cur)
      cur = cur.left
    if (not cur and l1):
      cur = l1.pop()
      res.append(cur.data)
      cur = cur.right
  if (res == sorted(res) and len(res) == len(set(res))):
    return(True)
  else:
    return(False)
