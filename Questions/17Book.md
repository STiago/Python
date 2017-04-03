## Book

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
