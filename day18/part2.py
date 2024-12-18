
lines = open(0).read().splitlines()
coords = [tuple(map(int,line.split(','))) for line in lines]

start = (0,0)
#end = (6,6) # FIXME
end = (70,70) # FIXME
SZ = end[0]+1

def dbg(c):
    for y in range(SZ):
        for x in range(SZ):
            if (x,y) in c:
                print('#',end='')
            else:
                print('.',end='')
        print()


directions = ((0,1),(0,-1),(1,0),(-1,0))

def in_bounds(p):
    x, y = p
    if 0 <= x < SZ and 0 <= y < SZ:
        return True
    else:
        return False

def add(p,d):
    x, y = p
    dx, dy = d
    return (x+dx,y+dy)

def search(start, end, walls):
    steps = 0
    todo = [(start,0)]
    visited = set()
    while todo:
        now,steps = todo.pop(0)

        if now == end:
            return steps

        for d in directions:
            new = add(now, d)
            if new not in visited and in_bounds(new) and new not in walls:
                todo.append((new,steps+1))
                visited.add(new)

    return -1

dbg(coords)
print(search(start, end, coords[0:1024]))

print(len(coords))
print(search(start, end, coords[0:3450])) #-1
print(search(start, end, coords[0:1725])) #ok
print(search(start, end, coords[0:2587])) #ok
print(search(start, end, coords[0:3018])) #-1
print(search(start, end, coords[0:2802])) #ok
print(search(start, end, coords[0:2910])) #-1
print(search(start, end, coords[0:2856])) #ok
print(search(start, end, coords[0:2883])) #ok
print(search(start, end, coords[0:2896])) #ok
print(search(start, end, coords[0:2903])) #ok
print(search(start, end, coords[0:2908])) #-1
print(search(start, end, coords[0:2907]))
print(coords[2907])

#lower = 0
#upper = len(coords)
#while True:
#    r1 = search(start, end, coords[0:upper])
#    if r1 == -1:
#        pass
    
