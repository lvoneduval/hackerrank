"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""
import sys

def rightView(root):
  if (not root):
    return
  sys.stdout.write(str(root.data )+ " ")
  rightView(root.right)

def leftView(root):
  if (not root):
    return
  leftView(root.left)
  sys.stdout.write(str(root.data )+ " ")

def topView(root):
  if (not root):
    return
  leftView(root.left)
  sys.stdout.write(str(root.data )+ " ")
  rightView(root.right)
  #Write your code here
