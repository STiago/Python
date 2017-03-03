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
