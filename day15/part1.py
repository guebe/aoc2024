
lines = open(0).read()

field, dirs = lines.split('\n\n')
field = field.split('\n')
dirs = dirs.strip('\n')
print(field)
print(dirs)

boxes = set()
walls = set()
robot = None
cols = len(field[0].strip('\n'))
rows = len(field)

for y,line in enumerate(field):
    for x,char in enumerate(line.strip('\n')):
        if char == '.':
            pass
        elif char == 'O':
            boxes.add((x,y))
        elif char == '#':
            walls.add((x,y))
        elif char == '@':
            assert robot == None
            robot=(x,y)
        else:
            assert False

print(robot)
print(walls)
print(boxes)

directions = { '^': (0,1), 'v': (0,-1), '>': (1,0), '<': (-1,0) }

def dbg():
    for y in range(rows):
        for x in range(cols):
            if (x,y) in walls:
                print('#', end='')
            elif (x,y) in robot:
                print('@', end='')
            elif (x,y) in boxes:
                print('O', end='')
            else:
                print(' ', end='')
        print()

for d in dirs:
    assert d in directions
    dx,dy = directions[d]

    todo = []
    np = robot
    do_move = False
    while True:
        np = (np[0]+dx,np[1]+dy)
        if np in walls:
            do_move = False
            break
        elif np in boxes:
            todo.append(np)
        else: # empty space
            do_move = True
            break

    if do_move:
        robot = (robot[0]+dx,robot[1]+dy)
        for box in todo:
            boxes.remove(box)
            boxes.add((box[0]+dx,box[1]+dy))

total = 0
for x,y in boxes:
    total += (y*100 + x)

print(total)





    
