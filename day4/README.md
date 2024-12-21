
A character based board was given.

In this board you have to count certain strings.

In the first part the search string was XMAS.
Written horzontal, vertical and diagonal. Also reversed variants shall be accepted.

In the second part only diagonal crossings of MAS needed to be searched.

First I tried doing the code variation using matrix transformations.
This was too hard so I rewrote the code to use simple two dimensional array lookup.

Problem on first part was also checking all possible array index violations.
However I found a simple and concise way checking only the worst case.
Array bounds checking was no problem on the second part because the search was
symmetrical and to avoid index violations the input could be changed.

Part 2 was definitely simpler than part 1.

