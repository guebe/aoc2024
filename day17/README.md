part1 was writing a trivial cpu simulation

part2 was more involved. We need to find the register value
for a program for which a given programs output is the
program itself (this is called a quine).

So first we had to reverse engineer the quine. Thus I wrote
a disassembler. This was also simple.

Now comes the hard part. Undoing the algorithm to find
all possible input register values to produce the given 
program output.
Using manual analyzation of the program code I reversed
the code. The reversed algorithm probes the possible
output of the A register (there are more possibilities
going in the other direction) - this was also the reason
it was hard.
Thus a solver for this program was written manually.
The solver was tested using simple answer from part1,
before using the same solver for the quine.

After finding all possible input values for the given
program output it was a matter of determining the smallest
register value which led to the wanted output (simple again).

Favourite day so far!

