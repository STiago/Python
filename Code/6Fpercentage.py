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
