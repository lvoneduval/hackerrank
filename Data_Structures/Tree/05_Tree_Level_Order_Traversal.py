"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys
from collections import deque
def levelOrder(root):
    if (not root):
      return
    l = deque([root])
    while (l):
      tmp = l.popleft()
      sys.stdout.write(str(tmp.data )+ " ")
      if (tmp.left):
        l.append(tmp.left)
      if (tmp.right):
        l.append(tmp.right)
    #Write code Here
