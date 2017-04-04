## Cake Candles

#### Task
Colleen is turning years old! She has n candles of various heights on her cake, and candle i has height "height". Because the taller candles tower over the shorter ones, Colleen can only blow out the tallest candles.

Given height the for each individual candle, find and print the number of candles she can successfully blow out.

#### Input Format

The first line contains a single integer,n , denoting the number of candles on the cake.
The second line contains n space-separated integers, where each integer i describes the height of candle i.

#### Output Format

Print the number of candles Colleen blows out on a new line.

#### Sample Input 0

4
3 2 1 3

#### Sample Output 0

2

#### Solution

```
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
```
