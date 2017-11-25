def person_lister(f):
    def inner(people):
      return map(f, sorted(people, key=lambda x: int(x[2])))
        # complete the function
    return inner
