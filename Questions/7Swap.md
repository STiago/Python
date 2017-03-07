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
