## 19.Quicksort

#### Task
Challenge
Given "ar" and "pos=ar[0]", partition into left, center(equal), right and using the Divide instructions above. Then print each element in left followed by each element in equal, followed by each element in right on a single line. Your output should be space-separated.

#### Input Format

The first line contains n(the size of ar).
The second line contains n space-separated integers describing ar (the unsorted array). The first integer (corresponding to ar[0]) is your pivot element, pos.

#### Output Format

On a single line, print the partitioned numbers (i.e.: the elements in left, then the elements in equal, and then the elements in right). Each integer should be separated by a single space.

#### Sample Input

5
4 5 3 7 2

#### Sample Output

3 2 4 5 7

#### Solution

```
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
```
