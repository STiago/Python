#!/bin/python

import sys

n = int(raw_input().strip())
p = int(raw_input().strip())
solution = 0
solution = min(p//2, n//2 - p//2)
print(solution)
