def out(A):
    B = (A%8)^2
    return (B ^ 7 ^ (A>>B)) % 8

A = 27334280
for i in range(9):
    print(out(A))
    A //= 8

print()
print(f"Oktal A {oct(27334280)}")
print()

probes = [0]
for stelle, x in enumerate([4, 0, 7, 5, 6, 3, 5, 6, 7]):
    new_probes = []
    for probe in probes:
       for i in range(8):
           if out(probe*8 + i) == x:
               new_probes.append(i)

    print(f"{stelle=} {new_probes=}")
    probes = new_probes
    



