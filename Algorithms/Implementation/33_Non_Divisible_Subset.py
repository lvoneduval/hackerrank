n , k = input().strip().split(' ')
n , k = [int(n), int(k)]
a = input().strip().split(' ')
a = [int(b) for b in a]
list_mod_k = [0] * k
result = 0
for i in a:
  list_mod_k[i % k] += 1

i = 1
while (i * 2 < k):
  result += max(list_mod_k[i], list_mod_k[k - i])
  i += 1
if (i * 2 == k and list_mod_k[i] != 0):
  result += 1
if (list_mod_k[0] != 0):
  result += 1
if (k == 0 or k == 1):
  result = 1

print(result)
