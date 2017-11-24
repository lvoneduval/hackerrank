"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):    
    if r is None:
        r = Node('')
        r.data = val
    elif val < r.data:
        if r.left is None:
            r.left = Node('')
            r.left.data = val
        else:
            insert(r.left, val)
    else:
        if r.right is None:
            r.right = Node('')
            r.right.data = val
        else:
            insert(r.right, val)
    return r
   #Enter you code here.
