def combo(op):
    global A,B,C,ip
    if 0<=op<=3: return op
    if op==4: return A
    if op==5: return B
    if op==6: return C

def adv(op):
    global A,B,C,ip
    A=A//pow(2,combo(op))
    ip+=2

def bxl(op):
    global A,B,C,ip
    B=B^op
    ip+=2

def bst(op):
    global A,B,C,ip
    B=combo(op)%8
    ip+=2

def jnz(op):
    global A,B,C,ip
    if A==0:
        ip+=2
        return
    ip=op

def bxc(op):
    global A,B,C,ip
    B=B^C
    ip+=2

def out(op):
    global A,B,C,ip
    print(f"{combo(op)%8},",end='')
    ip+=2

def bdv(op):
    global A,B,C,ip
    B=A//pow(2,combo(op))
    ip+=2

def cdv(op):
    global A,B,C,ip
    C=A//pow(2,combo(op))
    ip+=2

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
A,B,C=[27334280,0,0]
while True:
    if ip >= len(program):
        break
    instr[program[ip]](program[ip+1])

