## 3.List comprehensions

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
