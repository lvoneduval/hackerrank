import os

def isescape(view):
  if (view[0][1] == 'e'):
    return(4)
  elif (view[1][0] == 'e'):
    return(2)
  elif (view[2][1] == 'e'):
    return(3)
  elif (view[1][2] == 'e'):
    return(1)
  else:
    return (0)
fn = "dirtdi"
def tkt(view):
  if view == ["---","---","--#"] and not os.path.exists(fn):
    fh = open(fn, "w")
    fh.writelines("okokok")
    fh.close()
    return(1)
  else:
    return(0)
action = ["RIGHT","LEFT",  "DOWN", "UP"]

n = input()
view = [input() for i in range(3)]
esc = isescape(view)
if (esc):
  res = esc - 1
elif(tkt(view)):
  res = 0
elif (view[0][1] == '-'):
  res = 3
elif (view[1][0] == '-'):
  res = 1
elif (view[2][1] == '-'):
  res = 2
else:
  res = 0
print(action[res])
