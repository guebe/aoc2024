
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

def get_perimeter(region):
    perimeter=0
    for x, y in region:
        for dx, dy in directions:
            if (x+dx,y+dy) not in region:
                perimeter+=1
    return perimeter

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
    total += len(region)*get_perimeter(region)
print(total)
