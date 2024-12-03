#!/bin/sh
echo "define void do() { x = 1; }" > tmp.bc
echo "define void dont() { x = 0; }" >> tmp.bc
echo "define void mul(a,b) { sum += (x*a*b); }" >> tmp.bc
echo "do()" >> tmp.bc
grep -oE "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)" input | sed 's/don.t/dont/' >> tmp.bc
echo "sum" >> tmp.bc
echo "quit" >> tmp.bc
bc -q tmp.bc
