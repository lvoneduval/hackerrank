"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys
def inOrder(root):
  if (not root):
    return 
  if (root.left):
    inOrder(root.left)
  sys.stdout.write(str(root.data )+ " ")
  if (root.right):
    inOrder(root.right)
