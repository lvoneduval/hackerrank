def next_permutation(arr):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True

def nextlex(s):
  i = len(s) - 1
  if (i == 0):
    return(s)
  j = i
  while (i > 0 ):
    if (s[i] > s[i - 1]):
      break
    i -= 1
  i -=1
  while(j >= i + 1):
    if (s[j] > s[i]):
      break;
    j -= 1
      
  tmp = s[i]
  s[i] = s[j]
  s[j] = tmp
  s[i + 1:] = reversed(s[i + 1:])
  return(s)

n = int(input())
for i in range(n):
  s = str(input())
  res = list(s)
  print(''.join(res) if next_permutation(res) else "no answer")
