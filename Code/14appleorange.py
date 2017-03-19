#!/bin/python

import sys

def fruit(s,t,a,b,m,n,apple,orange):
    cApple = cOrange = 0

    for i in range(0,m):
        l = apple[i] + a
        if l>=s and l<=t:
            cApple += 1

    for i in range(0,n):
        l = orange[i] + b
        if l>=s and l<=t:
            cOrange += 1
    return(cApple, cOrange)

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

solution = fruit(s,t,a,b,m,n,apple,orange)
for i in solution:
    print i
