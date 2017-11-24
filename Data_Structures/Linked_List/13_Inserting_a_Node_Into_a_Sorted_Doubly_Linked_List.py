"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
  new = Node(data)
  if (not head):
    return(new)
  prev =  None
  tmp = head
  while (tmp and tmp.data < data):
    prev = tmp
    tmp = tmp.next
  if(prev):
    prev.next = new
  else:
    head = new
  new.prev = prev
  new.next = tmp
  if(tmp):
    tmp.prev = new
  return(head)
