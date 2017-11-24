def findpos(V, min_c, max_c, arr):
  cur = (min_c + max_c)//2
  if (min_c == max_c - 1):
    return(min_c if arr[min_c] == V else max_c)
  if (arr[cur] == V):
    return(cur)
  elif (arr[cur] > V):
    return(findpos(V, min_c, cur, arr))
  else:
    return(findpos(V, cur, max_c, arr))

V = int(input())
n = int(input())
ar = input().split(" ")
ar = [int(a) for a in ar]
print(findpos(V, 0, n - 1, ar))
