import re
FILE = open("input").read()

pattern = re.compile(r'mul\(([0-9]+),([0-9]+)\)')

s = 0

for (a, b) in re.findall(pattern, FILE):
    print(f"map({a},{b})")
    s = s + int(a)*int(b)

print(s)

