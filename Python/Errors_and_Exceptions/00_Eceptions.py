n = int(input())
for _ in range(n):
  l = input().split(" ")
  try:
    l = list(map(int,l))
  except  ValueError as e:
      print("Error Code:",e)
      continue 
  try:
    print(l[0]//l[1])
  except ZeroDivisionError as e:
    print ("Error Code:",e)
