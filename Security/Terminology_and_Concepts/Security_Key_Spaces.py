s = list(map(int,list(input())))
n = int(input())
s = [(a + n)%10 for a in s]
print("".join((str(a) for a in s)))
