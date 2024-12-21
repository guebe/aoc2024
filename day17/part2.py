def out(A): # this is just a manually simplified formula of the disassembler output
    B = (A%8)^2
    return (B ^ 7 ^ (A>>B)) % 8

def to_program(A):
    while A > 0:
        print(f"{out(A)},", end='')
        A //= 8
    print()

def to_A(program):
    probes = set([0])
    for x in reversed(program):
        new_probes = set()
        for probe in probes:
           for i in range(8):
               if out(probe*8 + i) == x:
                   new_probes.add(probe*8 + i)
        probes = new_probes
    return probes

A = 27334280
print(f"Convert A {A} ({oct(A)}) to program:")
to_program(A)
print()

program = [7,6,5,3,6,5,7,0,4] 
print(f"Convert program {program} to A:")
results = to_A(program)
print(sorted(results))
print(min(results))
assert A in results
print()

program = [2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0]
print(f"Convert program {program} to A:")
results = to_A(program)
print(sorted(results))
print(min(results))

