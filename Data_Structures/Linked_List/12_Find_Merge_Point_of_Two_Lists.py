"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
  curA = headA
  curB = headB
  
  while (curB):
    tmp = curB
    curB = curB.next
    tmp.next = None
  while(curA.next):
    curA = curA.next
  return (curA.data)
