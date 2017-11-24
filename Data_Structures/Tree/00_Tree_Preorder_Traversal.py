"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
import sys
def preOrder(root):
  if (not root):
    return 
  sys.stdout.write(str(root.data )+ " ")
  if (root.left):
    preOrder(root.left)
  if (root.right):
    preOrder(root.right)
    #Write your code here

