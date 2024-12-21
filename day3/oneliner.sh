grep -oE "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)" input | awk -f x.awk  | sed 's/mul(//' | sed 's/)//' | sed 's/,/*/' | tr '\n' "+" | sed 's/.$/\n/' | bc
