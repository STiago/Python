# María Victoria Santiago Alcalá

## Python - Challenges

### Tuesday 28th of February, 2017

Repository with **python** exercises from several pages as [Hackerrank](https://www.hackerrank.com/domains/python) .


* Exercises:
    
    - [Questions](https://github.com/STiago/Python/tree/master/Questions)
    
    - [Code](https://github.com/STiago/Python/tree/master/Code)


## Exercises

## 1. List
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

## 2. Tuples
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
```

## 4. Find the second largest number
#### Task
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

## 5.Nested Lists
#### Task
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#### Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

#### Constraints
    - 2<=N<=5
    - There will always be one or more students having the second lowest grade.

#### Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

#### Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

#### Sample Output

Berry
Harry

#### Solution

```
students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])
    
stu = 0
stu = students[0]
minim = stu[1]
n_min = stu[0]
m = []
name = []
valor = 0

students.sort(key=lambda x: x[1])
lowest = students[0][1]
two_worst = [s for s in students if s[1] != lowest][:2]

if len(two_worst) > 1:
    if two_worst[0][1] == two_worst[1][1]:
        two_worst.sort(key = lambda x: x[0])
        for s in two_worst:
            print s[0]
    else:
        print(two_worst[0][0])
else:
    print (two_worst[0][0])
```

## 6.Finding the percentage
#### Task
You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

#### Input Format

The first line contains the integer N, the number of students. The next N lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.

#### Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

#### Sample Input

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

#### Sample Output

56.00

#### Solution

```
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    marks = student_marks[query_name]
    avg = reduce(lambda x,y: x+y, marks)/len(marks)
    #print("{0:.2f}".format(avg))
    print("%.2f" % avg)
```

## 7.Swap
#### Task
You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

#### Solution

```
def swap_case(s):
    solution = ''
    for element in s:
        if element.isupper():
            solution += element.lower() 
        else:
            solution += element.upper()
    return solution


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
```

## 8.String Split and Join
#### Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

#### Input Format
The first line contains a string consisting of space separated words.

#### Output Format
Print the formatted string as explained above.

#### Sample Input

this is a string 

#### Sample Output

this-is-a-string

#### Solution

```
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line
```


## 9.String
#### Task
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

    Hello firstname lastname! You just delved into python.

#### Input Format

The first line contains the first name, and the second line contains the last name.

#### Output Format

Print the output as mentioned above.

#### Sample Input

Guido
Rossum

#### Sample Output

Hello Guido Rossum! You just delved into python.

#### Solution

```
def print_full_name(a, b):
    print 'Hello ' + str(a) + ' ' + str(b) + '! You just delved into python.'
    #print("Hello {} {}! You just delved into python.".format(a,b))

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
```

## 10.Mutations
#### Task
Read a given string, change the character at a given index and then print the modified string.

#### Input Format
The first line contains a string, .
The next line contains an integer , denoting the index location and a character separated by a space.

#### Output Format
Using any of the methods explained above, replace the character at index with character .

#### Sample Input

abracadabra
5 k

#### Sample Output

abrackdabra

#### Solution

```
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
```


## 11.Find a String
#### Task

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

#### Input Format

The first line of input contains the original string. The next line contains the substring.

#### Constraints

Each character in the string is an ascii character.

#### Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

#### Sample Input

ABCDCDC
CDC

#### Sample Output

2

#### Solution

```
def count_substring(string, sub_string):
    count = 0
    i = 0
    while i<len(string):
        a = string.find(sub_string,i,len(string))
        if a == -1:
            a = 0
        else:
            count += 1
        i += a + 1              
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count

```


## 12.String Validators
#### Task
You are given a string .
Your task is to find out if the string contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

#### Input Format

A single line containing a string .

#### Output Format

In the first line, print True if has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False.

#### Sample Input

qA2

#### Sample Output

True
True
True
True
True

#### Solution


## 13.Temperatures
#### Task

```

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
```

## 14.Apple vs Orange

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

## 15.Kangaroos

### Task

There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump. The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?


### Input Format

A single line of four space-separated integers denoting the respective values of x1, v1, x2 and v2.


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

## 16.Bon Appetit

#### Task

Anna and Brian order n items at a restaurant, but Anna declines k to eat any of the item due to an allergy. When the check comes, they decide to split the cost of all the items they shared; however, Brian may have forgotten that they didn't split the item and accidentally charged Anna for it.

You are given n, k, the cost of each of the n items, and the total amount of money that Brian charged Anna for her portion of the bill. If the bill is fairly split, print Bon Appetit; otherwise, print the amount of money that Brian must refund to Anna.

#### Input Format

The first line contains two space-separated integers denoting the respective values of (the number of items ordered) and (the -based index of the item that Anna did not eat).
The second line contains space-separated integers where each integer denotes the cost, , of item (where ).
The third line contains an integer, , denoting the amount of money that Brian charged Anna for her share of the bill.

#### Output Format

If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., ) that Brian must refund to Anna (it is guaranteed that this will always be an integer).

#### Sample Input 

4 1
3 10 2 9
12

#### Sample Output 

5

#### Solution

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


## 17.Book

#### Task
Brie’s Drawing teacher asks her class to open their n-page book to page number p. Brie can either start turning pages from the front of the book (i.e., page number 1) or from the back of the book (i.e., page number n), and she always turns pages one-by-one (as opposed to skipping through multiple pages at once). When she opens the book, page is always on the right side.

Each page in the book has two sides, front and back, except for the last page which may only have a front side depending on the total number of pages of the book (see the Explanation sections below for additional diagrams).

Given n and p, find and print the minimum number of pages Brie must turn in order to arrive at page p.

#### Input Format

The first line contains an integer, n, denoting the number of pages in the book.
The second line contains an integer, p, denoting the page that Brie's teacher wants her to turn to.

#### Output Format

Print an integer denoting the minimum number of pages Brie must turn to get to page p.

##### Sample Input 0

6
2

#### Sample Output 0

1


#### Solution

```
#!/bin/python

import sys

n = int(raw_input().strip())
p = int(raw_input().strip())
solution = 0
solution = min(p//2, n//2 - p//2)
print(solution)
```


## 18.Cake Candles

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



_Code_ licensed by **GNU GENERAL PUBLIC LICENSE Version 3**.

_Text_ licensed by **Creative Commons Attribution-ShareAlike 4.0 International**.

<p align="center">
<a href="http://www.gnu.org/licenses/gpl-3.0.html">
<img alt="GPL-3.0" src="https://dl.dropboxusercontent.com/s/t0ylvis7f1stcu7/GPL-3.0.png">
</a>
<a href="https://creativecommons.org/licenses/by-sa/4.0/legalcode">
<img alt="CC-BY-SA-4.0" src="https://dl.dropboxusercontent.com/s/sb421l5usayaigo/CC-BY-SA-4.0.png">
</a>
</p>




