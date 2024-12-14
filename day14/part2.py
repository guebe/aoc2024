lines = open(0).read().splitlines()

#rows = 7 # FIXME
#cols = 11 # FIXME
rows = 103 # FIXME
cols = 101 # FIXME

points = []
vs = []

def move(p, v):
    x, y = p
    dx, dy = v
    nx = x + dx
    ny = y + dy
    return (nx%cols, ny%rows)

def vis(i):
    print("***************************************")
    print(i)
    for y in range(rows):
        for x in range(cols):
            if (x,y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print()

for line in lines:
    p_line, v_line = line.strip('\n').split(' ')
    p = tuple(map(int,p_line.split('=')[1].split(',')))
    v = tuple(map(int,v_line.split('=')[1].split(',')))

    points.append(p)
    vs.append(v)

# the ebe score scores if a point has a neighbor
# in any direction.
# two single neighbors score 2
# a quadratic field of 4 scores 8
# this simple score can be used to find objects
# could simply be improved to bigger objects by checking the neighbor of neighbors also
def ebe_score(points):
    score = 0
    for x,y in points:
        for dx, dy in ([0,-1],[0,1],[1,0],[-1,0]):
            nx = x + dx
            ny = y + dy
            if (nx,ny) in points:
                score += 1
    return score

print(len(points))

for i in range(10000000):

    tmp = []

    for j, p in enumerate(points):
        p = move(p,vs[j])
        tmp.append(p)

    points = tmp
    score = ebe_score(points)
    print(f"{i} {score}")
    if (score > 250):
        vis(i)

    if (i == 100):
        q1,q2,q3,q4=(0,0,0,0)
        hx = cols//2
        hy = rows//2
        x, y = p
        if x < hx and y < hy: q1+=1
        if x < hx and y > hy: q2+=1
        if x > hx and y < hy: q3+=1
        if x > hx and y > hy: q4+=1
        print(q1*q2*q3*q4)

# ATTENTION: the number you get is too low by one - I increased it manually after not getting the star!

