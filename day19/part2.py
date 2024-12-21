from functools import cache

lines = open(0).read().splitlines()
patterns = lines[0].split(', ')
designs = lines[2:]

print(patterns)

@cache
def does_contain(design):
    found = False
    res = 0
    if len(design) == 0:
        return 1
    for pattern in patterns:
        if design.startswith(pattern):
            searchstr = design[len(pattern):]
            print(f"{design} starts with {pattern}")
            res += does_contain(searchstr)
            if (found == True): break
    return res

count = 0
for design in designs:
    ret = does_contain(design)
    print(f"{ret}: {design}")
    print()
    if ret>0: count += ret

print(count)

