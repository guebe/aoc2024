
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
    c = (int(xy2[0][2:]), int(xy2[1][2:]))

    max_ = 0xfffffffffffffffffffffff
    minsum = max_
    for i in range(100):
         for j in range(100):
             if c[0] == i*a[0] + j*b[0] and c[1] == i*a[1] + j*b[1]:
                 if (i*3+j < minsum):
                     minsum = i*3+j
    if minsum != max_:
        sumsections += minsum
print(sumsections)
