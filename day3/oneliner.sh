grep -oE "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)" input | awk '/do\(/{x=0};/don/{x=1}/mul/&&!x' | tr ',mul' '* ' | paste -sd+ | bc
