def combo(op):
    if 0<=op<=3: return (str(op))
    if op==4: return "A"
    if op==5: return "B"
    if op==6: return "C"

def adv(op):
    global ip
    ip+=2
    print(f"A=A>>{combo(op)}")

def bxl(op):
    global ip
    ip+=2
    print(f"B=B^{op}")

def bst(op):
    global ip
    ip+=2
    print(f"B={combo(op)}%8")

def jnz(op):
    global ip
    ip+=2
    print("jnz(0)")

def bxc(op):
    global ip
    ip+=2
    print(f"B=B^C")

def out(op):
    global ip
    ip+=2
    print(f"out({combo(op)}%8)")

def bdv(op):
    global ip
    ip+=2
    print(f"B=A>>{combo(op)}")

def cdv(op):
    global ip
    ip+=2
    print(f"C=A>>{combo(op)}")

instr=dict()
instr[0]=adv
instr[1]=bxl
instr[2]=bst
instr[3]=jnz
instr[4]=bxc
instr[5]=out
instr[6]=bdv
instr[7]=cdv
program=[2,4,1,2,7,5,0,3,1,7,4,1,5,5,3,0]
ip=0
while True:
    if ip >= len(program):
        break
    instr[program[ip]](program[ip+1])

