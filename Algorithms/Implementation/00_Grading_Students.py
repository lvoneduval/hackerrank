#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i, el in enumerate(grades):
      if el >= 38 and el % 5 > 2: 
        grades[i] = (int((el + 2)/5)) * 5
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
