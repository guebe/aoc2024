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

visited = set() # store visited positions

direction = grid[pos[0]][pos[1]] # initial direction
while(True):
    delta = get_delta(direction)
    new = (pos[0]+delta[0],pos[1]+delta[1])
    if new[0] >= ROW or new[1] >= COL or new[0] < 0 or new[1] < 0:
        break # left grid
    elif "#" == grid[new[0]][new[1]]:
        direction = turn_right(direction) # turn
    else:
        pos = new # move in current direction
        visited.add(pos)

print(len(visited))

