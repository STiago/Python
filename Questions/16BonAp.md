## Bon Appetit

### Task

Anna and Brian order n items at a restaurant, but Anna declines k to eat any of the item due to an allergy. When the check comes, they decide to split the cost of all the items they shared; however, Brian may have forgotten that they didn't split the item and accidentally charged Anna for it.

You are given n, k, the cost of each of the n items, and the total amount of money that Brian charged Anna for her portion of the bill. If the bill is fairly split, print Bon Appetit; otherwise, print the amount of money that Brian must refund to Anna.

### Input Format

The first line contains two space-separated integers denoting the respective values of (the number of items ordered) and (the -based index of the item that Anna did not eat).
The second line contains space-separated integers where each integer denotes the cost, , of item (where ).
The third line contains an integer, , denoting the amount of money that Brian charged Anna for her share of the bill.

### Output Format

If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., ) that Brian must refund to Anna (it is guaranteed that this will always be an integer).

### Sample Input 

4 1
3 10 2 9
12

### Sample Output 

5

### Solution

```
#!/bin/python

k = raw_input()
n = raw_input()
bcharged = int(input())

s = map(int, k.split())
m = list(map(int,n.split()))

rest = s[1]

total = sum(m)
both = total-m[rest]
part = both/2
solution = bcharged-part

if part != bcharged:
    print solution
else:
    print "Bon Appetit"

```
