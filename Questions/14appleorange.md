## Apple vs Orange

### Task
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where is the start point and is the end point. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point and the orange tree is at point .

When a fruit falls from its tree, it lands units of distance from its tree of origin along the -axis. A negative value of means the fruit fell units to the tree's left, and a positive value of means it falls units to the tree's right.

Given the value of for apples and oranges, can you determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range ) Print the number of apples that fall on Sam's house as your first line of output, then print the number of oranges that fall on Sam's house as your second line of output.

### Input Format

The first line contains two space-separated integers denoting the respective values of s and t.
The second line contains two space-separated integers denoting the respective values of a and b.
The third line contains two space-separated integers denoting the respective values of m and n.
The fourth line contains m space-separated integers denoting the respective distances that each apple falls from point a.
The fifth line contains n space-separated integers denoting the respective distances that each orange falls from point b.

### Output Format

Print two lines of output:

    On the first line, print the number of apples that fall on Sam's house.
    On the second line, print the number of oranges that fall on Sam's house.

### Sample Input 0

7 11
5 15
3 2
-2 2 1
5 -6

### Sample Output 0

1
1

### Solution

```
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
```

