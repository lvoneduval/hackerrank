#!/bin/python3

import sys
from datetime import datetime




def time_delta(t1, t2):
    return(abs((t1 -t2).total_seconds()))
    # Complete this function

f = "%a %d %b %Y %H:%M:%S %z"
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = datetime.strptime(input().strip(),f)
        t2 = datetime.strptime(input().strip(),f)
        delta = time_delta(t1, t2)
        print(int(delta))
