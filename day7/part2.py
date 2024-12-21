import itertools

lines = open(0).read().splitlines()

equations = {}

for line in lines:
    parse1 = line.split(": ")
    parse2 = list(map(int, parse1[1].split(" ")))
    equations[int(parse1[0])] = parse2

print(equations)

def calc(term, operators):
    res = term[0]
    for value, operator in zip(term[1:], operators):
        if operator == '*':
            res = res * value
        elif operator == '+':
            res = res + value
        elif operator == '|':
            res = int(str(res) + str(value))
    return res

t = 0
for test, term in equations.items():
    nr_operators = len(term) - 1

    print(f"{test} {term}")
    matches = False
    for operators in itertools.product(["*","+","|"], repeat=nr_operators):
        if (calc(term, operators) == test):
            matches = True
            break

    if (matches):
        t += test
        print(f"match {t} {operators}")

print(t)

