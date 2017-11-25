n = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
  com = input().split(" ")
  if (com[0] == "pop"):
    s.pop()
  elif (com[0] == "remove"):
    s.remove(int(com[1]))
  elif (com[0] == "discard"):
    s.discard(int(com[1]))
print(sum(s)) 
