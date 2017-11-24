#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
  tmp = head
  lenl = 0
  while (tmp):
    tmp = tmp.next
    lenl += 1
  position = lenl - position - 1
  while (head and position):
    head = head.next
    position -= 1
  return(head.data)
