grid = open(0).read().splitlines()

SZ = len(grid)
starters = []
for y in range(SZ):
    for x in range(SZ):
        if grid[y][x] == '0':
            starters.append((x,y))

def in_bounds(x):
    if x >= 0 and x < SZ:
        return True
    else:
        return False

result = 0
trail = []
for start in starters:
    assert len(trail) == 0
    trail.append((start, 1))
    found = []

    while len(trail) > 0:
        (x, y), height = trail.pop()

        if (height == 10):
            if (x,y) not in found:
                found.append((x,y))
        else:
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nx = x + dx
                ny = y + dy
                if in_bounds(nx) and in_bounds(ny):
                    if int(grid[ny][nx]) == (height):
                        trail.append(((nx,ny), height+1))

    result += len(found)

print(result)

