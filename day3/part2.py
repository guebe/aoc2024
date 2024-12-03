import re
FILE = open("input").read()

pattern = re.compile(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)')
pattern2 = re.compile(r'mul\(([0-9]+),([0-9]+)\)')

s = 0
do = 1

for x in re.findall(pattern, FILE):
    if 'mul(' in x:
        for (a, b) in re.findall(pattern2, x):
            print(f"mul({a},{b})")
            s = s + do*int(a)*int(b)
    elif 'do(' in x:
        do = 1
        print(x)
    elif 'don\'t(' in x:
        do = 0
        print(x)

print(s)

