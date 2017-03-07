## String
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
