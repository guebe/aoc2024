from collections import defaultdict
import sys

lines = open(0).read().splitlines()

print(lines)

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


print(order)
print(updates)

ok = []

def check(update):
    for i, page in enumerate(update):
        o = order[page]

        after = update[i+1:]
        print(page)
        print(after)

        for a in after:
            if a in o:
                pass
            else:
                return
    ok.append(update)


for update in updates:
    check(update)

print(ok)

t = 0
for o in ok:
    t += int(o[len(o)//2])

print(t)
