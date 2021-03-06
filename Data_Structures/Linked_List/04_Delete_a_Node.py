"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
  tmp = head
  if (not position):
    return head.next
  else :
    for _ in range(position - 1):
      tmp = tmp.next
    tmp.next = (tmp.next).next
    return(head)
