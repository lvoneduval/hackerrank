n = int(input())
for i in range(n):
  j = 0
  count = 0
  a = [int(a_tmp) for a_tmp in input().strip().split(' ')]
  while (j * j <= a[1]):
    count += (j * j >= a[0])
    j += 1
  print(count)
