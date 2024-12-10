

grid = open(0).read().splitlines()

SZ = len(grid)
starters = []
for y in range(SZ):
    for x in range(SZ): # FIXME cols vs rows
        if grid[y][x] == '0':
            starters.append((x,y))

def in_bounds(x):
    if x >= 0 and x < SZ:
        return True
    else:
        return False

#print(grid)
#print(starters)

def dbg(f):
    g = ""
    for x, y in f:
        g += f" [{y}][{x}]"
    return g

result = 0
trail = []
import sys
for start in starters:
    assert len(trail) == 0
    trail.append((start, 1))
    #print(f"start at [{start[1]+1}][{start[0]+1}]")
    found = []

    while len(trail) > 0:
        (x, y), height = trail.pop()

        if (height == 10):
            if (x,y) not in found:
                #print(f"fin {height} at [{y+1}][{x+1}]")
                found.append((x,y))

        else:
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nx = x + dx
                ny = y + dy
                if in_bounds(nx) and in_bounds(ny):
                    if int(grid[ny][nx]) == (height):
                        #print(f"nex {height} at [{ny+1}][{nx+1}]")
                        trail.append(((nx,ny), height+1))

    #print(f"found {len(found)}")
    result += len(found)
    # sys.exit()

print(result)


