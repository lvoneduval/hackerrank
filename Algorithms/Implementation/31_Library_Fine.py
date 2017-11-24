#!/bin/python3

import sys


d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]
count =  (y1 - y2 > 0) * 10000
count += (m1 - m2 > 0) * (m1 - m2) * 500 * (y1 - y2 == 0)
count += (d1 - d2 > 0) * (d1 - d2) * 15  * (y1 - y2 == 0) * (m1 - m2 == 0)
print(count)
