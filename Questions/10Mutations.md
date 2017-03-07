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
