BEGIN { exec=1; sum = 0; }
/do\(\)/ { exec=1; }
/don't\(\)/ { exec=0; }
/mul\(/ { if (exec) print $0; }
