n = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
  com = input().split(" ")
  if (com[0] == "intersection_update"):
    tmp = set(map(int, input().split()))
    s &= tmp
  elif (com[0] == "update"):
    tmp = set(map(int, input().split()))
    s |= tmp
  elif (com[0] == "symmetric_difference_update"):
    tmp = set(map(int, input().split()))
    s ^= tmp
  elif (com[0] == "difference_update"): 
    tmp = set(map(int, input().split()))
    s -= tmp
print(sum(s)) 
