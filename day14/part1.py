lines = open(0).read().splitlines()

# FIXME
#rows = 7 # FIXME
#cols = 11 # FIXME
# FIXME
rows = 103 # FIXME
cols = 101 # FIXME

q1,q2,q3,q4=(0,0,0,0)

def move(p, v):
    x, y = p
    dx, dy = v
    nx = x + dx
    ny = y + dy
    if nx >= cols:
        nx = nx%cols
    elif nx < 0:
        nx = cols+nx
    if ny >= rows:
        ny = ny%rows
    elif ny < 0:
        ny = rows+ny
    return (nx, ny)


for line in lines:
    p_line, v_line = line.strip('\n').split(' ')
    p = tuple(map(int,p_line.split('=')[1].split(',')))
    v = tuple(map(int,v_line.split('=')[1].split(',')))
    #print(f"{p} {v}")

    for i in range(100):
        p = move(p, v)

    hx = cols//2
    hy = rows//2
    x, y = p
    if x != hx and y != hy:
        if x < hx and y < hy:
            q1+=1
        if x < hx and y > hy:
            q2+=1
        if x > hx and y < hy:
            q3+=1
        if x > hx and y > hy:
            q4+=1
    print(f"{p}")

print(q1*q2*q3*q4)

#np = move((2,4), (2,-3))
#print(f"{np}")
#np = move(np, (2,-3))
#print(f"{np}")
#np = move(np, (2,-3))
#print(f"{np}")
#np = move(np, (2,-3))
#print(f"{np}")
#np = move(np, (2,-3))
#print(f"{np}")

