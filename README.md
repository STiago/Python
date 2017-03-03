# María Victoria Santiago Alcalá

## Python - Challenges

### Tuesday 28th of February, 2017

Repository with **python** exercises from several pages as [Hackerrank](https://www.hackerrank.com/domains/python) .


* Exercises:
    
    - [Questions](https://github.com/STiago/Python/tree/master/Questions)
    
    - [Code](https://github.com/STiago/Python/tree/master/Code)


## Exercises

### 1. List
#### Consider a list (list = []). You can perform the following commands:

```
    insert i e: Insert integer at position .
    print: Print the list.
    remove e: Delete the first occurrence of integer .
    append e: Insert integer at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.
```

#### Initialize your list and read in the value of followed by lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

#### Input Format

The first line contains an integer, , denoting the number of commands.
Each line of the subsequent lines contains one of the commands described above.

#### Constraints

    - The elements added to the list must be integers.

#### Output Format

For each command of type print, print the list on a new line.

#### Solution

```
if __name__ == '__main__':
    N = int(raw_input())
    
    list = []
    
    for i in range(N): 
        option = raw_input().split()
        if option[0] == 'print':
            print(list)
        elif option[0] == 'sort':
            list.sort()
        elif option[0] == 'remove':
            list.remove(int(option[1]))
        elif option[0] == 'append':
            list.append(int(option[1]))
        elif option[0] == 'insert':
            list.insert(int(option[1]),int(option[2]))
        elif option[0] == 'reverse':
            list.reverse()
        elif option[0] == 'pop':
list.pop()
```

### 2. Tuples
#### Task
Given an integer, , and space-separated integers as input, create a tuple, , of those integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

#### Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains space-separated integers describing the elements in tuple .

#### Output Format

Print the result of .

#### Sample Input

2
1 2

#### Sample Output

3713081631934410656


#### Solution

```
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))
```

### 3.List comprehensions

#### Task
Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an integer N. You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N. Here, 0<=i<=X; 0<=j<=Y; 0<=k<=Z

#### Input Format

Four integers X,Y,Z and N each on four separate lines, respectively.

#### Constraints

Print the list in lexicographic increasing order.

#### Sample Input

1
1
1
2

#### Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] 


#### Solution

```
from itertools import product
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    xd = [i for i in range(x+1)]
    yd = [i for i in range(y+1)]
    zd = [i for i in range(z+1)]
    print([list(x) for x in product(xd,yd,zd) if sum(x)!=n])
```

### 4. Find the second largest number
### Task
You are given N numbers. Store them in a list and find the second largest number.

#### Input Format
The first line contains N. The second line contains an array A[] of N integers each separated by a space.

#### Output Format
Output the value of the second largest number.

#### Sample Input

5
2 3 6 6 5

#### Sample Output

5

#### Solution

```
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    arr =sorted(set(arr))
    print(arr[-2]) 
```

### 5.

### 6.


### 7.




_Código_ liberado bajo licencia **GNU GENERAL PUBLIC LICENSE Version 3**.

_Texto_ liberado bajo la licencia **Creative Commons Attribution-ShareAlike 4.0 International**.

<p align="center">
<a href="http://www.gnu.org/licenses/gpl-3.0.html">
<img alt="GPL-3.0" src="https://dl.dropboxusercontent.com/s/t0ylvis7f1stcu7/GPL-3.0.png">
</a>
<a href="https://creativecommons.org/licenses/by-sa/4.0/legalcode">
<img alt="CC-BY-SA-4.0" src="https://dl.dropboxusercontent.com/s/sb421l5usayaigo/CC-BY-SA-4.0.png">
</a>
</p>




