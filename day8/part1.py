from collections import defaultdict
import itertools

grid = list(map(list, open(0).read().splitlines()))

ROW = len(grid)
COL = len(grid[0])

antennas = defaultdict(list)

for r in range(ROW):
    for c in range(COL):
        x = grid[r][c]
        if x != '.': # FIXME: must be an antenna
            antennas[x].append((r,c))

print(antennas)

t = 0

def in_bounds(cord):
    r, c = cord
    if r >= 0 and c >= 0 and r < ROW and c < COL:
        return True
    else:
        return False

import copy
dbg = copy.deepcopy(grid)
dbg2 = []

for frequency, antenna_list in antennas.items():
    for a1, a2 in itertools.combinations(antenna_list, 2):
        dr = a1[0] - a2[0]
        dc = a1[1] - a2[1]
        n1 = (a1[0] + dr, a1[1] + dc)
        n2 = (a2[0] - dr, a2[1] - dc)
        print(f"{a1}, {a2} delta {dr} {dc} -> {n1} {n2}")
        if in_bounds(n1) and n1 not in dbg2: # FIXME there is only one resonant frequency in dbg2
            t+=1
            dbg2.append(n1)
        if in_bounds(n2) and n2 not in dbg2:
            t+=1
            dbg2.append(n2)

print(t)
print(len(dbg2))

for d in dbg2:
    dbg[d[0]][d[1]] = '#'

for line in dbg:
    print(''.join(line))


