def wrapper(f):
    def fun(l):
      return (f(["+91 {} {}".format(n[-10:-5], n[-5:]) for n in l]))
        # complete the function
    return fun
