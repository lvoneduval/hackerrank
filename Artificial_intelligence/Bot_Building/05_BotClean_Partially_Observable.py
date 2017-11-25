import os
fn = 'dirtyFile'
def findclosest(posr,posc,board,tab):
  mindis = 300
  for i in range(posr -1, posr + 2):
    for j in range(posc -1, posc + 2):
      if (i >= 0 and i < 5 and j >= 0  and j < len(board[0]) and board[i][j] != 'd' and  [i , j] in tab):
        tab.remove([i, j])
  lent = len(tab)
  for i in range(lent):
    tmp = abs(posr - tab[i][0]) + abs(posc - tab[i][1])
    if (tmp) < mindis:
      mindis = tmp
      tmp1 = i
  res = tab[tmp1]
  if (board[posr][posc] == 'd'):
    del tab[tmp1]
  fh = open(fn, "w")
  fh.writelines("\n".join([" ".join([str(i) for i in tmp]) for tmp in tab]))
  fh.close()
  return(res)

def next_move(posr, posc, board):
    action = ["UP", "RIGHT", "DOWN", "LEFT", "CLEAN"]
    if (os.path.exists(fn)):
      fh = open(fn, "r")
      tmp = fh.readlines()
      tab = [list(map(int,i.split(" "))) for i in tmp]
      fh.close()
    else:
      lenb = len(board[0])
      tab = []
      for i in range(5):
        for j in range(lenb):
          tab.append([i , j])
      fh = open(fn, "w")
      fh.writelines("\n".join([" ".join([str(i) for i in tmp]) for tmp in tab]))
      fh.close()
    pos = findclosest(posr,posc,board,tab)
    if (posr > pos[0]):
      res = 0
    elif (posc < pos[1]):
      res = 1
    elif (posr < pos[0]):
      res = 2
    elif (posc > pos[1]):
      res = 3
    elif board[posr][posc] == 'd':
      res = 4
    print(action[res])

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)
