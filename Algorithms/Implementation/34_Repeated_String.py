#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())
print(int(n / len(s)) * s.count('a') + s[:n % (len(s))].count('a'))
