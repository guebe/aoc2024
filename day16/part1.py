import heapq
from collections import defaultdict

grid=list(map(list, open(0).read().splitlines()))

SZ = len(grid)
assert SZ == len(grid[0])
path = set()

for y in range(SZ):
    for x in range(SZ):
        if grid[y][x] == ".":
            path.add((x,y))
        elif grid[y][x] == "S":
            path.add((x,y))
            start = (x,y)
        elif grid[y][x] == "E":
            path.add((x,y))
            end = (x,y)

def rotl(a):
    x,y=a; return (y,-x)

def rotr(a):
    x,y=a; return (-y,x)

def add(a, b):
    return (a[0]+b[0],a[1]+b[1])

source = (start, (1,0)) # source node
dist = defaultdict(lambda:0x7fffffff) # unknown distance
dist[source] = 0 # the distance to the source node is 0
Q = [(0, source)] # associated priority equals dist[]

while Q:
    _, (v,d) = heapq.heappop(Q) # remove and return the best vertex

    if v == end: print(dist[(v,d)]); break # stop when we reached end, end in my example is only reached from one previous position (does not work for all inputs)

    straight = ((add(v,d), d), 1)
    left = ((v,rotl(d)), 1000)
    right = ((v,rotr(d)), 1000)
    neighbor = (straight, left, right)
    for u, weight in neighbor: # go through all u neighbors of v
        if u[0] in path:
            alt = weight + dist[(v,d)] # alternative distance
            if alt < dist[u]: 
                dist[u] = alt
                heapq.heappush(Q, (alt, u))

