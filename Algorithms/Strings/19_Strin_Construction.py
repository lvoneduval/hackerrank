#!/bin/python3

import sys

def stringConstruction(s):
    l = set(s)
    return(len(l))
    # Complete this function

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)
