#!/bin/python3

import sys

def getTotalX(a, b):
    x = 0
    # Complete this function
    r = range(1,101)
    for el in r:
      if (len(a) == len([nb for nb in a if (el % nb) == 0]) and len(b) == len([nb for nb in b if (nb % el) ==0])):
        x+= 1
    return(x)
  
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
