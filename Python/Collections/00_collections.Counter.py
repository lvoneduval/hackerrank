from collections import Counter

n = int(input())
l = list(map(int,input().split(" ")))
counter = Counter(l)
itera = int(input())
money = 0
for _ in range(itera):
  n,cost = map(int,input().split(" "))
  if(counter[n] > 0):
    money += cost
    counter[n] -= 1
print(money)
