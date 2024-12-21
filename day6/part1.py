
a = open(0).read().splitlines()

pos = 0

ROW = len(a)
COL = len(a[0])

for r in range(ROW):
    for c in range(COL):
        if "^" == a[r][c]:
            pos = (r, c)

guard = a[pos[0]][pos[1]]

def get_delta(guard):
    if guard == '^':
        delta=(-1,0)
    if guard == '>':
        delta=(0,1)
    if guard == '<':
        delta=(0,-1)
    if guard == 'v':
        delta=(1,0)
    return delta

def turn_right(guard):
    if guard == '^':
        return '>'
    if guard == '>':
        return 'v'
    if guard == '<':
        return '^'
    if guard == 'v':
        return '<'

delta=get_delta(guard)
import sys
print(guard)
print(pos)
print(delta)

t=0

m = set()

while(True):
    npos = (pos[0]+delta[0],pos[1]+delta[1])
    print(pos)
    if npos[0] >= ROW or npos[1] >= COL or npos[1] < 0 or npos[0] < 0:
        break
    if "#" == a[npos[0]][npos[1]]:
        guard = turn_right(guard)
        delta=get_delta(guard)
        print(guard)
        print(pos)
        print(delta)
    else:
        pos = npos
        m.add(pos)
        t += 1

print(len(m))





