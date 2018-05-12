# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

adj = {} #adjacency list

dist = {}

def get_distance(road):
    pass
    #in my home dir

def find_routes(node, destination, routes, current_road, visited):

    visited.add(node)
    current_road.append(node)

    print "Step ", node, destination, "Routes:", routes, "Current_road ", current_road, visited, "\n"

    #reached destination
    if node == destination:
        routes.append(list(current_road))
    if node not in adj:
        return

    if node in adj:
        for i in adj[node]:
            if i not in visited:
                #add
                #recurse
                find_routes(i, destination, routes, current_road, visited)

                #take out
                del current_road[-1]
                visited.remove(i)



def findRoutes(source, destination):
    pass
    #in my home dir

n = int(raw_input())
origin = raw_input()
destination = raw_input()

print n, origin, destination
segments = []

for i in xrange(n):
    segments.append(raw_input())
    a, b, dis = segments[-1].split(" ")
    print a,b, dis
    if a in adj:
        adj[a].append(b)
    else:
        adj[a] = [b]

    dist[ (a,b) ] = dis

print adj, dist

routes = []

find_routes(origin, destination, routes, [], set())

print routes

