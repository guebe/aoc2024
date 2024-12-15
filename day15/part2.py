
lines = open(0).read()

field, dirs = lines.split('\n\n')
field = field.split('\n')
dirs = ''.join(dirs.strip('\n').split('\n'))

boxes = dict()
walls = set()
robot = None
cols = len(field[0].strip('\n'))*2
rows = len(field)

for y,line in enumerate(field):
    for x,char in enumerate(line.strip('\n')):
        if char == '.':
            pass
        elif char == 'O':
            boxes[(x*2,y)] = '['
            boxes[(x*2+1,y)] = ']'
        elif char == '#':
            walls.add((x*2,y))
            walls.add((x*2+1,y))
        elif char == '@':
            assert robot == None
            robot=(x*2,y)
        else:
            assert False

#print(field)
#print(dirs)
#print(robot)
#print(walls)
#print(boxes)

directions = { '^': (0,-1), 'v': (0,1), '>': (1,0), '<': (-1,0) }

def dbg():
    for y in range(rows):
        for x in range(cols):
            if (x,y) in walls:
                print('#', end='')
            elif (x,y) == robot:
                print('@', end='')
            elif (x,y) in boxes:
                print(f'{boxes[(x,y)]}', end='')
            else:
                print(' ', end='')
        print()
    print()

#print("Initial state:")
#dbg()

for d in dirs:
    assert d in directions
    dx,dy = directions[d]

    todo = []
    nps = [robot]
    do_move = False
    while True:
        tmp = set()
        for np in nps:
            np = (np[0]+dx,np[1]+dy)
            tmp.add(np)
            if d == '^' or d == 'v':
                if boxes.get(np) == '[':
                    tmp.add((np[0]+1,np[1]))
                if boxes.get(np) == ']':
                    tmp.add((np[0]-1,np[1]))
        nps = tmp
        if any(np in walls for np in nps):
            do_move = False
            break
        elif any(np in boxes for np in nps):
            tmp=[]
            for np in nps:
                if np in boxes:
                    todo.append((np,boxes[np]))
                    tmp.append(np)
            nps = tmp
        else: # empty space
            do_move = True
            break

    if do_move:
        robot = (robot[0]+dx,robot[1]+dy)
        assert len(todo)%2 == 0
        for box, v in todo:
            del boxes[box]
        for box, v in todo:
            boxes[(box[0]+dx,box[1]+dy)] = v

    #print(f"Move {d}:")
    #dbg()

#dbg()
total = 0
for (x,y),v in boxes.items():
    if v == '[':
        total += (y*100 + x)

print(total)





    
