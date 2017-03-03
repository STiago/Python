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
