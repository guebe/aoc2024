grep -oE "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)" input | awk '/do\(/{dont=0};/don/{dont=1}/mul/&&!dont' | tr -d 'mul()' | tr ',\n' '*+' | sed 's/.$/\n/' | bc
