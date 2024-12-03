import re
FILE = open("input").read()
s = 0
do = 1
for m in re.findall(r'mul\((\d+),(\d+)\)|(do)\(\)|(don\'t)\(\)', FILE):
    print(m)
    if m[0] and m[1]:
        s = s + do*int(m[0])*int(m[1])
    elif m[2]:
        do = 1
    elif m[3]:
        do = 0

print(s)
