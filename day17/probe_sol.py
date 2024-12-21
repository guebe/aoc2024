def out(A):
    B = (A%8)^2
    return (B ^ 7 ^ (A>>B)) % 8

#A = 27334280
#for i in range(9):
#    print(out(A))
#    A //= 8
#
#print()
#print(f"Oktal A {oct(27334280)}")
#print()
#Program: 2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0

#print(out(5))
#print(out(43))

probes = set([0])
for stelle, x in enumerate([0, 3, 5, 5, 1, 4, 7, 1, 3, 0, 5, 7, 2, 1, 4, 2]):
    new_probes = set()
    for probe in probes:
       for i in range(8):
           if out(probe*8 + i) == x:
               new_probes.add(probe*8+i)

    print(f"{stelle=} {new_probes=}")
    probes = new_probes

print(min(probes))
#{5}
#{3, 7}
#{2}
#{2}
#{0, 4}
#{1}
#{0}
#{4}
#{7}
#{5, 6}
#{2}
#{3}
#{6, 7}
#{0, 4}
#{1}
#{7}

A = 0o5322010475236017
for i in range(16):
    print(out(A))
    A //= 8


