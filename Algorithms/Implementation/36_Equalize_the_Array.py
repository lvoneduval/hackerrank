n  = int(input())
a = input().split(' ')
a = [int(b) for b in a]
count = [0] * (max(a) + 1)
for i in range(max(a) + 1):
  count[i] = a.count(i)
print(sum(count) - max(count))
