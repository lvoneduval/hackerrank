#!/usr/bin/python

# Head ends here
def findclosest(posr,posc,board):
  mindis = 300
  res = [-1,-1]
  for i in range(len(board)):
    for j in range(len(board[i])):
      if (board[i][j] == "d" and (mindis > abs(i - posr) + abs(j - posc))):
        mindis = abs(i - posr) + abs(j - posc)
        res = [i,j]
  return(res)

def next_move(posr, posc, board):
    pos = findclosest(posr,posc,board)
    if (posr > pos[0]):
      print("UP")
    elif (posr < pos[0]):
      print("DOWN")
    elif (posc < pos[1]):
      print("RIGHT")
    elif (posc > pos[1]):
      print("LEFT")
    else :
      print("CLEAN")
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
