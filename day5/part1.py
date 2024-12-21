from collections import defaultdict

file = open(0) # file object simplifies parsing of sectioned data file

order = defaultdict(list) # creates an empty list by default
updates = []
for line in file:
    if line.isspace():
        break
    o = list(map(int, line.split('|'))) # ATTENTION: map to int ASAP
    order[o[0]].append(o[1])

for line in file:
    updates.append(list(map(int, line.split(',')))) # ATTENTION: map to int ASAP

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
