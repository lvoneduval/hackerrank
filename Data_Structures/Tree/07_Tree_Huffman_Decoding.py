"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        
import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
  tmp = root
  lens = len(s) 
  i = 0
  while i < len(s):
    if not tmp.left and not tmp.right:
      sys.stdout.write(tmp.data)
      tmp = root
    elif s[i] == '1':
      i += 1
      tmp = tmp.right
    else:
      i += 1
      tmp = tmp.left  
  print(tmp.data)
   #Enter Your Code Here
