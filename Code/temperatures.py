# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

try:
    n = int(raw_input())
    lis = raw_input().split()
except ValueError:
    print "0 - Cannot process the data"
    
position = 0
less = 0
more = 0

s = map(int, lis)
s.append(0)
s.sort()

# Position of 0
for i in range(0,n):
    if s[i] == 0:
        position = i
        break
        
# Number close to 0
less = s[position-1]
more = s[position+1]

if abs(more) <= abs(less):
    print more
else:
    print less 



