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
