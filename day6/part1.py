a = open(0).read().splitlines()

ROW = len(a)
COL = len(a[0])

# determine initial position
pos = 0
for r in range(ROW):
    for c in range(COL):
        if "^" == a[r][c]:
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

direction = a[pos[0]][pos[1]] # initial direction
visited = set() # store visited positions

while(True):
    delta = get_delta(direction)
    npos = (pos[0]+delta[0],pos[1]+delta[1])
    if npos[0] >= ROW or npos[1] >= COL or npos[0] < 0 or npos[1] < 0:
        break # left grid
    elif "#" == a[npos[0]][npos[1]]:
        direction = turn_right(direction) # turn
    else:
        pos = npos # move in current direction
        visited.add(pos)

print(len(visited))

