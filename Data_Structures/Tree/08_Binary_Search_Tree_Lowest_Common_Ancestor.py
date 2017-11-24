"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
  tmp = root
  while (1):
    if (tmp.data > v1 and tmp.data > v2):
      tmp = tmp.left
    elif (tmp.data < v1 and tmp.data < v2):
      tmp = tmp.right
    else:
      return(tmp)
  #Enter your code here
