a = open('input').readlines()
Y = len(a)
X = len(a[0])
DIRECTIONS = [(-1,-1), (-1,0), (-1,1),
              ( 0,-1),         ( 0,1),
              ( 1,-1), ( 1,0), ( 1,1)]
count = 0
for y in range(Y):
    for x in range(X):
        for dy, dx in DIRECTIONS:
            x1,x2,x3 = (x+1*dx, x+2*dx, x+3*dx)
            y1,y2,y3 = (y+1*dy, y+2*dy, y+3*dy)
            if 0 <= x3 < X and 0 <= y3 < Y:
                if a[y][x]+a[y1][x1]+a[y2][x2]+a[y3][x3] == "XMAS":
                    count += 1
print(count)
