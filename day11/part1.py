import sys
stones = list(map(int,open(0).readline().strip().split(' ')))

print(stones)

#for i in range(6):
for i in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            strstone = str(stone)
            half = len(strstone) // 2
            stone1 = int(strstone[:half])
            stone2 = int(strstone[half:])
            new_stones.append(stone1)
            new_stones.append(stone2)
        else:
            new_stones.append(stone*2024)
    stones = new_stones
    print(stones)
    print(len(stones))
    #sys.exit()
