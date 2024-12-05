from collections import defaultdict
import functools

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

# rational for return values:
# the default comparison function for two integers is (x-y)
# now (x-y) returns -1 if the integers are in order, respectively 1 if they
# are not in order, and 0 if they are the same!
def compare(x,y):
    if x not in order:
        return 0 # same order
    if y in order[x]:
        return -1 # in order
    else:
        return 1 # not in order
    return 

t = 0
for update in updates:
    if (not is_ordered(update)):
        update.sort(key=functools.cmp_to_key(compare))
        t += int(update[len(update)//2])
print(t)
