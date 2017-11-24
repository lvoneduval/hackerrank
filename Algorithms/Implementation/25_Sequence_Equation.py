n = int(input())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
for el_a in range(n):
  print(a.index(a.index(el_a + 1) + 1) + 1)
