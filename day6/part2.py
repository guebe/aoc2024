grid = list(map(list, open(0).read().splitlines()))

ROW = len(grid)
COL = len(grid[0])

# determine initial position
pos = 0
for r in range(ROW):
    for c in range(COL):
        if "^" == grid[r][c]:
            pos = (r, c)

def get_delta(direction):
    if direction == '^':
        return (-1,0)
    elif direction == '>':
        return (0,1)
    elif direction == '<':
        return (0,-1)
    elif direction == 'v':
        return (1,0)

def turn_right(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == '<':
        return '^'
    elif direction == 'v':
        return '<'

def is_endless(grid, pos, visited=None):
    direction = grid[pos[0]][pos[1]] # initial direction
    visited_direction = set() # set to detect if we have endless loop
    while(True):
        delta = get_delta(direction)
        new = (pos[0]+delta[0],pos[1]+delta[1])
        if new[0] >= ROW or new[1] >= COL or new[0] < 0 or new[1] < 0:
            return False # left grid
        elif (new, direction) in visited_direction:
            return True # endless loop
        elif "#" == grid[new[0]][new[1]]:
            direction = turn_right(direction) # turn
        else:
            visited_direction.add((new, direction))
            if (visited is not None): visited.add(new)
            pos = new # move in current direction

visited = set() # store visited positions
assert is_endless(grid, pos, visited) == False
print(len(visited))

# remove guards starting position - this is not allowed
visited.remove(pos)

# add wall on all previously visited paths
t = 0
for r, c in visited:
    grid[r][c] = '#' # modify line
    if (is_endless(grid, pos)):
        t += 1
    grid[r][c] = '.' # change back

print(t)

