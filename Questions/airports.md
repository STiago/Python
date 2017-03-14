## Airports
 	
In this exercise, you have to find the closest route between two airports.
 
Write a function findRoutes(source, destination) that efficiently outputs all possible routes sorted by distance.
 
#### INPUT:
Line 1: N, the number of segments
Line 2: ORIGIN, the IATA code of the origin
Line 2: DESTINATION, the IATA code of the destination
Line 3 to N+3: The N segments expressed as ORIGIN DESTINATION DISTANCE
 
#### OUTPUT:

    Display ORIGIN if no segment is provided
    Otherwise, display the list of possible itineraries sorted by distance

 
#### CONSTRAINTS:
0 ≤ N < 1000

PYTHON CODE TO READ INPUT:

import sys

n = int(raw_input())
origin = raw_input()
destination = raw_input()
segments = []
for i in xrange(n):
    segments.append(raw_input())

print "Hello World!"

EXAMPLE:
Input
6
SFO
MSP
SFO SEA 679
SEA MSP 1399
SFO LAX 338
PHX SEA 1107
LAX PHX 370
PHX MSP 1276

#### Output
SFO -> LAX -> PHX -> MSP
SFO -> SEA -> MSP
SFO -> LAX -> PHX -> SEA -> MSP
 
Available RAM : 512MB
Timeout: 6 seconds

    The program has to read inputs from standard input
    The program has to write the solution to standard output
    The program must run in the test environment

Download the files provided in the test script:
Validate basic solution: in1.txt out1.txt
