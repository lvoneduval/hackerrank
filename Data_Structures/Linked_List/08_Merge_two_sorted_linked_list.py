"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def min_head(headA,headB):
  if(not headA):
    return(headB,headA,headB.next)
  if(not headB):
    return(headA,headA.next,headB)
  if(headA.data > headB.data):
    return(headB,headA,headB.next)
  else:
    return(headA,headA.next,headB)
    
def MergeLists(headA, headB):
  if (not headA):
    return(headB)
  if (not headB):
    return(headA)
  new,headA,headB = min_head(headA, headB)
  tmp = new
  while(headA or headB):
    tmp.next,headA,headB = min_head(headA, headB)
    tmp = tmp.next
  return(new)
