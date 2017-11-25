def miniswap(s):
  if (s.islower()):
    return(s.upper())
  else:
    return(s.lower())

def swap_case(s):
    return "".join((map(miniswap,s)))
