#!/bin/python

import sys

def blows(n,height):
    heightest = max(height)
    blows = 0

    for i in height:
        if i==heightest:
            blows +=1
    return blows

n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

solution = blows(n,height)

print solution
