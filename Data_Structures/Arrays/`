#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    l = [0] * (n + 1)
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        l[a - 1] += k
        if (b < n + 1):
          l[b] -= k
    maxi = 0
    x = 0
    for i in range(n):
      x += l[i]
      if (maxi < x):
        maxi = x
    print(maxi)

