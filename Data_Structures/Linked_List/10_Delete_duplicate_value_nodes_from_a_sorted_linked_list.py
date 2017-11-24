"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
  if (not head or not head.next):
    return head
  tmp = head
  while (tmp.next):
    if tmp.data == (tmp.next).data:
      tmp.next = tmp.next.next
    else:
      tmp = tmp.next
  return (head)
