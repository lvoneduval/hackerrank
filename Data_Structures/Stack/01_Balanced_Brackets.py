#!/bin/python3

import sys

op = "({["
cl = ")}]"
dic = {a:b for a,b in zip(cl,op)}
def isBalanced(s):
  l = []
  for i in s:
    if i in op:
      l.append(i)
    elif i in cl:
      if (not l or l.pop() != dic[i]):
        return(False)
    else:
      return False
  return(not l)
    # Complete this function

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print("YES" if result else "NO")
