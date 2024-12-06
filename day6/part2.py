
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

t=0

path = set() # set for unique visited path
initial_pos = pos
initial_guard = guard

while(True):
    npos = (pos[0]+delta[0],pos[1]+delta[1])
    if npos[0] >= ROW or npos[1] >= COL or npos[1] < 0 or npos[0] < 0:
        break
    if "#" == a[npos[0]][npos[1]]:
        guard = turn_right(guard) # direction
        delta=get_delta(guard)
    else:
        pos = npos
        path.add(pos)
        t += 1

print(len(path))

def is_endless(a, pos, guard):
    path_and_dir = set() # set to detect if we have endless loop
    delta=get_delta(guard)
    while(True):
        npos = (pos[0]+delta[0],pos[1]+delta[1])
        if npos[0] >= ROW or npos[1] >= COL or npos[1] < 0 or npos[0] < 0:
            return False
        if "#" == a[npos[0]][npos[1]]:
            guard = turn_right(guard) # direction
            delta=get_delta(guard)
        else:
            if (npos, guard) in path_and_dir:
                return True
            pos = npos
            path_and_dir.add((pos, guard))

t2 = 0
for modi in path:
    a_trie = a.copy()
    x, y = modi[0], modi[1]
    line = a_trie[x]
    a_trie[x] = line[:y] + '#' + line[y + 1:] # modify line
    
    if (is_endless(a_trie, initial_pos, initial_guard)):
        #for line in a_trie:
        #    print(line)
        #print()
        t2 += 1

print(t2)






