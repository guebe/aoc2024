
grid=list(map(list, open(0).read().splitlines()))
SZ=len(grid)
assert SZ == len(grid[0])
directions=[(0,1),(0,-1),(1,0),(-1,0)]
regions=[]
for i in range(SZ):
    for j in range(SZ):
        ch = grid[i][j]
        assert ch != "$"

def in_bounds(x,y):
    if 0 <= x < SZ and 0 <= y < SZ:
        return True
    return False

def get_regions(coordinates, patch):
    stack = [coordinates]
    while stack:
        coordinates = stack.pop()
        x,y=coordinates
        for dx, dy in directions:
            nx = x+dx
            ny = y+dy
            if in_bounds(nx, ny):
                if patch == grid[ny][nx]:
                    next_point = (nx,ny)
                    regions[-1].append(next_point)
                    grid[ny][nx] = '$'
                    stack.append(next_point)

def count_x_top(line, region):
    last_x, last_y = line[0]
    count = 0
    for i, (x, y) in enumerate(line):
        assert x >= last_x
        assert y == last_y
        # a top side line AND (previous not there OR previous no top side line)
        if (x,y-1) not in region and ((x-1,y) not in region or (x-1,y-1) in region):
            count += 1
        # a bottom side line AND (previous not there OR previous no bottom side line)
        if (x,y+1) not in region and ((x-1,y) not in region or (x-1,y+1) in region):
            count += 1
        last_x = x
    return count

def count_y_top(line, region):
    last_x, last_y = line[0]
    count = 0
    for i, (x, y) in enumerate(line):
        assert x == last_x
        assert y >= last_y
        # a left side line AND (previous not there OR previous no left side line)
        if (x-1,y) not in region and ((x,y-1) not in region or (x-1,y-1) in region):
            count += 1
        # a right side line AND (previous not there OR previous no right side line)
        if (x+1,y) not in region and ((x,y-1) not in region or (x+1,y-1) in region):
            count += 1
        last_x = x
    return count

def get_sides(region):
    #print(f"region {region}")
    count = 0
    for y in range(SZ):
        line = []
        for x in range(SZ):
            if (x,y) in region:
                line.append((x,y))
        if line:
            cnt = count_x_top(line, region)
            #print(f"line {line} count {cnt}")
            count += cnt
    for x in range(SZ):
        row = []
        for y in range(SZ):
            if (x,y) in region:
                row.append((x,y))
        if row:
            cnt = count_y_top(row, region)
            #print(f"row {line} count {cnt}")
            count += cnt
    #print(f"count {count}")
    return count

for r in range(SZ):
    for c in range(SZ):
        ch = grid[r][c]
        if ch != '$':
            grid[r][c] = '$'
            coordinate = (c,r)
            regions.append([coordinate])
            get_regions((coordinate), ch)

total=0
for region in regions:
    total += len(region)*get_sides(region)
print(total)
