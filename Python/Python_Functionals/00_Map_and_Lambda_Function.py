cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
  f = [0]
  if n == 0: 
    return ([])
  elif n == 1:
    return(f)
  f.append(1)
  for i in range(2,n):
    f.append(f[i-2] + f[i-1])
  return(f)
    # return a list of fibonacci numbers
