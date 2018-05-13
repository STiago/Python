# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

adj = {} 
dist = {}

def get_distance(road):
    sum_dist = 0
    for i in range(0,len(road)-1):
        a = road[i]
        b = road[i+1]
    sum_dist += int(dist[(a,b)])
    return sum_dist


def find_routes(node, destination, routes, current_road, visited):
    visited.add(node)
    current_road.append(node)
    
    if node == destination:
        routes.append(list(current_road))
    if node not in adj:
        return
    
    if node in adj:
        for i in adj[node]:
            if i not in visited:
                find_routes(i, destination, routes, current_road, visited)
                del current_road[-1]
                visited.remove(i)

                
n = int(raw_input())
origin = raw_input()
destination = raw_input()

segments = []
for i in xrange(n):
    segments.append(raw_input())
    a, b, dis = segments[-1].split(" ")
       
    if a in adj:
        adj[a].append(b)
    else:
        adj[a] = [b]
    dist[ (a,b) ] = dis

routes = []

find_routes(origin, destination, routes, [], set())

r_dists = [ (r, get_distance(r)) for r in routes]
r_dists.sort(key = lambda tup : tup[1])

for i in r_dists:
    for a in range(0, len(i[0])-1):
        sys.stdout.write(i[0][a])
        sys.stdout.write(" -> ")
    print i[0][-1]

