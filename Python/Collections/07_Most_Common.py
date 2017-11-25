#!/bin/python3
from collections import Counter
from operator import itemgetter
import sys

if __name__ == "__main__":
    s = input().strip()
    s = Counter(s).most_common()
    s = sorted(Counter(s),key = lambda x :(-x[1],x[0]))[:3]
    for i in s:
      print("{} {}".format(i[0],i[1]))
