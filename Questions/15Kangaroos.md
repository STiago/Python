## 15.Kangaroos

### Task

There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location and moves at a rate of meters per jump. The second kangaroo starts at location and moves at a rate of meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?


### Input Format

A single line of four space-separated integers denoting the respective values of , , , and .


###Output Format

Print YES if they can land on the same location at the same time; otherwise, print NO.

Note: The two kangaroos must land at the same location after making the same number of jumps.

### Sample Input 0

0 3 4 2

### Sample Output 0

YES


### Solution

```
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
```
