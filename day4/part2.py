a = open('input').readlines()
Y = len(a)
X = len(a[0])
count = 0
for y in range(1,Y-1):
    for x in range(1,X-1):
        d1 = a[y-1][x-1]+a[y][x]+a[y+1][x+1]
        d2 = a[y+1][x-1]+a[y][x]+a[y-1][x+1]
        if (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM"):
            count += 1
print(count)
