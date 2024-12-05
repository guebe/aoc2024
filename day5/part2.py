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
    valid = 0
    was_wrong = 0

    while (valid == 0):
        found_error = 0
        for i, page in enumerate(update):
            valid = 0
            o = order[page]

            after = update[(i+1):]
            #print(page)
            #print(after)

            for j, a in enumerate(after):
                if a in o:
                    pass
                else:
                    print(f"fail {page} {after} {a}")
                    print(update)
                    tmp = a
                    del(update[i+j+1])
                    update.insert(i,tmp)
                    print(update)
                    found_error = 1
                    was_wrong = 1
                    break
            if (found_error == 0):
                print("valid")
                valid = 1
            else:
                print(f"breaking {valid=}")
                break

    if (was_wrong == 1):
        print("ok")
        print(update)
        ok.append(update)


for update in updates:
    check(update)

print(ok)

t = 0
for o in ok:
    t += int(o[len(o)//2])

print(t)
