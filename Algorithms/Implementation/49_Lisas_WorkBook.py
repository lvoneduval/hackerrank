n, k = input().split(" ")
t = input().split(" ")

n, k =[int(n), int(k)]
t = [int(tmp) for tmp in t]

cnt = 0
res = 0
for tmp in t:
  cmp = 0
  while (cmp < tmp):
    cnt += 1
    if (cnt > cmp and ((cnt <= cmp + k and cmp + k <= tmp) or (cmp + k > tmp and cnt <= cmp + (tmp %k)))):
      res += 1
    cmp += k
print(res)
