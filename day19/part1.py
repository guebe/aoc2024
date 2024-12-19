from functools import cache

lines = open(0).read().splitlines()
patterns = lines[0].split(', ')
designs = lines[2:]

print(patterns)

@cache
def does_contain(design):
    found = False
    if len(design) == 0:
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            searchstr = design[len(pattern):]
            print(f"{design} starts with {pattern}")
            found = does_contain(searchstr)
            if (found == True): break
    return found

count = 0
for design in designs:
    ret = does_contain(design)
    print(f"{ret}: {design}")
    print()
    if ret: count += 1

print(count)

