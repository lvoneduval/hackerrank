#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
word_h = [h[ord(nb) - ord('a')] for nb in word]
print(max(word_h) * len(word))
