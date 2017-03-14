# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

def findRoutes(source, destination):
    depart = []
    arrive = []
    
    for i in range(0,n):
        if segments[i] == source:
            depart.append(segment[i])
        else:
            print "[ERROR] - Source empty"
            
    #depart = depart.split()
    dep = depart[1]
    
    for i in depart:
        if depart[1] == destination:
            arrive.append(depart[i])
        elif dep[i] == depart[0]:
            intermedite = dep[i]
            findRoutes(intermedite,destination)
    return arrive

if __name__ == '__main__':
    n = int(raw_input())
    origin = raw_input()
    destination = raw_input()
    segments = []
    solution = []
    
    for i in xrange(n):
        segments.append(raw_input())
    
    solution = findRoutes(origin, destination)
    
    #for i in range solution:
    #    print solution[i]
    
    print solution