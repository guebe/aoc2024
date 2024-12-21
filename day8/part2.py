from collections import defaultdict
import itertools
import copy

grid = list(map(list, open(0).read().splitlines()))

ROW = len(grid)
COL = len(grid[0])

antennas = defaultdict(list)

for r in range(ROW):
    for c in range(COL):
        x = grid[r][c]
        if x != '.':
            antennas[x].append((r,c))

def in_bounds(cord):
    r, c = cord
    if r >= 0 and c >= 0 and r < ROW and c < COL:
        return True
    else:
        return False

antinodes = set()

for frequency, antenna_list in antennas.items():
    for a1, a2 in itertools.combinations(antenna_list, 2):
        dr = a1[0] - a2[0]
        dc = a1[1] - a2[1]
        antinodes.add(a1)
        antinodes.add(a2)
        while in_bounds(a1):
            a1 = (a1[0] + dr, a1[1] + dc)
            if in_bounds(a1):
                antinodes.add(a1)
        while in_bounds(a2):
            a2 = (a2[0] - dr, a2[1] - dc)
            if in_bounds(a2):
                antinodes.add(a2)

dbg = copy.deepcopy(grid)
for d in antinodes:
    dbg[d[0]][d[1]] = '#'
for line in dbg:
    print(''.join(line))

print(len(antinodes))

