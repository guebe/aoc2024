
sections = open(0).read().strip('\n').split('\n\n')

sumsections = 0
for section in sections:
    lines = section.split('\n')
    line0 = lines[0]
    line1 = lines[1]
    line2 = lines[2]
    line0 = line0[10:].strip()
    line1 = line1[10:].strip()
    line2 = line2[7:].strip()
    xy0 = line0.split(', ')
    xy1 = line1.split(', ')
    xy2 = line2.split(', ')
    a = (int(xy0[0][2:]), int(xy0[1][2:]))
    b = (int(xy1[0][2:]), int(xy1[1][2:]))
    c = (int(xy2[0][2:])+10000000000000, int(xy2[1][2:]) + 10000000000000)

    max_ = 0xfffffffffffffffffffffff
    minsum = max_

    i = (c[0]*b[1]-c[1]*b[0]) / (a[0]*b[1]-b[0]*a[1])
    if (int(i) == i):
        i = int(i)
        j = (c[1]-i*a[1])/b[1]
        if (int(j) == j):
            j = int(j)
            minsum = i*3+j

    if minsum != max_:
        sumsections += minsum
print(sumsections)
