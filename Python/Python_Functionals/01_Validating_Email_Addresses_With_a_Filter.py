import re
def fun(s):
  return(re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s))
    # return True if s is a valid email, else return False
