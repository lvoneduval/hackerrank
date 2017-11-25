s = list(map(int,list(input())))
s = [(a + 1)%10 for a in s]
print("".join((str(a) for a in s)))
