from collections import defaultdict
import sys

lines = open(0).read().splitlines()

order = defaultdict(list)
updates = []
i = 0
for line in lines:
    if line == '':
        i+=1
        continue

    if i == 0:
        o = line.split('|')
        order[o[0]].append(o[1])
    else:
        updates.append(line.split(','))

def is_ordered(update):
    for i, first in enumerate(update):
        for after in update[i+1:]:
            if after not in order[first]:
                return False
    return True

t = 0
for update in updates:
    if (is_ordered(update)):
        t += int(update[len(update)//2])
print(t)
