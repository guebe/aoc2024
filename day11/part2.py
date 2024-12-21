stones = list(map(int,open(0).readline().strip().split(' ')))

# This function is used to keep track of splitted stones well.
#
# e.g. stone 2048 counted 4 times must be split to 20 counted 4 times
# _and_ 48 counted 4 times. Thus += value _and_ = value is important.
#
# In other words this function compresses stones and helps to keep the
# dictionary small.
def inc_or_set(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    else:
        dictionary[key] += value

# trivial function to split a stone.
# precondition: ATTENTION: Only call this function if you ought to
# split a stone
def splitstone(stone):
    strstone = str(stone)
    half = len(strstone) // 2
    stone1 = int(strstone[:half])
    stone2 = int(strstone[half:])
    return (stone1, stone2)

# count unique stones
counter = {}
for stone in stones:
    inc_or_set(counter, stone, 1) # initially each stone is counted once, but we may have duplicates - which are compressed by this function

print(counter)

for i in range(75):
    new = {}
    print(f"at {i}")
    for stone, count in counter.items():
        if stone == 0:
            inc_or_set(new, 1, count)
        elif len(str(stone)) % 2 == 0:
            stone1, stone2 = splitstone(stone)
            inc_or_set(new, stone1, count)
            inc_or_set(new, stone2, count)
        else:
            inc_or_set(new, stone*2024, count)
    counter = new
    #print(counter)

print(len(counter))
total = 0
for stone, count in counter.items():
    total += count

print(total)

