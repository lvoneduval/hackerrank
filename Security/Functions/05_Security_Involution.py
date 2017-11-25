n = int(input())
l = list(map(int,input().split(" ")))
b = True
for i in range(1,n + 1):
  if (l[l[i - 1] - 1] != i):
    b = False
    break
print("YES" if b else "NO")
