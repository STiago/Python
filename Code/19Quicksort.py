#!/bin/python
def partition(ar):   
    pos = ar[0]
    l, c, r = [i for i in ar if i < pos], [i for i in ar if i == pos], [i for i in ar if i > pos]
    ll = ' '.join(map(str, l))
    cc = ' '.join(map(str, c))
    rr = ' '.join(map(str, r))
    solution = ll + ' '+ cc + ' ' + rr
    return solution

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print partition(ar)
