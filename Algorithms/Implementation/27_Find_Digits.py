#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(len([div for div in str(n) if(div != '0' and (n % int(div) == 0))]))
