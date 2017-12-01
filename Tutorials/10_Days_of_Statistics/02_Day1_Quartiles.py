def medianr (l):
  lenl = len(l)
  if (lenl % 2 == 0):
    median = (l[lenl//2 - 1] + l[lenl//2])/2
  else:
    median = l[lenl//2]
  return(int(median))

n = int(input())
l = list(map(int,input().split(" ")))
l.sort()
median = medianr(l)
L=list(filter(lambda x: x < median,l))
U=list(filter(lambda x: x > median,l))
print(medianr(L))
print(median)
print(medianr(U))
