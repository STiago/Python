#!/bin/python

import sys

def positionKangaroos(x1,v1,x2,v2):
    if not (x1 == x2 and v1 < v2) or (x1 < x2 and v1 <= v2):
        for i in range(0,100):
            x1 += v1
            x2 += v2
            if x1==x2:
                print 'YES'
                exit()
            #break
        print 'NO'

x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

solution = positionKangaroos(x1,v1,x2,v2)
